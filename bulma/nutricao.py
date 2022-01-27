import requests
import json



class alimentacao:
    # gramas =  (gramas input)/100
    dados_alimentos = (requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id=147a6cdf&app_key=151a5a0252dfd4b3f9dbbe47fd7c21dc&ingr={alimento}&nutrition-type=cooking"))
    tabela = gramas * dados_alimentos.json()
    tabela_nutricional = gramas * (tabela['parsed'][0]['food']['nutrients'])
    caloria = gramas * (tabela_nutricional["ENERC_KCAL"])
    proteina = gramas * (tabela_nutricional['PROCNT'])
    gordura = gramas * (tabela_nutricional['FAT'])
    carbo = gramas * (tabela_nutricional['CHOCDF'])





gordura_ideal = 580
proteina_ideal = 65
carbo_ideal = 260
calorias_ideal = 2680

def add_contato():
    con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
    if con.is_connected():
        nutrientes = ['caloria', 'proteina', 'gordura', 'carbo', 'dia']

        for coluna in nutrientes:
            valor = input(print(f'que nome devo colocar na coluna {coluna}??'))
            declaracao = """INSERT INTO `proxetinho`.`alimentacao` (`{}`) VALUES ('{}');""".format(coluna, valor)
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
    if con.is_connected():
        cursor = con.cursor()
        cursor.close()
        con.close()
        print("encerrou a conexao")





