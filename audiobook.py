import pyttsx3
import PyPDF2
book = open('book.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
number_of_pages = pdfReader.numPages
print(number_of_pages)
speaker = pyttsx3.init()
for num in range(1, number_of_pages):
    page_number = pdfReader.getPage(10)
    text = page_number.extractText()
    speaker.say(text)
    speaker.runAndWait()