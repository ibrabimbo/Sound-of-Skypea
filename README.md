**The Sound of Skypea**

A battery-powered, aerial system that records the vibration of its body caused by free fall, then lands safely with a parachute.

![picture](https://github.com/ibrabimbo/Sound-of-Skypea/blob/main/skypea%20topright.png=true)

**Why?**

This year, I participated in the Hungarian CanSat competition, and last year in a local physics-engineering project. They had one thing in common: I sewed the parachute. In my time working on the model satellite for CanSat I learned a few things about designing aerial 3d prints and working with electronics. With my experience, I want to solve an age old question: is it possible to record the whistling sound a nerf bullet makes, from within its body, while still in the air? Physics call this effect the Helmholtz resonance. The rushing air on the outside vibrates the air within the flying chamber at a specific frequency, thus producing sound. 

I decided to build something that is capable of recording this, while also

* keeping complexity low  
* adding a landing system, so its reusable and safe  
* looking cool

**Assembly**

So you want one of these for yourself? No problem, the following guide will walk you through building it step by step.

**1\. Components**

You’ll have to source some components to build The sound of Skypea. You can find a list of everything needed in the table below. Links are included to make the shopping experience faster, but you can also go to alternative stores.

| Component | Description | Link |
| ----- | :---- | :---- |
| Adafruit Feather RP2040 Adalogger | main board | https://eu.mouser.com/ProductDetail/Adafruit/5980?qs=IKkN%2F947nfCnlS5PgbpnkA%3D%3D |
| Adafruit I2S MEMS ICS-43434  | microphone | https://eu.mouser.com/ProductDetail/Adafruit/6049?qs=olJun0bQHM88XeFsw90dVw%3D%3D |
| SG92R  | servo motor | https://eu.mouser.com/ProductDetail/Adafruit/169?qs=GURawfaeGuBHe0ZgcSsTjA%3D%3D |
| Adafruit MiniBoost 5V | booster | https://eu.mouser.com/ProductDetail/Adafruit/3661?qs=W0yvOO0ixfEzr%2F%252BSbf0hYQ%3D%3D |
| Li-Po Battery LP852040 | battery | https://www.akyga.com/products/873-li-po-battery-lp852040-akyga-aky0661-3-7v-620mah-pcm-jst-2-pin-connector-150mm.html |
| JST-PH 2.0 | battery cable | https://eu.mouser.com/ProductDetail/Adafruit/261?qs=GURawfaeGuDeA9XsXeF0ug%3D%3D |
| CNC KitchenHeat Set Inserts  | threaded insert | https://www.3djake.hu/cnc-kitchen/m25-standard-menetbetet?sai=15444 |
| cylinder head M 2 | screws | locally sourced |
| Dupont wires | jumper wires | locally sourced |
| MICROSD MEMORY CARD | sd card | https://eu.mouser.com/ProductDetail/ADLINK-Technology/Micro-SD-Memory-Card-32GB-TS32GUSD420T?qs=VJzv269c%252BPaEasM5SptuWg%3D%3D |
| SANWEAL120PCS/200PCS Fishing Weights Sinkers  | lead (fishing weights) | https://www.amazon.com/Fishing-Weights-SANWEAL-Removable-Including/dp/B096VLXPRJ/ref=sr\_1\_8?crid=2APA4P44H81OC\&dib=eyJ2IjoiMSJ9.nQvHi2aLW1y48RL51ZUzPd0F6E8PQ1SLJs0fs7tgkeYXlcJfFZuJQNBv2jagtvS9WUBzw8kRz4DnzINHXfDYB0q\_yqMwfaD2n5vmzZEvWExS8Klb9qG1RRlCi7egEFRrbrl7DZoieBwzMusvJMu9zx8-zD9i1ct4ojFCVH3eYmyNLAHY0Df8iL7TkMeQjdn5dtDUidgdY5HwmlMLCFK0O-ckBwSG\_W3GSh1FkLh2nU12f2lAdZo209C8g74Tk8BKnolkNCC0mls2jWQ5nv-6wL6m0LPhPI-GSUFWtLJrncA.xpFqImHCX1mhfefNpWzQDkMVmpndfLNeeYhprxQKBcE\&dib\_tag=se\&keywords=fishing%2Bweights\&qid=1779483113\&sprefix=fishing%2Bwei%2Caps%2C223\&sr=8-8\&th=1 |

Of course, electronics and screws are not “everything”. The body itself is 3d printed. You will need to print some parts to finish the build. A  3d printer is recommended, as well as some soldering skills.

**2\.**  **3D printing**

Start by 3d printing the models, first the body (part 1\) and then the smaller components, if your printer isn’t capable of handling it all at once.

You can find the files in the  “STL” folder.

Print each part once. Afterwards, you might have to use sandpaper to even out the threads on part 1 and 2, so that later they can be connected.

**3\. Inserts**

You will find insertable screw threads in the BOM. This is where they come into play. Different parts hold together with screws, so you'll need to install these threaded inserts into the 3d parts.

1. Get yourself 10 inserts from the packet, they should be 2.5mmx4mm, as listed in the BOM.  
2. Locate the 10 holes on the top of the body (wider end).  
3. Populate the holes with the inserts one by one, based on the issued instructions received with the inserts.

**4\. Soldering**

Follow this wiring diagram to connect then electronics. You might need to cut off a plug from the end of the servo’s wires, feel free to do so. Also, keep in mind that even at this stage, the microphone on the Adafruit I2S MEMS should be facing away , this is crucial because of the way it sits in the build and also allows you to differentiate the pins easier.

**5.Software**  
Download circuit python ( from [circuitpython.org](http://circuitpython.org) ) onto the adalogger and load the .vscode on to it.

Then, enter the bootloader by holding down the “Boot” button, and while continuing to hold it, press and release  the “Reset” button. Keep holding the Boot button until the RPI-RPI2 drive. The RPI-RPI2 drive will disappear when the firmware is loaded.

**6\. Absolute Assembly**  
*Last but not least, you need to actually put the parts together.*  
 

1. Put your SD card into the adalogger.  
2. Place the adalogger onto the main body, like you see in the onshape file assembly.  
3. Screw it in, all 4 holes with the screws you bought earlier.   
4. Repeat this process with the booster as well as with the microphone.  
     
   *Pay attention to the wires and soldering, try not to damage your precious work.*  
     
5. Plug the battery in to the adalogger and place it on the main body based on the onshape assembly.   
6. Grab the battery attachment 3D part and place it on the battery, then screw it in.  
7. Repeat this process with the servo.   
8. Take your servo arm (3D printed part) and attach it to the servo’s axis (might have to remove the part it originally came with).  
     
   *Don’t position it down yet\! It should stay at a 90 degree angle for now.*  
     
9. Attach your parachute to the attachment point in the very center of the upper face of the main body (where all the other electronics and extra components go). Take the 8 strings coming out of the parachute and tie them around the attachment point’s middle part, by knotting one end of the string to the other, getting a fully secured parachute in the end.   
10. Fold the secured parachute in harmonica style (one left, one right, this helps it open), and place it on top of the main body, right above the attachment point, while paying attention to not one part of the parachute overlapping the walls.  
11. Close the arm of the servo onto the folded parachute, so that it holds it in place.  
12. Take the tip of the print (part 2\) and fill it up with the fishing weights\! This is crucial because it ensures that the system will fall in the correct position.  
13. Screw it into the narrower end of part 1\.

	*Thats it, you’re done.*  
