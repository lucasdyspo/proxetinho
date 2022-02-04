import mysql
from mysql import connector
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import tkinter as tk


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

def formatar_mensagem(mensagem):

    lista = ["'", '[', ']', ',',]
    for i in lista:
        mensagem = mensagem.replace(i, '')
    return palavra

def formatar_numero(palavra):

    lista = [' ', '-', "'", '[', ']', '+', '(', ')', ',', ")"]
    for i in lista:
        palavra = palavra.replace(i, '')
    return palavra

def pesquisar_contato (nome, coluna):
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


def login_insta ():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    time.sleep(3)
    login_button = driver.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[1]/div/label/input')
    login_button.click()
    time.sleep(1)
    usuario = "lucas_dyspo"

    user_element = driver.find_element_by_xpath(
        "//input['username']")
    user_element.clear()
    user_element.send_keys(usuario)
    time.sleep(1)
    senha = '83915684luh'
    password_element = driver.find_element_by_xpath(
        "//input[@name='password']")
    password_element.clear()
    password_element.send_keys(senha)
    time.sleep(1)
    enter = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    enter.click()
    time.sleep(3)
    validar = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    validar.click()

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

def mensagem_insta(insta, mensagem):
    driver = webdriver.Chrome()
    driver.get(f'https://www.instagram.com/"{insta}"/')
    botao = driver.find_element_by_xpath('// *[ @ id = "react-root"] / section / main / div / header / section / div[1] / div[1] / div / div[1] / button / div')
    botao.click()
    campo_mensagem = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    campo_mensagem.click()
    campo_mensagem.clear()
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)

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





