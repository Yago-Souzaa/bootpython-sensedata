from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)



class geral:
    def  abrirSite(link):
        navegador.get(link)

    def click(aux):
        navegador.find_element('xpath',aux).click()

    def fazerlogin(usuario,senha):
        #digitar fazer login 
        navegador.find_element('xpath','/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input').send_keys(usuario)
        navegador.find_element('xpath','/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input').send_keys(senha)

    def entrega(nome,sobrenome,cep):
        navegador.find_element('xpath','/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input').send_keys(nome)
        navegador.find_element('xpath','/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(sobrenome)
        navegador.find_element('xpath','/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input').send_keys(cep) 

    def fechar():
        navegador.close()   