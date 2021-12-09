CSC226 Project

**Term**: Fall 2021

️**Author(s)**: Sabira Duishebaeva


**Author Note**: 
The program will only run if you have access to the internet. 


**References**: 

1- This video covers most of the aspects of Tkinter. It helped me a lot to understand its basics and how to use it properly https://www.youtube.com/watch?v=YXPyB4XeYLA&ab_channel=freeCodeCamp.org
2- From this website I learned about Canvas, which allows drawing in Tkinter https://www.tutorialspoint.com/python/tk_canvas.htm
3-  From this website I learned how to use text modification event in Tkinter https://www.pythontutorial.net/tkinter/tkinter-stringvar/
4- This website helped me learn how to deactivate or activate the button https://stackoverflow.com/questions/53580507/disable-enable-button-in-tkinter/53580612
5- I used the API of this website to search for images in Google https://serpapi.com/images-results
6- From this website I learned how to download and save images https://www.geeksforgeeks.org/python-pil-image-save-method/
7- From this website I learned how to save to a JSON file https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file

---

## Milestone 1: Setup, Planning, Design (due 1 Dec 2021)

**Title**: Items Barcode Generator

**Purpose**: 

My program will not only generate a random UPC Barcodes for the items that the user will type in the program, 
but also draw a barcode for it and also display an appropriate for this item image from Google. 
Also, the user can save the information about this item in a JSON file. Thus, this program can be used by people who work in shops
to generate barcodes and images of the items in their shops. 

**Sources**: 

A08 - UPC Bar code

**CRC Card**: 

CRC CARD LINK: https://docs.google.com/document/d/1alo3J6SiLNO59cr8YVD90KqUAc_PcugukqiccZ3GSOA/edit?usp=sharing
![alt text](
image/SABIRA_CRC.PNG)


---

## Milestone 2: Code (due 3 Dec 2021)

---
Done

## Milestone 3: Virtual Check-In (due 6 Dec 2021)

**Completion Percentage**: 90-100%

**Confidence**: I feel very confident about this project. I have come up with the solutions for the implementation ideas I had in my mind. 
I developed almost all the necessary functions, and my program seems to be working in a correct way. 

## Milestone 4: Final Code, Presentation, Demo (due 10 Dec 2021)

### ❗User Instructions

After the user hits the "Run" button, the user will see an interface of my program.
First, he needs to input a name of the item (any item you can think of that you can get from the shop) and then click the "Generate Barcode" button.
After that, the Barcode for this item will be generated along with the appropriate picture from the Google for this item and the barcode lines. 
Then, the user can/should click the "Save" button to save the information about this item in the JSON file. 

### ❗Errors and Constraints
Every program has bugs or features that had to be scrapped for time. Use this section to create a bullet list of all known errors and deficiencies that remain in your code. Bugs found that aren't acknowledged here will be penalized.

### ❗Reflection

As a person, who is interested in business and shopping, I found the UPC Barcode assignment one of the most interesting labs to me.
  I came up with the decision on how to develop this lab into something that can be useful for people who own shops.
  I got excited about the idea that this program can actually help shop owners generate barcodes and images of the items for their shops.

  
My initial design did not differ much from the final - the base idea was to generate the barcode and it remained the same. However,
I was also thinking of adding some more functionality to the program and came up with two ideas.
The first idea was to add the image generator - it would generate the first image from the Google Search for the item name 
that the user input. The second idea was to be able to save this information about the item: its name, barcode, image, link and etc. Thus,
the initial design did not have this functionality and this is how it was different in the beginning. 

  
I learnt a lot of new things from the project along with the fact that I also strengthened some of my previous skills by creating this program.
For example, I had a prior experience working with JSON flat database systems in the web development. Thus, I thought that would be cool to use this skill in
this project as well by allowing the user to save the items' information in a separate JSON file, so that the
shoppers would be able to keep track of their items in the shop. I also
learned how to fetch images from the Google Search and display them in 
your program - that was the coolest part I am most proud of.
  
The most challenging part was to develop the function where it would generate 
the first image from the Google Search. I had to use various websites and StackOverflow
to see how people fetch images from the Google Search. It took me a while
to understand how the API keys work and all API-related libraries.
Althugh the documentation in their libraries are  relatively straight-forward,
applying their existing templates in your own code was the most difficult part. 

In the future, I would enhance this project by allowing the user to generate 
  not only the UPC type of the barcode, but also other types of the barcodes. 
  I would also work more on the user interface and make it more interactive. 
  
