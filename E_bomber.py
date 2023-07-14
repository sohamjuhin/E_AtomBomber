import smtplib
from email.mime.text import MIMEText

# Function to generate multiple email addresses
def generate_multiple_emails(base_email, start_num, end_num):
    emails = []
    for num in range(start_num, end_num + 1):
        email = f"{base_email}{num}@example.com"
        emails.append(email)
    return emails

# Function to send emails
def send_emails(sender_emails, sender_password, recipient_email, email_subject, email_body):
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate SMTP port number
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_emails[0], sender_password)
        for sender_email in sender_emails:
            msg = MIMEText(email_body)
            msg['Subject'] = email_subject
            msg['From'] = sender_email
            msg['To'] = recipient_email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent from {sender_email} to {recipient_email}")
        server.quit()
        print("All emails sent successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

# Get custom inputs from the user
base_email = input("Enter the base email: ")
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

sender_emails = generate_multiple_emails(base_email, start_num, end_num)
sender_password = input("Enter the sender email password: ")
recipient_email = input("Enter the recipient email: ")
email_subject = input("Enter the email subject: ")
email_body = input("Enter the email body: ")

send_emails(sender_emails, sender_password, recipient_email, email_subject, email_body)
