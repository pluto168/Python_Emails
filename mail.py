import smtplib
import getpass   #隱藏密碼

smtp_obj = smtplib.SMTP("smtp.google.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()

email = input("Enter your email: ")
password = getpass.getpass("Enter you password: ")
smtp_obj.login(email, password)

#send emails
from_address = email
to_address = email
subject = input("Enter subject: ")
message = input("Enter your message: ")
full_message = "subject: " + subject + "\n" + message

print(smtp_obj.send(from_address, to_address, full_message))
smtp_obj.quit()
