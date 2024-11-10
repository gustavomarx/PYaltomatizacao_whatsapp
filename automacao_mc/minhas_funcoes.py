import pandas as pd #ler arquivo excel
from selenium import webdriver #navegador
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #Achar os elementos
from selenium.webdriver.common.keys import Keys #Para digitar no teclado na web
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pg
from openpyxl import Workbook
from openpyxl import load_workbook
from datetime import datetime
import webbrowser
from botcity.core import DesktopBot
from botcity.maestro import *
import os
from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import Window

#Funções

#service = Service(ChromeDriverManager().install())
#chrome = webdriver.Chrome(service=service)

array_texto_celular = []

#Abre o chrome e loga no AVEC
"""def logar_avec():
    url_avec = "https://admin.avec.beauty/meus-cilios-sao-jose/admin"
    email_meuscilios = "meusciliossaojose@gmail.com"
    senha_meuscilios = "96459141@Saojose"

    print('entrei logar avec')

        # /html/body/div[6]/div[1]/div/div[2]/form/button

    

    #chrome.get(url_avec)
    
    time.sleep(5)

    elemento_campo_email = chrome.find_element(By.XPATH, "//*[@id='formEmail']")
    elemento_campo_senha = chrome.find_element(By.XPATH, "//*[@id='formSenha']")
    elemento_botao_entrar = chrome.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/form/button")
    
    elemento_campo_email.send_keys(email_meuscilios)
    elemento_campo_senha.send_keys(senha_meuscilios)
    elemento_botao_entrar.click()

    time.sleep(5)


   # chrome.find_elementss(By.XPATH, "")
    

"""

"""
def gerar_relatorio_clientes(data_ini, data_fim):

    data_confirmacao_inicio = data_ini
    data_confirmacao_fim = data_fim
        
    url_relatorio = "https://admin.avec.beauty/admin/relatorio/0051"
    chrome.get(url_relatorio)

    elemento_data_inicio = chrome.find_element(By.XPATH, "//*[@id='variaveis']/div[1]/span[1]/div/input")
    elemento_data_fim = chrome.find_element(By.XPATH, "//*[@id='variaveis']/div[1]/span[2]/div/input")
    elemento_botao_buscar = chrome.find_element(By.XPATH, "//*[@id='variaveis']/div[1]/span[5]/a")   

    elemento_data_inicio.click()
    elemento_data_inicio.send_keys(data_confirmacao_inicio)
    time.sleep(2)
    elemento_data_fim.click()
    elemento_data_fim.send_keys(data_confirmacao_fim)
    time.sleep(2)
    elemento_botao_buscar.click()
    time.sleep(2)

    pg.press('tab')
    time.sleep(2)

    pg.press('tab')
    time.sleep(2)

    pg.press('tab')
    time.sleep(2)

    pg.press('tab')
    time.sleep(2)

    pg.press('enter')
    time.sleep(5)
    
"""

def pegar_dados_excel_confirmacao():
    string  = r"C:\Users\gusta\Downloads"
    directory_path = r"C:\Users\gusta\Downloads"

    array_celular = []
    contador_array = 0

    most_recent_file = None
    most_recent_time = 0

    # iterate over the files in the directory using os.scandir
    for entry in os.scandir(directory_path):
        if entry.is_file():
            # get the modification time of the file using entry.stat().st_mtime_ns
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                # update the most recent file and its modification time
                most_recent_file = entry.name
                most_recent_time = mod_time
              
    novo_diretorio = r'C:\Users\gusta\Downloads\\' + most_recent_file

    df = pd.read_excel(novo_diretorio)
    
    for index, row in df.iterrows():
        # print("Index " + str(index) + " Cliente: " + row["Cliente"])
        nome_cliente = row["Cliente"]
        data_reserva = row["Data Reserva"]
        hora_reserva = row["Hora"]
        celular_cliente = int(row["Celular"])#[:-2]
        serviço_cliente = row["Serviço"]
        
        status_reserva = row["Status"]

        celular_cliente = str(celular_cliente)
    
        

        if(status_reserva == 'Agendado'):

                        
            nome_cliente = nome_cliente.split()[0]

            string_inteira = 'https://web.whatsapp.com/send?phone='+celular_cliente+'&text=Oiee%20maravilhosa%2C%20t%C3%A1%20pertinho%20de%20voc%C3%AA%20vir%20ter%20o%20seu%20momento%20de%20autocuidado%20conosco%20%E2%9D%A4%EF%B8%8F%0D%0ASeu%20servi%C3%A7o%20foi%20agendado%20com%20sucesso%20para%20dia%20%2A'+data_reserva+'%20%C3%A0s%20'+hora_reserva+'%2A%20no%20Studio%20Meus%20C%C3%ADlios%20S%C3%A3o%20Jos%C3%A9.%0D%0A%0D%0A%2A'+nome_cliente+'%2A%2C%20queremos%20confirmar%20sua%20presen%C3%A7a%20que%20%C3%A9%20muuuuito%20importante%20para%20a%20profissional%20que%20conta%20com%20sua%20presen%C3%A7a.%20%2APosso%20confirmar%3F%2A%20'
                
            #print(string_inteira)

            array_texto_celular.append(string_inteira)
            print(string_inteira)
            



    tam = len(array_texto_celular)    
    sg.popup_auto_close('Carregados:  '+ str(tam))    

