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
def send_emails(sender_email, sender_password, recipient_email, email_subject, email_body):
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
    smtp_port = 587  # Replace with the appropriate SMTP port number
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        for email in sender_emails:
            msg = MIMEText(email_body)
            msg['Subject'] = email_subject
            msg['From'] = sender_email
            msg['To'] = recipient_email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent from {email} to {recipient_email}")
        server.quit()
        print("All emails sent successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

# Usage example
sender_email = "sender@example.com"
sender_password = "password"
recipient_email = "recipient@example.com"
email_subject = "Custom Email Subject"
email_body = "This is the body of the custom email."

base_email = "user"
start_num = 1
end_num = 5
sender_emails = generate_multiple_emails(base_email, start_num, end_num)

send_emails(sender_email, sender_password, recipient_email, email_subject, email_body)
