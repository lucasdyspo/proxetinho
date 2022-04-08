import mysql
from mysql import connector
import selenium
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import tkinter as tk
import re
from selenium.webdriver.common.by import By
from instadm import InstaDM
"""numero = "94093][3,4-598795fds"
numero_telefone = re.sub(r"|]|\[|(|)|'|\+|,|\-|[a-z]", '', numero)
print(numero_telefone)
"""

selectors = {
            "accept_cookies": "//button[text()='Allow essential and optional cookies']",
            "accept_cookies_post_login": "//button[text()='Allow all cookies']",
            "home_to_login_button": "//button[text()='Log In']",
            "count_messages": '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div/div',

            "username_field": '//*[@id="loginForm"]/div/div[1]/div/label/input',
            "password_field": '//*[@id="loginForm"]/div/div[2]/div/label/input',
            "button_login": '//*[@id="loginForm"]/div/div[3]/button/div',
            "login_check": '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg',
            "search_user": '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input',
            "select_user": '//div[text()="{}"]',
            "profile_inbox_message": '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div',
            "name": "((//div[@aria-labelledby]/div/span//img[@data-testid='user-avatar'])[1]//..//..//..//div[2]/div[2]/div)[1]",
            "next_button": "//button/*[text()='Next']",
            "textarea": '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea',
            "send": "//button[text()='Send']",
            "chh" : "/html/body/div[5]/div/div/div/div[3]/button[2]"
        }


class instagram:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.user = 'lukinhandrade'
        self.password= "Lucahaha10*"

    def login(self):
        self.driver.get("https://www.instagram.com/")
        #time
        user_element = driver.find_element_by_xpath(selectors["username_field"])
        user_element.clear()
        user_element.send_keys(self.user)
        #time
        password_element = driver.find_element_by_xpath(selectors["password_field"])
        password_element.clear()
        password_element.send_keys(senha)
        #time
        driver.find_element_by_xpath(selectors["button_login"]).click()
        #time
        check = driver.find_element_by_xpath(selectors["chh"])
        check.click()
        #time



    def send_message(self, msg, profile):
        caxa = driver.find_element_by_xpath(selectors["search_user"])
        caxa.send_keys(profile)
        #time
        caxa.send_keys(Keys.ENTER, Keys.ENTER)
        #time
        print("tipo isssssooooooo")
        # time.sleep(3)
        button = driver.find_element_by_xpath(selectors["profile_inbox_message"])
        button.click()
        # time.sleep(7)
        button = driver.find_element_by_xpath(selectors["textarea"])
        # time.sleep(3)
        button.send_keys(msg)
        # time.sleep(3)
        button.send_keys(Keys.ENTER)

    @staticmethod
    def humanizar_mensagem(mensagem):
        palavra = mensagem.split()
        mensagem_editada = []
        termo = ['ruim', "voce", 'obrigado', 'não', 'por favor', 'verdade', 'valeu', 'porque', 'de novo', 'aqui', 'por que',
                 'saudades', 'saudade', 'firmeza', 'mesmo', 'comigo', 'sei la', 'risos', 'gargalhada']

        abreviacao = ['ruim', 'vc', 'obd', 'n', 'pfv', 'vdd', 'vlw', 'pq', 'dnv', 'aq', 'pq', 'sdds', 'sdd', 'fmz',
                      'msm', 'cmg', 'sla', 'kk', 'kkikkskklkksk']
        for i in palavra:

            if palavra.count(i) > 1:
                termo = termo.index(i)
                abr = termo.index(i)
                abr = (abreviacao[abr])
                mensagem_editada.append(abr)

            else:
                mensagem_editada.append(i)

        return mensagem_editada
    """def _formatar_numero(numero):
    
    numero_telefone = re.sub(r"|]|\[|(|)|'|\+|,|\-", '', numero)
   
    return numero_telefone"""
    @staticmethod
    def _pesquisar_contato (nome, coluna):
        con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
        if con.is_connected():
            consulta = (f'select {coluna} from contatos where nome = "{nome}";')
            cursor = con.cursor()
            cursor.execute(consulta)
            linha = cursor.fetchall()
            linha = str(linha)
            linha = formatar_numero(linha)
            return linha
        if con.is_connected():
            cursor = con.cursor()
            con.close()
            cursor.close()
            print("chega")


def mensagem_insta(insta, mensagem):
    button = driver.find_element(By.XPATH(selectors["search_user"]))
    button.click()
    button.send_keys(insta)
    button = driver.find_element(By.XPATH(selectors["profile_inbox_message"]))
    button.click()
    button = driver.find_element(By.XPATH(selectors["textarea"]))
    button.click()
    button.send_keys(mensagem)
    button.send_keys(Keys.ENTER)


