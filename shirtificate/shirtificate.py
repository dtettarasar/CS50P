from fpdf import FPDF

def main():
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    pdf.cell(text="CS50 Shirtificate")
    pdf.output("shirtificate.pdf")
    
    name = input('Name: ')
    
    print(f"your name is: {name}")
    
main()