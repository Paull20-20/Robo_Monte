#from os import link
from operator import truediv
from xml.sax.xmlreader import Locator
from playwright.sync_api import sync_playwright
import time
#from bs4 import BeautifulSoup
import pathlib
#import pandas as pd
#import json
#from urllib.error import URLError


class Robo:

    with sync_playwright() as p:

        
        browser = p.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.add_init_script("""
        navigator.p = false
        Object.defineProperty (navigator, 'webdriver', {
        get: () => false
        })
        """
        )


        page.goto("https://drive.google.com/drive/folders/1zpJPcb4HuS5J5AHSMpMTF1sZLrFA0TFN")
        
        #page.goto("https://accounts.google.com/signin/v2/identifier?hl=pt-BR&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fclient%3Dubuntu%26hs%3DX8L%26channel%3Dfs%26q%3Dhow%2Bto%2Bcompile%2Bpython%2Bin%2Bwindows%26spell%3D1%26sa%3DX%26ved%3D2ahUKEwiPxsSPgvb4AhWrpZUCHX17B4kQBSgAegQIARA4%26biw%3D1472%26bih%3D742%26dpr%3D1.3&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

        #Espera o elemento ficar visivel
        def waitElement(self, el):
            status = True
            while status:
                el = self.page.locator(el)
                if el != None and el.is_visible():
                    status = False

        
        print(page.title())


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

        #clicando na pasta
        locator = page.locator('.dPmH0b > div:nth-child(1) > div:nth-child(1)')
        time.sleep(1)
        locator.focus()
        locator.wait_for() #Faz o script prosseguir somente quando o elemento aparecer
        locator.dblclick()


        with page.expect_file_chooser() as fc_info:
            page.locator('button.RTMQvb:nth-child(1) > div:nth-child(2)').click()
            page.locator('text=Upload de Arquivo').click()
        file_chooser = fc_info.value
        file_chooser.set_files(r'/home/tiago.oliveira/Área de Trabalho/teste_upload/2027teste.pdf')


        while True: 
            pass


        #browser.close()