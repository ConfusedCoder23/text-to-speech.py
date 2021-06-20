# text-to-speech.py
# install pyttsx3 and PyPDF2 from terminal section.
this code will help to read your pdf so that u ca relax and listen your book.
import pyttsx3
import PyPDF2
book = open('your pdf here.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(page no.)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
