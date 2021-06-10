import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date

#Informações do email para conexão e envio
email_from = os.getenv('email_from')
email_passwd = os.getenv('email_passwd')
email_to = os.getenv('email_to')

data_today = date.today()

#Conectando a onta de email

host = os.getenv('host')
server = smtplib.SMTP(host, 587)
server.starttls()
server.login(email_from, email_passwd)

#Corpo do email
body_msg = "Um novo Patch de atualização foi encotrado.\n Para agendar a tarefa de atualização, digite a senha de confirmação: \n Para Cancelar/Stand-by a terefa, digite: GMUD cancelada"
### Criando o email para envio
msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = "Agendar a GMUD novosima " + data_today.strftime("%d %b %Y ")
msg.attach(MIMEText(body_msg,'html'))

#Eviando o email.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print('Email enviado com sucesso')