def login_insta():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    time.sleep(10)

    usuario = "lukinhandrade"
    user_element = driver.find_element_by_xpath(selectors["username_field"])
    user_element.clear()
    user_element.send_keys(usuario)
    time.sleep(1)
    senha = 'Lucashaha10*'
    password_element = driver.find_element_by_xpath(selectors["password_field"])
    password_element.clear()
    password_element.send_keys(senha)
    time.sleep(1)
    driver.find_element_by_xpath(selectors["button_login"]).click()

    lk = 'naritmo08'
    hg = 'papao'
    time.sleep(10)
    check = driver.find_element_by_xpath(selectors["chh"])
    check.click()
    time.sleep(10)
    caxa = driver.find_element_by_xpath(selectors["search_user"])
    caxa.send_keys(lk)
    time.sleep(4)
    caxa.send_keys(Keys.ENTER, Keys.ENTER)
    time.sleep(10)
    print("tipo isssssooooooo")
    time.sleep(3)
    button = driver.find_element_by_xpath(selectors["profile_inbox_message"])
    button.click()
    time.sleep(7)
    button = driver.find_element_by_xpath(selectors["textarea"])
    time.sleep(3)
    button.send_keys(hg)
    time.sleep(3)
    button.send_keys(Keys.ENTER)


def __get_element__(self, path, timeout=20):
    outcome = False
    try:
        for i in range(timeout):
            if _is_element_present(1, path):
                outcome = True
                break
            else:
                time.sleep(0.3)
                outcome = False
    except excep as e:
        print('the execution error in', path, e)
    if outcome == True:
        keypath = self.driver.find_element_by_xpath(path)
        return keypath








def _is_element_present(self, what, selector="xpath"):
    try:
        self.driver.find_element(by=selector, value=what)
    except NoSuchElementException:
        return False
    return True

def __wait_for_element__(element_tag, tag, timeout=15):
    """Wait till element present. Max 30 seconds"""
    result = False
    for i in range(timeout):
        try:
            if locator == 'NAME' and _self.is_element_present(By.NAME, element_tag):
                result = True
                break
            elif locator == 'XPATH' and _self.is_element_present(By.XPATH, element_tag):
                result = True
                break
            else:
                logging.info(f"Error: Incorrect locator = {tag}")
                time.sleep(0.7)
        except Exception as e:
            logging.error(e)
            print(f"Exception when __wait_for_element__ : {e}")



    # print(q)
    # time.sleep(2)
    # enter.click()
    # time.sleep(10)
    # y = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
    # y.click()
    # l = "sdjasdlkj"
    # t = ('golsdosaopaulo')
    #
    #
    # mensagem_insta(t, l)

def add_contato():
    con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
    if con.is_connected():
        lista_contato = ['nome', 'primeiro_nome', 'outro_nome', 'telefone', 'insta']

        for coluna in lista_contato:
            valor = input(print(f'que nome devo colocar na coluna {coluna}??'))
            declaracao = """INSERT INTO `proxetinho`.`contatos` (`{}`) VALUES ('{}');""".format(coluna, valor)
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
    if con.is_connected():
        cursor = con.cursor()
        cursor.close()
        con.close()
        print("encerrou a conexao")
def mensagem_whats(mensagem, telefone):
    navegador = webdriver.Chrome()
    while len(navegador.find_elements_by_id("side")) < 1:
        texto = urllib.parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
        navegador.get(link)
        while len(navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)
        navegador.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        time.sleep(10)
def check_messages():
    try:
        msg = driver.find_element_by_xpath(selectors["count_messages"])

        if msg:
            numer = driver.find_element_by_xpath(selectors["count_messages"]).text

            print('you have', numer, 'new messages')
    except:
        print('you not have new messages or messages unread')







# selector = '//*[@id="gb"]/div/div[2]/a'
# goo = webdriver.Chrome()
# goo.get('https://www.google.com.br/')
# y = goo.find_element_by_xpath(selector).text
# print((y))
# time.sleep(4)
# goo.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys('só teste mermo', Keys.ENTER)










"""
//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div
//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div

//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg
//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a

//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a 
//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg



"""
# <div class="             qF0y9          Igw0E     IwRSH      eGOV_         _4EzTm ">Entrar</div>

# a = str(<a aria-label="Mensagem direta — Link para 1 nova notificação" class="xWeGp" href="/direct/inbox/" tabindex="0"><svg aria-label="Direct" class="_8-yf5 " color="#262626" fill="#262626" height="24" role="img" viewBox="0 0 24 24" width="24"><line fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="2" x1="22" x2="9.218" y1="3" y2="10.083"></line><polygon fill="none" points="11.698 20.334 22 3.001 2 3.001 9.218 10.084 11.698 20.334 stroke="currentColor" stroke-linejoin="round" stroke-width="2"></polygon></svg><div class="KdEwV"><div class="J_0ip  Vpz-1  TKi86 "><div class="bqXJH">1</div></div></div></a>)
# print(a)
# driver = webdriver.Chrome()
# driver.get("https://www.google.com.br/")
# z = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[2]/a')
# n = z.find_element(By.CLASS_NAME, "gb_1 gb_2 gb_9d gb_9c")
#
# print(z)
# print(n)
# z.click()
# # <a class="gb_1 gb_2 gb_9d gb_9c" href="https://accounts.google.com/ServiceLogin?hl=pt-BR&amp;passive=true&amp;continue=https://www.google.com.br/&amp;ec=GAZAmgQ" target="_top">Fazer login</a>
# #react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(2) > a > div > div > div



