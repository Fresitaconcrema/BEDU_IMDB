from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = "Select alpha2code,alpha3code, country, region, pop from country where trim(alpha2code) !='' order by 1"
cursor.execute(qry)
result = cursor.fetchall()
identifier = 1

now = datetime.now()
timestamp = datetime.timestamp(now)

def add_quote(a):
    return '"{0}"'.format(a)

for x in result:
    # print(identifier, x[0], x[1], x[2], x[3], x[4])
    popu = 0
    if str(x[4]).replace(',', '') == '':
        popu = '0'
    else: popu = str(x[4]).replace(',', '')

    ins = "Insert Into CAT_COUNTRY (id_country, code_alpha2, code_alpha3, country_name, region, population, insert_date) values ("+str(identifier)+",'"+x[0]+"','"+x[1]+"',"+add_quote(x[2])+",'"+str(x[3]).strip()+"',"+popu+",'"+str(now)+"');"
    # cursor.execute(ins)
    identifier = identifier + 1
    print(ins)

cnx.commit()
cursor.close()
cnx.close()
