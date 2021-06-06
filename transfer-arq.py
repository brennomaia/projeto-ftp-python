import glob
import shutil

caminho_origen = '/projeto-net/projeto-ftp-python/'
caminho_dest = '/teste-arq/'
nome_arquivo = 'novosigma.exe'

print(glob.glob(caminho_origen))

#Capia e cola o novosima.exe para a pasta de destino
shutil.copy(caminho_origen + nome_arquivo, caminho_dest)