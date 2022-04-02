import requests
import json
import datetime




class nutrition:

    period = 442
    today = datetime.date.today()
    fat_ideal = 580
    protein_ideal = 65
    carbo_ideal = 260
    caloria_ideal = 2680



    @classmethod
    def modify_meta_nutrients(cls, period, fat = fat_ideal, protein = protein_ideal, carbo = carbo_ideal, caloria = caloria_ideal):
        "alter the objectives and you values, for a period time that said input"
        input('what news values')
        pass


class meal(nutrition):
    aliments_of_meal = []
    nutrients_of_meal = []

    def remove_aliment(self, *aliments):
        global aliments_of_meal

        for ali_m in aliments_of_meal:
            for ali in aliments:
                if ali == ali_m.name:
                    aliments_of_meal.remove(ali_m)
        return aliments_of_meal




    def __calc_nut_meal(self):
        global nutrients_of_meal
        calorie = 0
        fat = 0
        protein = 0
        carbo = 0
        for aliment in aliments_of_meal:
            calorie = calorie + aliment.calorie
            protein = protein + aliment.protein
            fat = fat + aliment.fat
            carbo = carbo + aliment.carbohydrate
        nutrients_of_meal.append([calorie, protein, fat, carbo])
        return nutrients_of_meal



    def register_meal(self, meal = "meal"):
        "register in sql or other database the aliments and nutients of meal"

        pass



class aliment_api(nutrition):
    def __init__(self, food, gramas):
        self.gramas = gramas / 100
        dados_alimentos = (requests.get(f"https://api.edamam.com/api/food-database/v2/parser?app_id=147a6cdf&app_key=151a5a0252dfd4b3f9dbbe47fd7c21dc&ingr={food}&nutrition-type=cooking"))
        tabela = dados_alimentos.json()
        self.name = tabela['text']
        print(self.name)
        print(tabela)
        tabela_nutricional = (tabela['parsed'][0]['food']['nutrients'])
        print(tabela_nutricional)
        self.calorie = (self.gramas * (tabela_nutricional["ENERC_KCAL"]))
        self.protein = (self.gramas * (tabela_nutricional['PROCNT']))
        self.fat = (self.gramas * (tabela_nutricional['FAT']))
        self.carbohydrate = (self.gramas * (tabela_nutricional['CHOCDF']))
        print(self.calorie)

    def search_food(self, fat=False, calorie=False, carbo=False, protein=False, grams=100):
        if fat:
            print(f' the food has', + self.fat + 'g of fat in '+ grams + 'g')
        elif calorie:
            print(f' the food has', + self.calorie + 'Kcal of calories in '+ grams + 'g')
        elif carbo:
            print(f' the food has', + self.carbohydrate + 'g of carbohydrate in '+ grams + 'g')
        elif protein:
            print(f' the food has', + self.protein + 'g of protein in '+ grams + 'g')










aliment_api('rice', 100)