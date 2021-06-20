# text-to-speech.py
# install pyttsx3 and PyPDF2 from terminal 
this code will help to read your pdf so that u ca relax and listen your book.
import pyttsx3
import PyPDF2
book = open('pdf name.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init(pdf page number)
page = pdfReader.getPage()
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
