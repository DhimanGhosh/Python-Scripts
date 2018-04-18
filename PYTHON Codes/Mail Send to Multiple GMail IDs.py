# Sending mail to multiple users from your Gmail account 
import smtplib

# list of email_id to send the mail
li = ["mail_ID_1@gmail.com", "mail_ID_2@gmail.com"]

for i in range(len(li)):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("Sender_Mail_ID", "Sender_Mail_ID_Password")
	message = "Message_you_need_to_send"
	s.sendmail("sender_email_id", li[i], message)
	s.quit()
