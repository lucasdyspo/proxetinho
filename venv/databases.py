import json

# save in database mysql

def registro_proxetinho(database, columns, values, function=save):

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


"""save in Json"""
def register_json(database, columns, values, function=save):
    database = str(database)
    nome = open(database, 'r+')
    nome.write('eae cefe')
    nome.close()









"""save in SQLite"""
def register_sqlite():
    pass




def __pull_conf_databases():
    pass



def _know_db_function():
    pass



