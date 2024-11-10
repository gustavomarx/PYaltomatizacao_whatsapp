"""
def funcao_ibeptran():

    url_relatorio = "https://ead.ibreptran.com.br/aluno/academico/curso/3194/509/rota/3#conteudo"
    chrome.get(url_relatorio)
    time.sleep(5)


    login = chrome.find_element(By.XPATH, '//*[@id="txt_usuario"]')
    login.send_keys('gustavomarx15@gmail.com')
    
    senha = chrome.find_element(By.XPATH, '//*[@id="txt_senha"]')
    senha.send_keys('03275861093')
    time.sleep(1)

    subdmit = chrome.find_element(By.XPATH, '//*[@id="entrar"]')
    subdmit.click()
    
    
    time.sleep(20)




    while True:
    
        botao_next = chrome.find_element(By.XPATH, '/html/body/div[10]/div/div[5]/div[3]/div/div/div[5]/div[3]')
        botao_next.click()
        time.sleep(10)
"""