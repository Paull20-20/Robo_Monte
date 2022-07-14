import pathlib


#verificando a quantidade de arquivos dentro da pasta que terá os arquivos a serem enviados para o drive.
numberFile = 0
for path in pathlib.Path(f'/home/tiago.oliveira/Área de Trabalho/teste_upload/').iterdir():
    if path.is_file():
        numberFile += 1

print(numberFile)