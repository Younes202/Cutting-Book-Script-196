import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Function to send an email with attachments
def send_email(subject, body, to_email, pdf_files):
    # Email configuration (change these settings)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'murichesys@gmail.com'
    smtp_password = 'ncpo ymvw imzs'  # Replace with your App Password

    # Create an SMTP connection
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)

    # Create a message container
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = ', '.join(to_email)
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF files
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as pdf:
            part = MIMEApplication(pdf.read(), Name=os.path.basename(pdf_file))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf_file)}"'
            msg.attach(part)

    # Send the email
    smtp.sendmail(smtp_username, to_email, msg.as_string())
    smtp.quit()

# Input PDF file names
pdf_files = []
while True:
    pdf_name = input("Enter the name of a PDF file (or press Enter to finish): ")
    if not pdf_name:
        break
    if os.path.isfile(pdf_name) and pdf_name.endswith('.pdf'):
        pdf_files.append(pdf_name)
    else:
        print(f"'{pdf_name}' is not a valid PDF file or does not exist. Please try again.")

if not pdf_files:
    print("No valid PDF files entered. Exiting.")
else:
    # Input email addresses
    to_email = input("Enter the email addresses (comma-separated) to send the PDF files to: ").split(',')

    # Input email subject and body
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")

    # Send the email
    send_email(subject, body, to_email, pdf_files)
    print(f"Email sent successfully to {', '.join(to_email)} with {len(pdf_files)} attached PDF(s).")

