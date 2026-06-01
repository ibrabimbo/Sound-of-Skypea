**The Sound of Skypea**

A battery-powered, aerial system that records the vibration of its body caused by free fall, then lands safely with a parachute.

![Logo](https://github.com/ibrabimbo/Sound-of-Skypea/blob/main/Pictures/skypea_topleft.png)

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

| Component | Price in USD | Description | Link |
| ----- | :---- | :---- | :---- |
| Adafruit Feather RP2040 Adalogger | 15 | main board | https://eu.mouser.com/ProductDetail/Adafruit/5980?qs=IKkN%2F947nfCnlS5PgbpnkA%3D%3D |
| Adafruit I2S MEMS ICS-43434  | 5 | microphone | https://eu.mouser.com/ProductDetail/Adafruit/6049?qs=olJun0bQHM88XeFsw90dVw%3D%3D |
| SG92R  | 6 | servo motor | https://eu.mouser.com/ProductDetail/Adafruit/169?qs=GURawfaeGuBHe0ZgcSsTjA%3D%3D |
| Adafruit MiniBoost 5V | 3 | booster | https://eu.mouser.com/ProductDetail/Adafruit/3661?qs=W0yvOO0ixfEzr%2F%252BSbf0hYQ%3D%3D |
| Li-Po Battery LP852040 | 8.67 | battery | https://www.akyga.com/products/873-li-po-battery-lp852040-akyga-aky0661-3-7v-620mah-pcm-jst-2-pin-connector-150mm.html |
| JST-PH 2.0 | 0.75 | battery cable | https://eu.mouser.com/ProductDetail/Adafruit/261?qs=GURawfaeGuDeA9XsXeF0ug%3D%3D |
| CNC KitchenHeat Set Inserts  | 15.47 | threaded insert | https://www.3djake.hu/cnc-kitchen/m25-standard-menetbetet?sai=15444 |
| cylinder head M 2 | 8 | screws | locally sourced / https://www.amazon.com/WZHUIDA-Screws-Assortment-M2x4mm-Washers/dp/B0F93XL3WK/ref=sr_1_8?crid=3GG71MWCZ1ATH&dib=eyJ2IjoiMSJ9.bJmSRx0fTW4Nuo1Ws-nwrforW57EpTe0ZCpBm32fW7HS6qFWlZ01KHaYa7Ovih0iE2u_Oou84YRr4Oit4l9-jClSgThBtNAF8MmLX6Nt7HrZslr0eGZ7Pg3K5B0Y2gE0aiseIlp9XaQJ-5Q8f08yC2WWd5x--uGyAuwFGflfHEV34gxyQL-fP_bMoExulEbeg0BEPVQQ52OzriXOUvznFtL6waU-CzwaI0qzrzumvYk.hFhaWtfrMGVPvZDL2boMsuEKIYHyJcRUHRgNFej2ZH4&dib_tag=se&keywords=screw%2Bcylinder%2Bhead%2Bm2%2Bx%2B6&qid=1779656474&sprefix=screw%2Bcylinder%2Bhead%2Bm2%2Bx%2B%2Caps%2C239&sr=8-8&th=1 |
| Dupont wires | 6 | jumper wires | locally sourced / https://www.amazon.com/California-JOS-Breadboard-Optional-Multicolored/dp/B0BRTJXND9/ref=sr_1_3?crid=1W89FLOX7LIGD&dib=eyJ2IjoiMSJ9.SszVHKRXXxbEIG2ErBYrie2KzCkO4T65B91w6fTioeukwnR3EUmExJc8uF3q_qFfS4ZYrBavI4IztsW8LaddICn7wmukpXjriObjfiUIRDg4TqwYdOnKGwMduunjtKrF0JdKYd7gWwlneB2AwFR8ucVyEeOTPLMxDI28Pr7A0kIv1NN0-f4JF7YZPYXHXPRB21RwCtwzGbJsz7C1Ql_Y9D_JAVLlQs2NnELRMPh2qN4.zaMUYYbvRuriO4H-hys5oGMYQwPETU2Rgpj0c0SWHOU&dib_tag=se&keywords=dupont%2Bwires&qid=1779656564&sprefix=dupont%2Bwires%2Caps%2C261&sr=8-3&th=1 |
| MICROSD MEMORY CARD | 12.89 | sd card | https://eu.mouser.com/ProductDetail/DFRobot/FIT0394?qs=lqAf%2FiVYw9isxJnGlF1v2Q%3D%3D |
| SANWEAL120PCS/200PCS Fishing Weights Sinkers  | 7.95 | lead (fishing weights) | https://www.amazon.com/Fishing-Weights-SANWEAL-Removable-Including/dp/B096VLXPRJ/ref=sr\_1\_8?crid=2APA4P44H81OC\&dib=eyJ2IjoiMSJ9.nQvHi2aLW1y48RL51ZUzPd0F6E8PQ1SLJs0fs7tgkeYXlcJfFZuJQNBv2jagtvS9WUBzw8kRz4DnzINHXfDYB0q\_yqMwfaD2n5vmzZEvWExS8Klb9qG1RRlCi7egEFRrbrl7DZoieBwzMusvJMu9zx8-zD9i1ct4ojFCVH3eYmyNLAHY0Df8iL7TkMeQjdn5dtDUidgdY5HwmlMLCFK0O-ckBwSG\_W3GSh1FkLh2nU12f2lAdZo209C8g74Tk8BKnolkNCC0mls2jWQ5nv-6wL6m0LPhPI-GSUFWtLJrncA.xpFqImHCX1mhfefNpWzQDkMVmpndfLNeeYhprxQKBcE\&dib\_tag=se\&keywords=fishing%2Bweights\&qid=1779483113\&sprefix=fishing%2Bwei%2Caps%2C223\&sr=8-8\&th=1 |
| sancua Rectangle Tablecloth - 60 x 84 Inch | 9 | parachute material | https://www.amazon.com/sancua-Rectangle-Tablecloth-Resistant-Decorative/dp/B07XPTJKQC/ref=sr_1_2_sspa?crid=3LE4GR0S8UGCR&dib=eyJ2IjoiMSJ9.5nZdR6RlI8K1BhvFi7O-TTb33W3aS0SjoFPJ1bKNqnVQuCCWKdDSvG3wRCQPycKt9dcfZeKZ-PSGWlyRuDQH4exiwwgINqPu1vsyE6So6TqmHlXVrnVlXL1xETAwO9DCY7fAjUU9PpOLSguq7nXXg0_uOlR3jNed2sRhgFPBb6vK3-LCq2iUu1vjaRALBxMvu_4CLTqxKrw0WsQOYEhSIKUVqZ85wAg_H1kQLzAPdu40soSsJkm3lbAHmInQdxk8-JgcYgk3KDUqyGMk90NJMi702D1A_HIKjn7DwWWLAU8.OEvD-EgdP-ClrHYuLX6tkS0AbxKYpqu1FWgI1KP4QrA&dib_tag=se&keywords=tablecloth&qid=1779655947&sprefix=tablecloth%2Caps%2C272&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1 |
| Bright White Twine String | 7 | parachute string | https://www.amazon.com/White-Mason-Line-String-Construction/dp/B0BFCDFWVS/ref=sr_1_7?crid=33TTOY9FKV6TU&dib=eyJ2IjoiMSJ9.zGMcXR0SibP8Dx1OYaCjAI56o-x0hnb5oNCr5Y-dJGcHn-pX9t4F39ZFPHV76Uh8jSW6zUYeyze5wukt36UyIRRWH1ALbgCcdJdbxjR8-Z7exbvQg3G_JBD0n3bCv0N1LLRI62TUDauw6iREOU7mO9mm34hOn2noAz8S3KgKQra4evG00jD4_Q1ZpKUHAXY4F1xGT4qwNkq7yo-80Vd7XQL5l8XFtW_0C8z3_A61kskp8LE-wS1q_EVB5CZWzfY7_R3gFL7OwE0GWA8XXuI9BRAcrQnyNKqOMq_i5t40CSk.hKQ_ZBDThkbLk3cFiAF-Eu3Dy3rV1ZDpbc_mFIV_nz4&dib_tag=se&keywords=string&qid=1779656119&sprefix=string%2Caps%2C256&sr=8-7&th=1 |
| Space Trek Ripstop Nylon Parachute | 2 | complete parachute | make your own (recommended)/ https://www.amazon.com/Space-Trek-Ripstop-Parachutes-Rocketry/dp/B0D9ZJKVZY/ref=sr_1_13?crid=3Q4UC5ZPX5MJH&dib=eyJ2IjoiMSJ9.q81t9dbId1aHsYzVDdR4N6nWMFwDyyDPMZHsS3bz4ghPebLjuL-y6dEMM3UTaDQ2M2aFriYYkpVpQt04dF8mqAZnNvQsRrE5f6cB1MDBEHY6KyHcfu3qmEWms88aA8zPErVH29VFFBN0bp84JOexBBFzqhdnF-gC4W4ehR4CVwpBsL2ed1_YLfHocCqP_0F2EKo72OZx1OdfGqj5PxG4GAybq7Nhqb9ju83zjCsYbfdQjM6ocHfA0euabvFZ5AvWSETrvvxn0Dh9wykdjOPtYdyTUY1wynUpDIzTBXJtXcw.Dbr9mDp7SacsCnwO-WAArcm1I5YBq1xv16H9bwJ0tvk&dib_tag=se&keywords=small%2Bparachute&qid=1779968944&sprefix=small%2Bparachute%2Caps%2C279&sr=8-13&th=1 |
| Total | 106.73 | - | - |





The parts with amazon links are also easily sourced locally or from completely different sites, feel free to choose comfortable options.
The materials of the parachute (cloth and string) are completely for example, you can basically use any other types of these materials as long as it possesses basic endurance.
And even though you can buy a complete one, I recommend making one yourself.



Of course, electronics and screws are not “everything”. The body itself is 3d printed. You will need to print some parts to finish the build. A  3d printer is recommended, as well as some soldering skills.

**2\.**  **3D printing**

Start by 3d printing the models, first the body (part 1\) and then the smaller components, if your printer isn’t capable of handling it all at once.

You can find the files here:

Step files: [Step](https://github.com/ibrabimbo/Sound-of-Skypea/tree/main/Step)

STL files:  [STL](https://github.com/ibrabimbo/Sound-of-Skypea/tree/main/STL)

Print each part once. Afterwards, you might have to use sandpaper to even out the threads on part 1 and 2, so that later they can be connected.

**3\. Inserts**

You will find insertable screw threads in the BOM. This is where they come into play. Different parts hold together with screws, so you'll need to install these threaded inserts into the 3d parts.

1. Get yourself 10 inserts from the packet, they should be 2.5mmx4mm, as listed in the BOM.  
2. Locate the 10 holes on the top of the body (wider end).  
3. Populate the holes with the inserts one by one, based on the issued instructions received with the inserts.

**4\. Soldering**

![Logo](https://github.com/ibrabimbo/Sound-of-Skypea/blob/main/Pictures/wiring_plan.png)

I understand that this diagram may not be my best work, here is a soldering list for clarification: [wiring](https://github.com/ibrabimbo/Sound-of-Skypea/tree/main/wiring.md)

Follow this wiring diagram/list to connect then electronics. You might need to cut off a plug from the end of the servo’s wires, feel free to do so. Also, keep in mind that even at this stage, the microphone on the Adafruit I2S MEMS should be facing away , this is crucial because of the way it sits in the build and also allows you to differentiate the pins easier. The colors of the proposed wires dont mean anything, dont correlate them with purposes.

**5.Software**  
Download circuit python ( from [circuitpython.org](http://circuitpython.org) ) onto the adalogger and load the [.vscode](https://github.com/ibrabimbo/Sound-of-Skypea/tree/main/.vscode) on to it. But first, modify the servo_delay_seconds variable based on the last point of this README.

Then, enter the bootloader by holding down the “Boot” button, and while continuing to hold it, press and release  the “Reset” button. Keep holding the Boot button until the RPI-RPI2 drive. The RPI-RPI2 drive will disappear when the firmware is loaded.

**6. Descend System**

To actually make it safe to use the system, we must build the parachute system. You can alternatively buy the amazon one from the BOM, but the following guide can help you make your own: [parachute](https://github.com/ibrabimbo/Sound-of-Skypea/blob/main/parachute.md)


**7\. Absolute Assembly**  
*Last but not least, you need to actually put the parts together.*  

Onshape (for assembly reference): [assembly](https://cad.onshape.com/documents/749d855f21592cb7ad435800/w/52d14e606b9725a530c02d20/e/6858fd8794da090b422fa8f4) ( this assembly contains the 3d model of an adalogger with a hdmi connector instead of an sd card one, but it doesnt matter in our aspect )
 

1. Put your SD card into the adalogger.  
2. Place the adalogger onto the main body, like you see in the onshape file assembly.  
3. Screw it in, all 4 holes with the screws you bought earlier.   
4. Repeat this process with the booster as well as with the microphone.  
     
   *Pay attention to the wires and soldering, try not to damage your precious work.*  
     
5. Take the battery and place it on the main body based on the onshape assembly.   
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


**8\. How to "fly" it**

Choose a high point, like a building or a cliff, the important thing is that you know the height of which you are dropping the system from. It is preferable to be atleast 50 meters, since the longer the drop the better. 

For 50 meters, the servo_delay_seconds should be 1.20 seconds. Add 1 second every 30 meters, roughly calculating. Here is the formula to accurately calculate: t = √(2h/g). You get a figure, add five (later explained) and then subtract MINIMUM  2 and type it into the varieble. Preferrably substract more than 2 because this is the time that the parachute has to open under, in seconds. 

Climb up wherever you are dropping it from. If you followed the assembly carefully, your battery is not yet connected to the adalogger. Now is the time, connect it and from the moment of contact, start counting. After counting to 5 ( this is why we added it to the number), or alternatively starting a 5 second timer at the moment of connection ( recommended ), wait until it runs out and let go, so that the nose faces downwards. Pay attention not to fall with it tho, always grab onto something with your other arm.

ALWAYS HAVE SOMEBODY CLEAR THE SPACE UNDER YOU! It will fall slowly, but it is still not comfortable to be hit with. Trust me, I have done this many times, have someone look out under for bypassers.

I get it, this might sound a little dangerous. You are right, doing this in an urban area does require a lot of careful cooperation, but nonetheless is very cool if done right.. However, a drone-attachement is on the way, so that you can drop it from higher while also making the process easier. Stay tuned :)





![Logo](https://github.com/ibrabimbo/Sound-of-Skypea/blob/main/Pictures/zine_page.png)

