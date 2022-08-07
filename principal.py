#import os
from funcoesSite import geral

#entrar no site
geral.abrirSite("https://www.saucedemo.com/")

#fazer login
geral.fazerlogin("standard_user","secret_sauce")
geral.click('/html/body/div/div/div[2]/div[1]/div[1]/div/form/input')

#ordenar
geral.click('/html/body/div/div/div/div[1]/div[2]/div[2]/span/select')
geral.click('//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]')

#colocar produtos no carrinho
geral.click('//*[@id="add-to-cart-sauce-labs-onesie"]')
geral.click('/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button')

#entrar no carrinho/concluindo compra
geral.click('/html/body/div/div/div/div[1]/div[1]/div[3]/a')
geral.click('/html/body/div/div/div/div[2]/div/div[2]/button[2]')

#digitando informações para entrega
geral.entrega("yago","souza","37130-000")
geral.click('/html/body/div/div/div/div[2]/div/form/div[2]/input')
geral.click('/html/body/div/div/div/div[2]/div/div[2]/div[8]/button[2]')

#os.system("PAUSE")
#fechar
geral.fechar()


