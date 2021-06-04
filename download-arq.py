import os
from getpass import getpass
from ftplib import FTP


#Informações do servidor ftp e credenciais para conexão.
host = "192.168.1.4" #servidor 
users = "beta@dunk.com" #usuario
password = "02345678"#senha


dir_name = "pasta-teste-ftp\Origem_Para_Atualizar" #nome do diretorio acessado
file_name = "novosigma.exe" #nome do arquivo a ser baixado

#Varial que determina se devemos usar o modo ativo
nonpassive = False

#conctando no servidor  ftp
 # inserindo as credenciais
print("Conectando no FTP")
ftp = FTP(host)
ftp.login(user=users, passwd=password)


## Acessando o diretorio
#Listando o conteudo do diretorio
ftp.cwd(dirname=dir_name)
ftp.dir()

if nonpassive:
    ftp.set_pasv(False)
print("Inciando o download do arquivo...")

with open(file_name, 'wb') as local_arquivo:
    ftp.retrbinary('RETR ' + file_name, local_arquivo.write, 100000)
    ftp.quit()
