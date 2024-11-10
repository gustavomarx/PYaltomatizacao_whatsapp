
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

# Window


# TELAS
def tela_menu():
    layout = [
        #[sg.Input(size=(20,1), key='-DATE-'), sg.CalendarButton("Date", close_when_date_chosen=True, target="-DATE-", location=(200,200), format="%d/%m/%Y")],]
        [sg.Text("Data início"),sg.Input(default_text="", key="-DATA_INI-", size=10), sg.Push()],
        [sg.Text("Data fim"),sg.Input(default_text="", key="-DATA_FIM-", size=10), sg.Push()],
        [sg.Text("Intervalo mensagem"),sg.Input(default_text="", key="-TIME_MSG-", size=5), sg.Push()],
        [sg.Button('Gerar relatório'), sg.Push()],
        [sg.Button('Dados Confirmações'), sg.Push()],
        [sg.Button('Dados Confirmações2'), sg.Push()],
        [sg.Button('Dados Feedback'), sg.Push()],
        [sg.Button('Dados Feedback por profissional'), sg.Push()],
        [sg.Button('Enviar mensagens'), sg.Push()],
        [sg.Button('Limpar Array'), sg.Push()]
        
    ]
    return sg.Window('Menu', layout=layout, finalize=True)