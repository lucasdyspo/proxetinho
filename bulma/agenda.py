import mysql
from mysql import connector
import datetime
import time

MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro"
    , "outubro", "novembro", "dezembro"]
DAYS = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]
MONTH_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
DAY_EXTENTIONS = ["st", "nd", "th", "rd"]


def tempo_termino(minutagem_input):
    tempo_termino = minutagem_input + int(input(print('tempo pra terminar esse role???')))
    return tempo_termino


po = time.localtime()
hora_atual = po.tm_hour
minuto_atual = po.tm_min

def registrar_agenda(minutagem_agenda, dia_agenda, mes_agenda, titulo_agenda):
    con = mysql.connector.connect(host='localhost', database='proxetinho', user='root', password='Lucashaha10*')
    if con.is_connected():
        print("pao")
        dados = minutagem_agenda + ',\'' + dia_agenda + '\',' + mes_agenda + ',' + titulo_agenda + ');'
        declaracao = """INSERT INTO agenda_horario
                                    (minutagem, dia, mes, titulo) 
                                VALUES ("""
        sql = declaracao + dados
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()
        print("encerrou a conexao")


#text
#verifica o dia de hoje
def get_date(text):
    today = datetime.date.today()
    text = text.lower()
    if text.count("hoje") > 0:
        return today

#verifica amanhã
    if text.count("amanhã") > 0:
        day = today.day + 1
        if day > MONTH_DAYS.get(today.month):
            day -= MONTH_DAYS.get(today.month)
        month = today.month
        year = today.year
        if month > 11:
            month -= 11
            year += 1
        return  print(today.month)
        #return datetime.date(month=month, day=day, year=year)

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
            print(month)
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:
        year = year + 1

    if month == -1 and day != -1:
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("próximo") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:
        return datetime.date(month=month, day=day, year=year)



