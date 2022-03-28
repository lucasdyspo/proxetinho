import requests
import json




class nutricao:

    fat_ideal = 580
    protein_ideal = 65
    carbo_ideal = 260
    caloria_ideal = 2680


    @classmethod
    def modify_meta_nutrients(cls, period, fat = fat_ideal, protein = protein_ideal, carbo = carbo_ideal, caloria = caloria_ideal):
        pass


class alimentacao(nutricao):
    def __init__(self, food, gramas):
        self. gramas = gramas / 100
        dados_alimentos = (requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id=147a6cdf&app_key=151a5a0252dfd4b3f9dbbe47fd7c21dc&ingr={food}&nutrition-type=cooking"))
        tabela = dados_alimentos.json()
        tabela_nutricional = gramas * (tabela['parsed'][0]['food']['nutrients'])
        self.calorie = (gramas * (tabela_nutricional["ENERC_KCAL"]))
        self.protein = (gramas * (tabela_nutricional['PROCNT']))
        self.fat = (gramas * (tabela_nutricional['FAT']))
        self.carbohydrate = (gramas * (tabela_nutricional['CHOCDF']))


def registro_proxetinho():
    con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
    if con.is_connected():


        for coluna in colunas:
            index = colunas.index(coluna)
            valor = valores[index]
            declaracao = """INSERT INTO `proxetinho`.`alimentacao` (`{}`) VALUES ('{}');""".format(coluna, valor)
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
    if con.is_connected():
        cursor = con.cursor()
        cursor.close()
        con.close()
        print("encerrou a conexao")





