from fpdf import FPDF

def main():
    
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font('helvetica', size=48)
    pdf.cell(center=True,text="CS50 Shirtificate", h=57)
    #pdf.image('shirtificate.png', w=120,h=252,x="C",keep_aspect_ratio=True,)
    pdf.output("shirtificate.pdf")
    
    name = input('Name: ')
    
    print(f"your name is: {name}")
    
main()