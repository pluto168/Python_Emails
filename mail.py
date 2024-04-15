import smtplib
import getpass   #隱藏密碼

smtp_obj = smtplib.SMTP("smtp.google.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()

email = input("Enter your email: ")
password = getpass.getpass("Enter you password: ")
smtp_obj.login(mail, password)