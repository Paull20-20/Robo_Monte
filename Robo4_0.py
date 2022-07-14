#from os import link
from operator import truediv
from xml.sax.xmlreader import Locator
from playwright.sync_api import sync_playwright, Playwright
import time
#from bs4 import BeautifulSoup
import os
import pathlib
#import pandas as pd
#import json
#from urllib.error import URLError


class Robo:

 
    def run(playwright: Playwright) -> None:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://drive.google.com/drive/folders/1zpJPcb4HuS5J5AHSMpMTF1sZLrFA0TFN")
        print("Funcionando!")


    
    with sync_playwright() as p:
        run(p)
        print("Funcionando2!")
        

        #Espera o elemento ficar visivel
    def waitElement(self, el):
        status = True
        while status:
            el = self.page.locator(el)
            if el != None and el.is_visible():
                status = False
        print("Funcionando3!")

    
        #print(page.title())
        


        #clicando no botão de fazer login
        locator = page.locator("//*[@id='gb']/div[2]/div[3]/div[1]/a")
        locator.click()

        #clicando no input de inserir e-mail
        locator = page.locator('//*[@id="identifierId"]')
        locator.click()
        
        time.sleep(1)
        locator.focus()
        locator.wait_for() #Faz o script prosseguir somente quando o elemento aparecer
        locator.type("sistema@montenegrocontabilidade.com.br")
        
        
        #clicando no botão próxima
        locator = page.locator('//*[@id="identifierNext"]/div/button/span')
        locator.click()


        #clicando no input de inserir senha
        locator = page.locator('#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        locator.click()
        time.sleep(1)
        locator.focus()
        locator.wait_for() #Faz o script prosseguir somente quando o elemento aparecer
        locator.type("Monte@labs3094")   


        #clicando no botão próxima
        locator = page.locator('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)')
        locator.click()


        #verificando se existe pasta                    
        #if page.locator('text=2029999'):
        #   print('ok') # revisar
        #else:
        #   print('tem que criar!')


        #clicando na Pasta Teste
        locator = page.locator('.dPmH0b > div:nth-child(1) > div:nth-child(1)')  
        time.sleep(1)
        locator.focus()
        locator.wait_for() #Faz o script prosseguir somente quando o elemento aparecer
        locator.dblclick()

        #clicando na mes01
        locator = page.locator('c-wiz.Zz99o:nth-child(1) > c-wiz:nth-child(2) > div:nth-child(1) > c-wiz:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)')  
        time.sleep(1)
        locator.focus()
        locator.wait_for() #Faz o script prosseguir somente quando o elemento aparecer
        locator.dblclick() 

        #clicando na 01
        locator = page.locator('c-wiz.pmHCK:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)')  
        time.sleep(1)
        locator.focus()
        locator.wait_for() #Faz o script prosseguir somente quando o elemento aparecer
        locator.dblclick() 
        time.sleep(1)

        #verificando a quantidade de arquivos dentro da pasta que terá os arquivos a serem enviados para o drive.
        numberFile = 0
        for path in pathlib.Path(f'/home/tiago.oliveira/Área de Trabalho/teste_upload/').iterdir():
            if path.is_file():
                numberFile += 1

        print('Quantidade de arquivos dentro do diretório: ', numberFile)


        print('*************---------------***************')

        ano = 2020
        for i in range(0, numberFile): #verificando se existe tal arquivo dentro do diretório, retorna true ou false
            file = os.path.exists(rf'/home/tiago.oliveira/Área de Trabalho/teste_upload/{ano}teste.pdf')
            print(file)
            ano = ano + 1

                        
        #Comandos para inserir arquivos dentro da devida pasta.
        anoArquivo = 2020
        for i in range(0, numberFile):
            with page.expect_file_chooser() as fc_info:
                page.locator('button.RTMQvb:nth-child(1) > div:nth-child(2)').click() #clicando em +Novo no canto superior esquerdo do drive.
                page.locator('text=Upload de Arquivo').click()       
            file_chooser = fc_info.value
            file_chooser.set_files(rf'/home/tiago.oliveira/Área de Trabalho/teste_upload/{anoArquivo}teste.pdf')
            anoArquivo = anoArquivo + 1
            time.sleep(1)


        while True: 
            pass


        #browser.close()