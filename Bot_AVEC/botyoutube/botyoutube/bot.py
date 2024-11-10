from botcity.core import DesktopBot
from datetime import datetime

# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Opens the BotCity website.

        #LOGANDO NO AVEC
        self.execute(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk")
        self.wait(5000)
        self.paste("https://admin.avec.beauty/meus-cilios-sao-jose/admin/?email=meusciliossaojose@gmail.com")
        self.enter()

        self.wait(5000)

        if not self.find( "achar_email", matching=0.97, waiting_time=10000):
            self.not_found("achar_email")
        self.click()

        self.tab()

        self.paste("96459141@Saojose")

        if not self.find( "entrar_login", matching=0.97, waiting_time=10000):
            self.not_found("entrar_login")
        self.click()


        self.wait(5000)

        # GERANDO RELATÓRIO CLIENTES


        if not self.find( "alterar_url", matching=0.97, waiting_time=10000):
            self.not_found("alterar_url")
        self.click()


        self.paste("https://admin.avec.beauty/admin/relatorio/0051")
        self.enter()

        self.wait(5000)



        cont=1
        while cont!=17:
            self.tab()
            cont += 1

        dataHoje = datetime.now()
        dataHoje = dataHoje.strftime("%d/%m/%Y")
        self.paste(dataHoje)

        self.wait(1000)
        
        if not self.find( "clicar_buscar", matching=0.97, waiting_time=10000):
            self.not_found("clicar_buscar")
        self.click()

        self.wait(1000)
        
        if not self.find( "gerar_excel", matching=0.97, waiting_time=10000):
            self.not_found("gerar_excel")
        self.click()
        
        if not self.find( "mover_arquivo", matching=0.97, waiting_time=10000):
            self.not_found("mover_arquivo")
        self.move()
        
        self.wait(1000)
        
        if not self.find( "abrir_local", matching=0.97, waiting_time=10000):
            self.not_found("abrir_local")
        self.click()
        
        self.wait(5000)

        if not self.find("mover_para", matching=0.97, waiting_time=10000):
            self.not_found("mover_para")
        self.click()

        if not self.find("escolher_local", matching=0.97, waiting_time=10000):
            self.not_found("escolher_local")
        self.click()

        cont = 0
        while cont != 3:
            self.tab()
            cont += 1

        self.paste(r"C:\Users\gusta\OneDrive\Área de Trabalho\Studio Meus Cílios\8. Histórico Relatórios\Relatórios clientes diários")
        self.enter()



        
        
        
        
        

        

      
        




        
        
        
        
        
        
        
        
        


















    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()







