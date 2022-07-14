import os
import pathlib


#verificando a quantidade de arquivos dentro da pasta que terá os arquivos a serem enviados para o drive.
numberFile = 0
for path in pathlib.Path(f'/home/tiago.oliveira/Área de Trabalho/teste_upload/').iterdir():
    if path.is_file():
        numberFile += 1

print('Quantidade de arquivos dentro do diretório: ', numberFile)


print('*************---------------***************')

ano = 2020

for i in range(0, numberFile): #verificando se existe tal arquivo dentro do diretório
    file = os.path.exists(rf'/home/tiago.oliveira/Área de Trabalho/teste_upload/{ano}teste.pdf')
    print(file)
    ano = ano + 1
    
    



