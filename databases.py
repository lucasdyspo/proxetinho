import json
import mysql
from mysql import connector
from sqlite3 import *
import sqlite3
from os.path import dirname, realpath, join, isfile



def registro_proxetinho(database, columns, values, function="save"):
    con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
    cursor = con.cursor()

    if con.is_connected():
        for column in columns:
            index = columns.index(column)
            value = values[index]
            declaration = """INSERT INTO `proxetinho`.`{}` ('{}') VALUES ('{}');""".format(database, column, value)
            cursor.execute(declaration)
            con.commit()






    if con.is_connected():
        cursor = con.cursor()
        cursor.close()
        con.close()
        print("encerrou a conexao")


def pesquisar_contato (nome, coluna):
    con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
    if con.is_connected():
        consulta = (f'select {coluna} from contatos where nome = "{nome}";')
        cursor = con.cursor()
        cursor.execute(consulta)
        linha = str(cursor.fetchall())

        return linha
    if con.is_connected():
        cursor = con.cursor()
        con.close()
        cursor.close()
        print("chega")









"""save in Json"""

def register_json(database, columns, values, function='save'):
    new_datas = (dict(zip(columns, values)))
    data_file = "testdatabase.json"
    with open(data_file) as file:
        database_json = json.load(file)
        table = (database_json[0][(((database_json[0].index(database))) + 1)])
        table.append(new_datas)
        with open(data_file, 'w') as file:
            json.dump(database_json, file, indent=2)



"""save in SQLite"""
def register_sqlite(database, columns, values, function="save"):
    database = str(database)
    database_lite = sqlite3.connect(f'{database}.db')

    if database_lite:
        for column in columns:
            index = colunas.index(coluna)
            value = values[index]
            declaration = """INSERT INTO `proxetinho`.`alimentacao` ('{}') VALUES ('{}');""".format(column, value)
            cursor = database_lite.cursor()
            cursor.execute(declaration)
            database_lite.commit()






def __pull_conf_databases():
    pass



def _know_database_function():
    pass



def _create_database_json():
    pass



def _select_database():
    pass




p = ['a', 'b', 'c']
o = [1, 2, 3]
y = dict((zip(p, o)))
print(y)



if '__main__'== __name__:
    print('oi')
