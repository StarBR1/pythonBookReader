import fitz
import os

PDFLocation = os.path.join(os.path.dirname(__file__), 'exemple.pdf')

doc = fitz.open(PDFLocation)
bannedChar = input('Words you do *not* want  ')
header = "Header"
footer = "Page %i of %i" 

extractedPDF = ""

for page_number, page in enumerate(doc.pages(), start=1):
    page.insert_text((50, 50), header)
    
    page.insert_text(
        (50, page.rect.height - 50),
        footer % (page_number, doc.page_count),
    )
    extractedPDF += page.get_text()
    
def removeWords(extractedPDF, bannedChar):
    banned_words = bannedChar.split()
    words = extractedPDF.split()
    words = [word for word in words if word not in banned_words]
    productString = ' '.join(words)

    print(productString)

removeWords(extractedPDF, bannedChar)

if os.path.exists(PDFLocation):
    print(f'{PDFLocation} found')
else:
    print(f'{PDFLocation} not found')
