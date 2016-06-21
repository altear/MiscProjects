import smtplib

#instructions
#gmail account: username=franken.llama.sama@gmail.com; password=DraculasDentalDam

#setup account for smtpserver:
#1) goto https://mail.google.com/mail/u/1/#settings/fwdandpop and enable imtp and pop
#2) if texting, find service provider's sms server (ex. @msg.telus.com)

username="franken.llama.sama@gmail.com"
password="DraculasDentalDam"
recipient=["6133142234@txt.bell.ca", "telfer006@gmail.com"]
subject="Subject: (test)) A large dairy animal approached Zaphod Beeblebrox's table...\n"
message='"... I just don\'t want to eat an animal that\'s standing there inviting me to," said Arthur, "It\'s heartless."\
\
"Better than eating an animal that doesn\'t want to be eaten," said Zaphod.\
\
"That\'s not the point," Arthur protested. Then he thought about it for a moment. "Alright," he said, "maybe it is the point. I don\'t care, I\'m not going to think about it now. I\'ll just... er [...] I think I\'ll just have a green salad," he muttered.\
\
"May I urge you to consider my liver?" asked the animal, "it must be very rich and tender by now, I\'ve been force-feeding myself for months."\
\
"A green salad," said Arthur emphatically.\
\
"A green salad?" said the animal, rolling his eyes disapprovingly at Arthur.'

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
#smtpObj.starttls() #when connection isn't ssl
smtpObj.login(username, password)


smtpObj.sendmail(username, recipient, subject + message)
