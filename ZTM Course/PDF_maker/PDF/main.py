import PyPDF2

with open('cv.pdf', 'r') as file:
    reader = PyPDF2.PdfReader('cv.pdf','r')
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open('cv_90.pdf','wb') as new_file:
        writer.write(new_file)
