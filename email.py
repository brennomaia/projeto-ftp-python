import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_from = 'contatotik013@gmail.com'
email_to = 'brennomaia10@gmail.com'

#Infomações para conexão da conta de email.
host = 'smtp.gmail.com'
user = email_from


#Conectando a onta de email
server = smtplib.SMTP(host, 587)
server.starttls()
server.login(email_from, open('passwd.txt').read().strip())


#Corpo do email
body_msg = """
Estamos testando o envion do email.
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
