import os
import shutil

caminho_origen = '\Users\brenno.maia\Documents\GitHub\projeto-ftp-python'
caminho_dest = '\\redbull\Atendimento\#Geral\#Atualizacao-Arquivos-Executaveis-Geral\Claro-Net\NETSMS\test-exe'

try: 
    os.mkdir(caminho_origen)
except FileExistsError as e:
    print(f'Pasta {caminho_dest} já existe')

for root, dirs, files in os.walk(caminho_origen):
    for file in files:
        old_file_path = os.path.join(root, file)
        print(file)