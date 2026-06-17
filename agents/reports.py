from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(client_name, schedule, stats):

    filename = f"{client_name}_weekly_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph(f"Weekly Report - {client_name}", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Analytics", styles["Heading2"]))
    content.append(Paragraph(f"Average Score: {stats['avg_score']}", styles["Normal"]))
    content.append(Paragraph(f"Best Day: {stats['best_day']}", styles["Normal"]))

    content.append(Spacer(1, 12))
    content.append(Paragraph("Content Breakdown", styles["Heading2"]))

    i = 0
    while i < len(schedule):

        item = schedule[i]

        text = f"""
        Day: {item['day']} <br/>
        Idea: {item['post']['idea']} <br/>
        CTA: {item['post']['cta']}
        """

        content.append(Paragraph(text, styles["Normal"]))
        content.append(Spacer(1, 10))

        i += 1

    doc.build(content)

    return filename
