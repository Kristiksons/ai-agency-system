from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def export_pdf(calendar):

    file_path = "report.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)

    y = 750

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "AI Content Strategy Report")

    y -= 40

    i = 0
    while i < len(calendar):

        item = calendar[i]

        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, f"{item['day']}")

        y -= 20

        c.setFont("Helvetica", 10)
        c.drawString(60, y, f"Idea: {item['idea']}")

        y -= 15
        c.drawString(60, y, f"Caption: {item['caption']}")

        y -= 15
        c.drawString(60, y, f"Score: {item['score']}")

        y -= 30

        # page break
        if y < 100:
            c.showPage()
            y = 750

        i += 1

    c.save()

    return file_path