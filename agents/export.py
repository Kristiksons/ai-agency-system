from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(calendar, filename="strategy_report.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    # ---------------- TITLE ----------------
    content.append(Paragraph("AI CONTENT STRATEGY REPORT", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("Weekly Social Media Plan", styles["Heading2"]))
    content.append(Spacer(1, 20))

    # ---------------- POSTS ----------------
    i = 0
    while i < len(calendar):

        item = calendar[i]

        content.append(Paragraph(f"<b>Day:</b> {item.get('day','')}", styles["Heading3"]))
        content.append(Spacer(1, 6))

        content.append(Paragraph(f"<b>Hook:</b> {item.get('idea','')}", styles["Normal"]))
        content.append(Spacer(1, 4))

        content.append(Paragraph(f"<b>Caption:</b> {item.get('caption','')}", styles["Normal"]))
        content.append(Spacer(1, 4))

        content.append(Paragraph(f"<b>Hashtags:</b> {item.get('hashtags','')}", styles["Normal"]))
        content.append(Spacer(1, 4))

        content.append(Paragraph(f"<b>Reel Script:</b> {item.get('reel_script','')}", styles["Normal"]))
        content.append(Spacer(1, 4))

        content.append(Paragraph(f"<b>Best Time:</b> {item.get('best_time','')}", styles["Normal"]))
        content.append(Spacer(1, 4))

        content.append(Paragraph(f"<b>Score:</b> {item.get('score','')}", styles["Normal"]))
        content.append(Spacer(1, 20))

        i += 1

    doc.build(content)

    return filename