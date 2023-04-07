from fpdf import FPDF
import os


def add_text(pdf, text_filename):
    text = text_filename
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, text)


def add_image(pdf, image_filename, x, y, w=None, h=None):
    pdf.image(image_filename, x=x, y=y, w=w, h=h)


# def create_pdf(pdf_filename, text_filename=None, image_filename=None, image_x=None, image_y=None, image_w=None, image_h=None):
#     pdf = FPDF()
#     pdf.add_page()
#     if text_filename is not None:
#         add_text(pdf, text_filename)
#     if image_filename is not None:
#         add_image(pdf, image_filename, x=image_x,
#                   y=image_y, w=image_w, h=image_h)
#     pdf.output(pdf_filename+".pdf")

# def create_pdf(pdf_filename, text=None, image_filename=None, image_x=None, image_y=None, image_w=None, image_h=None):
#     if os.path.exists(pdf_filename+".pdf"):
#         pdf = FPDF('P', 'mm', 'A4')
#         pdf.add_page()
#         pdf.set_font('Arial', '', 12)
#         if text == None:
#             pdf.multi_cell(0, 10, text)
#         if image_filename is not None:
#             pdf.image(image_filename, x=image_x,
#                       y=image_y, w=image_w, h=image_h)
#         pdf.output(pdf_filename+".pdf", "F")
#     else:
#         pdf = FPDF()
#         pdf.add_page()
#         if text is not None:
#             pdf.set_font('Arial', '', 12)
#             pdf.multi_cell(0, 10, text)
#         if image_filename is not None:
#             pdf.image(image_filename, x=image_x,
#                       y=image_y, w=image_w, h=image_h)
#         pdf.output(pdf_filename+".pdf")

def create_pdf(pdf_filename, text_filename=None, image_filename=None, image_x=None, image_y=None, image_w=None, image_h=None, append=False):
    if append:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.cell(0, 10, "")
        pdf_file = open(pdf_filename+".pdf", 'ab')
    else:
        pdf = FPDF()
        pdf.add_page()
        pdf_file = open(pdf_filename+".pdf", 'wb')
    if text_filename is not None:
        add_text(pdf, text_filename)
    if image_filename is not None:
        add_image(pdf, image_filename, x=image_x,
                  y=image_y, w=image_w, h=image_h)
    pdf.output(pdf_file)
    pdf_file.close()


create_pdf("TEXT", text_filename="dsddvsdvdsvsdv")
create_pdf("TEXT", image_filename="./images/accept.png",
           image_x=0, image_y=10, image_w=200, image_h=100, append=True)
