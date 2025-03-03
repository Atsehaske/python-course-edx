from fpdf import FPDF

def main():
    ''' main function '''
    shirtificate(input("Name: "))

def shirtificate(s):
    ''' creates pdf file with user input '''
    s = ' '+s+' took CS50'
    png_file_name = "shirtificate.png"
    pdf_file_name = "shirtificate.pdf"
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # header
    pdf.set_font("helvetica", style="B", size=32)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C")
    pdf.ln(0)
    # image
    pdf.set_y(50)
    pdf.set_x(0.5)
    pdf.image(png_file_name)
    # writing on png
    pdf.set_text_color(255,255,255)
    pdf.set_x(1)
    pdf.set_font("helvetica", style="B", size=28)
    pdf.cell(0, -240, s, align="C")
    # creation of pdf file
    pdf.output(pdf_file_name)

if __name__ == "__main__":
    main()