def pegar_dados_excel_confirmacao2():
    string  = r"C:\Users\gusta\Downloads"
    directory_path = r"C:\Users\gusta\Downloads"

    array_celular = []
    contador_array = 0

    most_recent_file = None
    most_recent_time = 0

    # iterate over the files in the directory using os.scandir
    for entry in os.scandir(directory_path):
        if entry.is_file():
            # get the modification time of the file using entry.stat().st_mtime_ns
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                # update the most recent file and its modification time
                most_recent_file = entry.name
                most_recent_time = mod_time
              
    novo_diretorio = r'C:\Users\gusta\Downloads\\' + most_recent_file

    df = pd.read_excel(novo_diretorio)
    
    for index, row in df.iterrows():
        # print("Index " + str(index) + " Cliente: " + row["Cliente"])
        nome_cliente = row["Cliente"]
        data_reserva = row["Data Reserva"]
        hora_reserva = row["Hora"]
        celular_cliente = str(row["Celular"])[:-2]
        serviço_cliente = row["Serviço"]
        
        status_reserva = row["Status"]

    


        if(status_reserva == 'Agendado'):

                        
            nome_cliente = nome_cliente.split()[0]

            string_inteira = 'https://web.whatsapp.com/send?phone='+celular_cliente+'&text=Oiee%20maravilhosa%2C%20t%C3%A1%20pertinho%20de%20voc%C3%AA%20vir%20ter%20o%20seu%20momento%20de%20autocuidado%20conosco%20%E2%9D%A4%EF%B8%8F%0D%0ASeu%20servi%C3%A7o%20foi%20agendado%20com%20sucesso%20para%20dia%20%2A'+data_reserva+'%20%C3%A0s%20'+hora_reserva+'%2A%20no%20Studio%20Meus%20C%C3%ADlios%20S%C3%A3o%20Jos%C3%A9.%0D%0A%0D%0A%2A'+nome_cliente+'%2A%2C%20queremos%20confirmar%20sua%20presen%C3%A7a%20que%20%C3%A9%20muuuuito%20importante%20para%20a%20profissional%20que%20conta%20com%20sua%20presen%C3%A7a.%20%2APosso%20confirmar%3F%2A%20'
                
            #print(string_inteira)

            array_texto_celular.append(string_inteira)
            print(string_inteira)
            


def pegar_dados_excel_feedback():
    string  = r"C:\Users\gusta\Downloads"
    directory_path = r"C:\Users\gusta\Downloads"

    most_recent_file = None
    most_recent_time = 0

    # iterate over the files in the directory using os.scandir
    for entry in os.scandir(directory_path):
        if entry.is_file():
            # get the modification time of the file using entry.stat().st_mtime_ns
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                # update the most recent file and its modification time
                most_recent_file = entry.name
                most_recent_time = mod_time
              
    novo_diretorio = r'C:\Users\gusta\Downloads\\' + most_recent_file

    df = pd.read_excel(novo_diretorio)
    
    for index, row in df.iterrows():
        # print("Index " + str(index) + " Cliente: " + row["Cliente"])
        nome_cliente = row["Cliente"]
        data_reserva = row["Data Reserva"]
        hora_reserva = row["Hora"]
        celular_cliente = str(row["Celular"])
        serviço_cliente = row["Serviço"]
        status_reserva = row["Status"]


        if(status_reserva == 'Pago' or status_reserva == 'Finalizado' ):
            
            nome_cliente = nome_cliente.split()[0]

            string_inteira = 'https://web.whatsapp.com/send?phone='+celular_cliente+'&text=Oiie%20'+nome_cliente+'!%20Como%20voc%C3%AA%20est%C3%A1?%20%F0%9F%8C%B8%0A%0ARecentemente,%20voc%C3%AA%20esteve%20aqui%20conosco%20para%20podermos%20cuidar%20um%20pouquinho%20e%20dar%20o%20nosso%20melhor%20para%20proporcionar%20uma%20experi%C3%AAncia%20incr%C3%ADvel%20no%20seu%20momento%20de%20autocuidado.%20%F0%9F%A5%B0%F0%9F%A5%B9%0A%0APara%20continuarmos%20em%20evolu%C3%A7%C3%A3o%20e%20melhorarmos%20no%20atendimento%20e%20nos%20servi%C3%A7os,%20por%20favor,%20existe%20algo%20que%20possamos%20melhorar%20para%20tornar%20sua%20experi%C3%AAncia%20cada%20vez%20melhor?%0A%0A%20Fique%20a%20vontade%20para%20escrever%20ou%20enviar%C2%A0um%C2%A0audio%C2%A0%F0%9F%A5%B0%F0%9F%98%8D%0A'
            #https://web.whatsapp.com/send?phone=5551993721863&text=Oiie%20xxxxxx!%20Como%20voc%C3%AA%20est%C3%A1?%20%F0%9F%8C%B8%0A%0ARecentemente,%20voc%C3%AA%20esteve%20aqui%20conosco%20para%20podermos%20cuidar%20um%20pouquinho%20e%20dar%20o%20nosso%20melhor%20para%20proporcionar%20uma%20experi%C3%AAncia%20incr%C3%ADvel%20no%20seu%20momento%20de%20autocuidado.%20%F0%9F%A5%B0%F0%9F%A5%B9%0A%0APara%20continuarmos%20em%20evolu%C3%A7%C3%A3o%20e%20melhorarmos%20no%20atendimento%20e%20nos%20servi%C3%A7os.%20Por%20favor,%20existe%20algo%20que%20possamos%20melhorar%20para%20tornar%20sua%20experi%C3%AAncia%20cada%20vez%20melhor?%0A%0A%20Fique%20a%20vontade%20para%20escrever%20ou%20enviar%C2%A0um%C2%A0audio%C2%A0%F0%9F%A5%B0%F0%9F%98%8D%0A
            #print(string_inteira)

            array_texto_celular.append(string_inteira)
            print(string_inteira)

