import smtplib
import time


file_path = input("Enter the path to the file containing email addresses: ")
email = input("Enter your Gmail address: ")
password = input("Enter your Gmail password: ")
message = input("Enter the message: ")
message_reload = int(input("How many messages do you want to send to each recipient?: "))

with open(file_path, 'r') as file:
    bomb_emails = file.readlines()

for bomb_email in bomb_emails:
    for _ in range(message_reload):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as mail:
                mail.starttls()
                mail.login(email, password)
                mail.sendmail(email, bomb_email.strip(), message)
                print("Message sent to {}".format(bomb_email.strip()))
                time.sleep(1)
        except Exception as e:
            print("An error occurred while sending the message to {}: {}".format(bomb_email.strip(), str(e)))

print("Done")
