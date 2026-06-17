import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(to_email, subject, body):

    sender_email = "your_email@gmail.com"
    sender_password = "YOUR_APP_PASSWORD_HERE"  # 👈 PUT IT HERE

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, sender_password)

    server.send_message(msg)
    server.quit()

    return "sent"