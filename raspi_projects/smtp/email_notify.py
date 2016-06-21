import smtplib

#instructions
#gmail account: username=franken.llama.sama@gmail.com; password=DraculasDentalDam

#setup account for smtpserver:
#1) goto https://mail.google.com/mail/u/1/#settings/fwdandpop and enable imtp and pop
#2) 

username="franken.llama.sama@gmail.com"
password="DraculasDentalDam"
recipient="telfer006@gmail.com"
subject="Subject: If I could have just one more wish...\n"
message="I would like a tasty fish."

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
#smtpObj.starttls() #when connection isn't ssl
smtpObj.login(username, password)


smtpObj.sendmail(username, recipient, subject + message)
