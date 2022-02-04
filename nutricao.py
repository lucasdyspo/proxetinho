import requests
import json

alimentacao_objetivo = {"gordura_ideal" : 580,
"proteina_ideal" : 65,
"carbo_ideal" : 260,
"calorias_ideal" : 2680}


class alimentacao:
    def pesquisa_alimento (self, alimento):
        nutrientes_alimento = []
        # gramas =  (gramas input)/100
        dados_alimentos = (requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id=147a6cdf&app_key=151a5a0252dfd4b3f9dbbe47fd7c21dc&ingr={alimento}&nutrition-type=cooking"))
        tabela = dados_alimentos.json()
        tabela_nutricional = gramas * (tabela['parsed'][0]['food']['nutrients'])
        nutrientes_alimento.append(gramas * (tabela_nutricional["ENERC_KCAL"]))
        nutrientes_alimento.append(gramas * (tabela_nutricional['PROCNT']))
        nutrientes_alimento.append(gramas * (tabela_nutricional['FAT']))
        nutrientes_alimento.append(gramas * (tabela_nutricional['CHOCDF']))
        nutrientes = ['caloria', 'proteina', 'gordura', 'carbo', 'dia']
        return (nutrientes, nutrientes_alimento)



def registro_proxetinho():
    con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
    if con.is_connected():
        # colunas =
        # valores =

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





