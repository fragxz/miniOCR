#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip #used to save Var result into clipboard
import pytesseract
import webbrowser
import PIL.ImageGrab
from PIL import Image, ImageEnhance, ImageFilter
import requests
from difflib import SequenceMatcher
import difflib
import string
import time
import os
from PIL import ImageGrab

import re #regex
import os.path
import time

#function cleanhtml - erases html tags from the result
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


import subprocess
subprocess.call(['SnippingTool.exe']) #SnippingTool of your choice! I recommend SnippingToolPlus, because Windows integrated SnippingTool will be obsolete soon.

filepath = 'C:\\Users\\YOURNAME\\tmpfile.png' #Place where the tmpfile should get saved
otherfile = 'C:\\Users\\YOURNAME\\somefile.png' #Place where the tmpfile should get saved

while not os.path.exists(filepath):
   print("waiting..")
   time.sleep(1)
   im = ImageGrab.grabclipboard()
   if im:
      im.save('tmpfile.png','PNG')

if os.path.isfile(filepath):
   os.rename( filepath , otherfile)

   FrageText = pytesseract.image_to_string(Image.open("somefile.png"),lang="deu") #Befehl der das Bild in Text verwandelt (Bild wird geöffnet (Angabe des Pfades), Sprachpaket / Trainingsdaten für pytesseract = arial)
   FrageText = FrageText.replace('\n', ' ') # Ersetzt den Zeichenumbruch mit einem Leerzeichen 

   pyperclip.copy(FrageText) #Kopiert erkannten Text in die Zwischenablage

   print(FrageText)

   os.remove(otherfile)
   
else:
   raise ValueError("%s isn't a file!" % filepath)
   
