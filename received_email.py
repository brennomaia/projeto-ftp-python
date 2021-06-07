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

## Conectando o servidor de email
host = os.getenv('host')
server = imaplib.IMAP4_SSL(host)
server.login(email_from, email_passwd)

## Criando uma lista com de id dos email da pasta
server.select("bot_gmud")   #Selecinando a Pasta do email
result, id_email = server.uid('search', None, "ALL")    #Criando uma lista com os ids
id_item_email = id_email[0].split()     #Separando os Ids da lista e criando uma nova.

print(id_email)
print(id_item_email)
print(id_item_email[1])