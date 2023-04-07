import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def create_pdf(pdf_filename, text):
    if os.path.exists(pdf_filename):
        # If the PDF already exists, open it and append a new page
        with open(pdf_filename, 'rb') as f:
            existing_pdf = PdfFileReader(f)
            output_pdf = PdfFileWriter()
            output_pdf.appendPagesFromReader(existing_pdf)
            output_pdf.addBlankPage()
            with open(pdf_filename, 'wb') as output_file:
                output_pdf.write(output_file)
    else:
        # If the PDF does not exist, create a new one with a single page
        with open(pdf_filename, 'wb') as output_file:
            output_pdf = PdfFileWriter()
            output_pdf.addBlankPage()
            output_pdf.write(output_file)

    # Open the PDF file for appending
    with open(pdf_filename, 'rb') as f:
        existing_pdf = PdfFileReader(f)
        output_pdf = PdfFileWriter()
        output_pdf.appendPagesFromReader(existing_pdf)

        # Add the text to the last page
        last_page = output_pdf.getNumPages() - 1
        output_pdf.getPage(last_page).mergePage(
            existing_pdf.getPage(last_page))
        output_pdf.getPage(last_page).addText(text)

        # Write the updated PDF to the file
        with open(pdf_filename, 'wb') as output_file:
            output_pdf.write(output_file)


create_pdf("my_pdf.pdf", "This is some text")
create_pdf("my_pdf.pdf", "This is some more text")
