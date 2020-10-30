import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import confidential.credentials as cred

credentials = cred.Credentials()

def send_mail(destinations, text):
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(credentials.get_jenkins_mail_credentials(type="mail"), credentials.get_jenkins_mail_credentials(type="password"))
	for email in destinations:
		msg = MIMEMultipart()	   # create a message
		msg['From']=credentials.get_jenkins_mail_credentials(type="mail")
		msg['Subject']="3Pillars Jobs"
		msg.attach(MIMEText(text, 'plain'))
		msg['To']=email
		s.send_message(msg)
		del msg
