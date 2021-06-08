import os
import email
import imaplib
import urllib.parse
import re
from pathlib import Path
from dotenv import load_dotenv

email_from = os.getenv('email_from')
email_passwd = os.getenv('email_passwd')
email_to = os.getenv('email_to')

## Conectando o servidor de email imap
host = os.getenv('host')
server = imaplib.IMAP4_SSL(host)
server.login(email_from, email_passwd)


#Selecinando a Pasta da caixa de email "bot_gmud"
#Criando uma lista de ids com todos emails contidos em bot_gmud
#Separando os Ids(emails) da lista e criando uma nova lista com o split
server.select("bot_gmud")   
result, id_email = server.uid('search', None, "ALL")    
id_item_email = id_email[0].split()

#Trazendo o id"email" mais recente
id_email_recent = id_item_email[-1]

#Trazendo o id"mail" mais antigo
id_email_old = id_item_email[0]

#Lendo o conteudo do ultimo email em bytes
#convertendo o email em bytes para utf-8
result2, email_data = server.uid('fetch', id_email_recent, '(RFC822)')
utf_email = email_data[0][1].decode("utf-8")
email_message = email.message_from_string(utf_email)
print(email_message)




