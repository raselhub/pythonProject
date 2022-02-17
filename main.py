# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#Created by MOHAMMAD RASEL
#Copyright! @2022 All rights reserved.

import PyPDF2
import pyttsx3

book = open('oop.pdf', 'rb')
full_text = ""
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
var = pyttsx3.init()
var.setProperty('rate', 170 )
for num in range(6, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    var.say(text)
    full_text += text
    var.save_to_file(full_text, "audio.mp3")
    var.runAndWait()
