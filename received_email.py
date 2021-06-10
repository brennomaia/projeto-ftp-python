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
result, id_email = server.search(None, 'ALL')   
email_id = id_email[0].split()

#email_id = []
#for block in id_email:
    #email_id += block.split()


#Trazendo o id"email" mais recente
id_email_recent = email_id[-1]

#Trazendo o id"mail" mais antigo
#id_email_old = email_id[0]

#Lendo o conteudo do ultimo email em bytes
#convertendo o email em bytes para utf-8
result2, email_data = server.fetch(id_email_recent, '(RFC822)')
_, b = email_data[0]
message = email.message_from_bytes(b)
for part in message.walk():
    if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
        body = part.get_payload(decode=True)
        body2 = str(body)

        if 'n33v0x' in body2:
            
        else:
            print("Palavra não contrada")