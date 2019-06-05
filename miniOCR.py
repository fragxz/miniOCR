#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip 	#to save data into clipboard
import pytesseract	#makes ocr possible
import PIL.ImageGrab	#grabs image from clipboard
from PIL import Image, ImageEnhance, ImageFilter #to use / interact with images
import time #used for the "waiting.." process
import os #for OS paths
from PIL import ImageGrab
import subprocess #to call a snipping tool // will be obsolete in a future version of this

subprocess.call(['SnippingTool.exe']) #SnippingTool of your choice! I recommend SnippingToolPlus, because Windows integrated SnippingTool will be obsolete soon.

filepath = '.\\tmpfile.png' #Place where the tmpfile should get saved, default: same directory
otherfile = '.\\recognizeMe.png' #Place where the tmpfile should get saved, default: same directory

while not os.path.exists(filepath):
   print("waiting for image..")
   time.sleep(1)
   im = ImageGrab.grabclipboard()
   if im:
      im.save('tmpfile.png','PNG')

if os.path.isfile(filepath): #checks if a file got created
   os.rename( filepath , otherfile)
   recognizedText = pytesseract.image_to_string(Image.open("recognizeMe.png"),lang="deu") #converts the image to text via optical text recognition (opens the image (path), languagepack for pytesseract)
   recognizedText = recognizedText.replace('\n', ' ') #replaces a line-break with space
   pyperclip.copy(recognizedText) #copies recognized text to the clipboard
   os.remove(otherfile) #removes the saved file
   
else:
   raise ValueError("%s isn't a file!" % filepath)
   
