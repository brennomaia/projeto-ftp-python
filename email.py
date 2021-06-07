import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Informações do email para conexão e envio
email_from = os.getenv('email_from')
email_passwd = os.getenv('email_passwd')
email_to = os.getenv('email_to')

#Conectando a onta de email
host = os.getenv('host')
server = smtplib.SMTP(host, 587)
server.starttls()
server.login(email_from, email_passwd)


#Corpo do email
body_msg = """
YOOOOOOOOOOOOOOOOOOOOOOOOO
MONDAMOM
"""
### Criando o email para envio
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = "Testando Email"
msg.attach(MIMEText(body_msg,'html'))

#Eviando o email.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print('Email enviado com sucesso')