def pegar_dados_excel_feedback_profissional():
    string  = r"C:\Users\gusta\Downloads"
    directory_path = r"C:\Users\gusta\Downloads"

    most_recent_file = None
    most_recent_time = 0

    # iterate over the files in the directory using os.scandir
    for entry in os.scandir(directory_path):
        if entry.is_file():
            # get the modification time of the file using entry.stat().st_mtime_ns
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                # update the most recent file and its modification time
                most_recent_file = entry.name
                most_recent_time = mod_time
              
    novo_diretorio = r'C:\Users\gusta\Downloads\\' + most_recent_file

    df = pd.read_excel(novo_diretorio)
    
    for index, row in df.iterrows():
        # print("Index " + str(index) + " Cliente: " + row["Cliente"])
        nome_cliente = row["Cliente"]
        data_reserva = row["Data Reserva"]
        hora_reserva = row["Hora"]
        celular_cliente = str(row["Celular"])
        serviço_cliente = row["Serviço"]
        status_reserva = row["Status"]
        profissional = row["Profissional"]


        if(status_reserva == 'Pago' or status_reserva == 'Finalizado' ):
            
            nome_cliente = nome_cliente.split()[0]
            profissional = profissional.split()[0]

            if(profissional == "Maria" or profissional == "Yasmim" or profissional == "Eduarda" or profissional == "Madu" or profissional == "Gabriela"):
                string_inteira = 'https://web.whatsapp.com/send?phone='+celular_cliente+'&text=*Studio%20Meus%20C%C3%ADlios%20-%20S%C3%A3o%20Jos%C3%A9:*%0A%0A*Oi%20maravilhosa!%20Tudo%20bem?%20Espero%20que%20sim*%20%E2%9C%8C%F0%9F%8F%BC%F0%9F%92%9C%0A%0APassando%20para%20saber%20como%20est%C3%A3o%20seus%20c%C3%ADlios%20e%20como%20foi%20seu%20atendimento%20com%20a%20*Lash%C2%A0'+profissional+'*?'
            
            if(profissional == "Brenda" or profissional == "Luizy"):
                string_inteira = 'https://web.whatsapp.com/send?phone='+celular_cliente+'&text=*Studio%20Meus%20C%C3%ADlios%20-%20S%C3%A3o%20Jos%C3%A9:*%0A%0A*Oi%20maravilhosa!%20Tudo%20bem?%20Espero%20que%20sim*%20%E2%9C%8C%F0%9F%8F%BC%F0%9F%92%9C%0A%0APassando%20para%20saber%20como%20est%C3%A3o%20suas%20unhas%20e%20como%20foi%20seu%20atendimento%20com%20a%20*Nails%C2%A0'+profissional+'*?'

            array_texto_celular.append(string_inteira)
            print(string_inteira)

    
def enviar_msg_confirmacao(intervalo_msg):
    
    tam = len(array_texto_celular)
    cont = 0
    intervalo_msg = int(intervalo_msg)

    for texto in array_texto_celular:
        cont += 1
        print(texto)
        webbrowser.open(texto)
        time.sleep(intervalo_msg)
        pg.keyDown('ENTER')
        time.sleep(10)
        sg.popup_auto_close('Em processamento '+ str(cont) + '/'+ str(tam))

def limpar_array():
    array_texto_celular.clear()
        
