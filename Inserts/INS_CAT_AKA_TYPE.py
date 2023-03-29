from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = "Select distinct types from title_akas where types is not null order by 1"
cursor.execute(qry)
result = cursor.fetchall()
identifier = 1

now = datetime.now()
timestamp = datetime.timestamp(now)

for x in result:
    # print(identifier, x)
    ins = "Insert Into CAT_AKA_TYPE (id_aka_type, desc_aka_type, insert_date) values ("+str(identifier)+","+str(x)[1:-2]+",'"+str(now)+"')"
    cursor.execute(ins)
    identifier = identifier + 1
    # print(ins)

cnx.commit()
cursor.close()
cnx.close()
