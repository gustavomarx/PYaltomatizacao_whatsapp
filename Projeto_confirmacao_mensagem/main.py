import pandas as pd  # ler arquivo excel
from selenium import webdriver  # navegador
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Achar os elementos
from selenium.webdriver.common.keys import Keys  # Para digitar no teclado na web
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pg
import webbrowser
import os
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkBlue4')


# Funções


# Abre o chrome e loga no AVEC
def abrir_chrome():
    url_avec = "https://admin.avec.beauty/meus-cilios-sao-jose/admin"
    email_meuscilios = "meusciliossaojose@gmail.com"
    senha_meuscilios = "96459141@Saojose"

    # /html/body/div[6]/div[1]/div/div[2]/form/button

    chrome.get(url_avec)

    time.sleep(3)

    elemento_campo_email = chrome.find_element(By.XPATH, "//*[@id='formEmail']")
    elemento_campo_senha = chrome.find_element(By.XPATH, "//*[@id='formSenha']")
    elemento_botao_entrar = chrome.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/form/button")

    elemento_campo_email.send_keys(email_meuscilios)
    elemento_campo_senha.send_keys(senha_meuscilios)
    elemento_botao_entrar.click()

    time.sleep(5)


# chrome.find_element(By.XPATH, "")


def gerar_relatorio_clientes():
    data_confirmacao = "09/04/2024"

    url_relatorio = "https://admin.avec.beauty/admin/relatorio/0051"
    chrome.get(url_relatorio)

    elemento_data_inicio = chrome.find_element(By.XPATH, "//*[@id='variaveis']/div[1]/span[1]/div/input")
    elemento_data_fim = chrome.find_element(By.XPATH, "//*[@id='variaveis']/div[1]/span[2]/div/input")
    elemento_botao_buscar = chrome.find_element(By.XPATH, "//*[@id='variaveis']/div[1]/span[5]/a")
    elemento_botao_excel = chrome.find_element(By.XPATH, "//*[@id='tableFilter_wrapper']/div[3]/a[2]/span")

    elemento_data_inicio.click()
    elemento_data_inicio.send_keys(data_confirmacao)
    time.sleep(2)
    elemento_data_fim.click()
    elemento_data_fim.send_keys(data_confirmacao)
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


def pegar_dados_excel():
    string = r"C:\Users\gusta\Downloads"
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

        nome_cliente = nome_cliente.split()[0]

        string_inteira = 'https://web.whatsapp.com/send?phone=' + celular_cliente + '&text=Oiee%20maravilhosa%2C%20t%C3%A1%20pertinho%20de%20voc%C3%AA%20vir%20ter%20o%20seu%20momento%20de%20autocuidado%20conosco%20%E2%9D%A4%EF%B8%8F%0D%0ASeu%20servi%C3%A7o%20foi%20agendado%20com%20sucesso%20para%20dia%20%2A' + data_reserva + '%20%C3%A0s%20' + hora_reserva + '%2A%20no%20Studio%20Meus%20C%C3%ADlios%20S%C3%A3o%20Jos%C3%A9.%0D%0A%0D%0A%2A' + nome_cliente + '%2A%2C%20queremos%20confirmar%20sua%20presen%C3%A7a%20que%20%C3%A9%20muuuuito%20importante%20para%20a%20profissional%20que%20conta%20com%20sua%20presen%C3%A7a.%20%2APosso%20confirmar%3F%2A%20'

        # print(string_inteira)

        array_texto_celular.append(string_inteira)


def agendar_mensagem():
    for texto in array_texto_celular:
        print(texto)
        webbrowser.open(texto)
        time.sleep(30)
        pg.keyDown('ENTER')
        time.sleep(10)


service = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

array_texto_celular = []


# abrir_chrome()
# gerar_relatorio_clientes()
# pegar_dados_excel()
# agendar_mensagem()


def tela_menu():
    layout = [
        [sg.Push(), sg.Button('Gerar relatório'), sg.Push()],
        [sg.Push(), sg.Button('Pegar dados Excel'), sg.Push()],
        [sg.Push(), sg.Button('Enviar mensagens'), sg.Push()]
    ]
    return sg.Window('Menu', layout=layout, finalize=True)


tela_menu = tela_menu()

while True:
    window, eventos, valores = sg.read_all_windows()

    if window == tela_menu and eventos == sg.WIN_CLOSED:
        break

    if window == tela_menu and eventos == 'Gerar relatório':
        print("Gerando relatório")
        abrir_chrome()
        gerar_relatorio_clientes()

    if window == tela_menu and eventos == 'Pegar dados Excel':
        print("Pegando os dados")
        pegar_dados_excel()

    if window == tela_menu and eventos == 'Enviar mensagens':
        print("Enviando mensagens")
        agendar_mensagem()



















