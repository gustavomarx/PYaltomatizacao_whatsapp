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
from botcity.core import DesktopBot
from botcity.maestro import *
from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import Window
from minhas_funcoes import *
import telas

sg.theme('DarkBlue4')

tela_menu = telas.tela_menu()

   

while True:
    window, eventos, valores = sg.read_all_windows()

    if window == tela_menu and eventos == sg.WIN_CLOSED:
        break

    if window == tela_menu and eventos == 'Gerar relatório':
        data_ini = valores['-DATA_INI-']
        data_fim = valores['-DATA_FIM-']
        

        print(data_ini, data_fim)
        print("Gerando relatório")
       # logar_avec()
       # gerar_relatorio_clientes(data_ini, data_fim)

    if window == tela_menu and eventos == 'Dados Confirmações':
        print("Pegando os dados")
        pegar_dados_excel_confirmacao()

    if window == tela_menu and eventos == 'Dados Confirmações2':
        print("Pegando os dados2")
        pegar_dados_excel_confirmacao2()    

    if window == tela_menu and eventos == 'Dados Feedback':
        print("Pegando dados feedback")
        pegar_dados_excel_feedback()

    if window == tela_menu and eventos == 'Dados Feedback por profissional':
        print("Pegando dados feedback")
        pegar_dados_excel_feedback_profissional()

    if window == tela_menu and eventos == 'Enviar mensagens':
        intervalo_msg = valores['-TIME_MSG-']
        print("Enviando mensagens")
        enviar_msg_confirmacao(intervalo_msg)

    if window == tela_menu and eventos == 'Limpar Array':
        print("Limpando array")
        limpar_array()
    
   



         
        


    
        


    
    
    


    







    
    
