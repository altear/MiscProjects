import smtplib
import subprocess

#instructions
#gmail account: username=franken.llama.sama@gmail.com; password=DraculasDentalDam

#setup account for smtpserver:
#1) goto https://mail.google.com/mail/u/1/#settings/fwdandpop and enable imtp and pop
#2) if texting, find service provider's sms server (ex. @msg.telus.com)

username="franken.llama.sama@gmail.com"
password="DraculasDentalDam"
recipient=["6133142234@txt.bell.ca", "telfer006@gmail.com"]

subject='Subject: Process Complete\n'
file = "./testprog.sh"
#subprocess.Popen([file], stdout=subprocess.PIPE).stdout.read()
message=file

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
#smtpObj.starttls() #when connection isn't ssl
smtpObj.login(username, password)


smtpObj.sendmail(username, recipient, subject + message)
