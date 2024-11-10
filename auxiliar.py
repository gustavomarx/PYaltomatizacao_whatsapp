# 1º PASSO - ENTRAR NO SITE

pyautogui.press("win")
pyautogui.write("internet")
pyautogui.press("enter")
pyautogui.write("https://www.avec.app/")
pyautogui.press("enter")
time.sleep = 3



res = pyautogui.locateCenterOnScreen("entrar_na_plataforma.png")
click_button = pyautogui.center(res)
pyautogui.moveTo(click_button)
pyautogui.click()

res = pyautogui.locateCenterOnScreen("clicar_campo_email.png")
click_button = pyautogui.center(res)
pyautogui.moveTo(click_button)
pyautogui.click()
pyautogui.write("meusciliossaojose@gmail.com")

res = pyautogui.locateCenterOnScreen("buscar_unidade.png")
click_button = pyautogui.center(res)
pyautogui.moveTo(click_button)
pyautogui.click()
time.sleep(3)

res = pyautogui.locateCenterOnScreen("meus_cilios_sao_jose_button.png")
click_button = pyautogui.center(res)
pyautogui.moveTo(click_button)
pyautogui.click()
time.sleep(8)

res = pyautogui.locateCenterOnScreen("campo_senha.png")
click_button = pyautogui.center(res)
pyautogui.moveTo(click_button)
pyautogui.click()
pyautogui.write("96459141@Saojose")

res = pyautogui.locateCenterOnScreen("botao_entrar.png")
click_button = pyautogui.center(res)
pyautogui.moveTo(click_button)
pyautogui.click()
time.sleep(10)


imagem = 'teste.png' #<- seta a imagem como uma variável#

local = pyautogui.locateCenterOnScreen(imagem,confidence=0.8) #<- seta o local onde está a imagem e da uma margem de erro de 50% para caso a imagem apareça um pouco desfocada ou em uma resolução diferente ainda seja possível encontrá-la(use a variável local para conseguir mover o mouse para ela após achada, segue abaixo:)#

pyautogui.moveTo(local) #<- move para o local onde foi achada a imagem (variável local)#
pyautogui.click() #<- da o click onde foi movido pela função acima#