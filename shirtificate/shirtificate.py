from fpdf import FPDF

def main():
    
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font('helvetica', size=48)
    pdf.cell(center=True,text="CS50 Shirtificate", h=57)
    pdf.image('shirtificate.png', w=190,x="C", y=70,keep_aspect_ratio=True,)
    
    
    pdf.set_font('helvetica', size=24)
    pdf.set_text_color(255, 255, 255)
    
    name = input('Name: ')
    
    pdf.cell(center=True,text=f"{name} took CS50", h=252)
    
    pdf.output("shirtificate.pdf")
    
    
main()