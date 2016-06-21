import imapclient

#instructions
#gmail account: username=franken.llama.sama@gmail.com; password=DraculasDentalDam

#setup account for smtpserver:
#1) goto https://mail.google.com/mail/u/1/#settings/fwdandpop and enable imtp and pop

username="franken.llama.sama@gmail.com"
password="DraculasDentalDam"
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(username, password)
imapObj.logout()
