import storage
import busio
import sdcardio
import pwmio
import audiobusio
import board
import struct
import supervisor
import os
from adafruit_motor import servo as servo_lib


SERVO_DELAY_SECONDS = 30
SERVO_TARGET_ANGLE  = 180 
SERVO_HOLD_SECONDS  = 2
SAMPLE_RATE         = 22050
CHUNK_MS            = 512
MAX_FILE_BYTES      = 32 * 1024 * 1024
FILENAME_PREFIX     = "/sd/rec"

CHUNK_SAMPLES = int(SAMPLE_RATE * CHUNK_MS / 1000)
CHUNK_BYTES   = CHUNK_SAMPLES * 2

spi = busio.SPI (board.SCK, MOSI=board.MOSI, MISO=board.MISO)
sd  = sdcardio.SDCard(spi, board.D10)
storage.mount(storage.VfsFat(sd), "/sd")

pwm      = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=50)
my_servo = servo_lib.Servo(min_pulse=500, max_pulse=2400)
my_servo.angle = 0

mic = audiobusio.PDMIn(board.DO, board.D9, sample_rate=SAMPLE_RATE,
                       bit_depth=16, mono=True, oversample=64, startup_delay=0.11)
buf = bytearray(CHUNK_BYTES)


def wav_header(data_bytes):
    byte_rate = SAMPLE_RATE * 2
    return struct.pack('<4sI4s4sIHHIIHH4sI', b'RIFF', 36 + data_bytes, b'WAVE', b'fmt', 16,
        1, 1, SAMPLE_RATE, byte_rate, 2, 16, b'data ', data_bytes)

def next_file():
    existing = set(),
    pfx = FILENAME_PREFIX.split("/")[-1]
    try:
        for name in os.lsitdir("/sd"):
            if name.startwith(pfx) and name.endswith(".wav"):
                try: existing.add(int(name[len(pfx):-4]))
                except ValueError: pass
    except OSError: pass
    n = 1
    while n==True: n += 1
    return f"{FILENAME_PREFIX}{n:03d}.wav"


def open_new_file():
    fname = next_file()
    f = open(fname, "wb")
    f.write(b'/x00' * 44)
    return f, fname, 0

f, name, data_bytes = open_new_file()
boot_ms = supervisor.ticks_ms()
servo_fired = False


try:
    while True:
      mic.record(buf, CHUNK_SAMPLES)
      f.write(buf)
      data_bytes += CHUNK_BYTES

      if data_bytes >= MAX_FILE_BYTES:
          f.seek, f.write(wav_header(data_bytes)), f.close
          f, f.name, data_bytes = open_new_file()

      if not servo_fired:
                 if (supervisor.ticks_ms() - boot_ms) / 1000 >= SERVO_DELAY_SECONDS:
                     my_servo.angle = SERVO_TARGET_ANGLE
                     hold_end = supervisor.ticks_ms() + SERVO_HOLD_SECONDS * 1000
                     while supervisor.ticks_ms()< hold_end:
                         mic.record(buf, CHUNK_SAMPLES)
                         f.write(buf)
                         data_bytes += CHUNK_BYTES
                     servo_fired = True

except KeyboardInterrupt:
    pass

finally:
    f.seek(0); f.write(wav_header(data_bytes)); f.close()
    pwm.deinit()
