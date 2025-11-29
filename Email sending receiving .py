#!/usr/bin/env python3
import smtplib
import ssl
from email.message import EmailMessage
import getpass

def send_email():
    sender = input("Sender email: ").strip()
    receiver = input("Receiver email: ").strip()
    subject = input("Subject: ").strip()
    body = input("Message body: ").strip()
    password = getpass.getpass("App password (input hidden): ")

    if not sender or not receiver:
        print("Sender and receiver required.")
        return

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject or "No subject"
    msg.set_content(body or "")

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check email and app password.")
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    send_email()


