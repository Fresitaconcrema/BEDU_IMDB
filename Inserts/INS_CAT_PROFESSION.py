from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = "Select distinct primaryprofession from name_basics where primaryprofession is not null order by 1"
cursor.execute(qry)
result = cursor.fetchall()
identifier = 1

now = datetime.now()
ss = list()
final = list()

for x in result:
    lx = list(x)
    ss = ss+lx

for i in ss:
    if i.find(",") >= 1:
        lx2 = list(i.split(","))
        final = final+lx2
    else:
        final = final+list(i)
fdupli = list(dict.fromkeys(final))


for x in sorted(fdupli):
    if len(x) > 1:
        ins = "Insert Into CAT_PROFESSION (id_profession, desc_profession, insert_date) values ("+str(identifier)+",'"+str(x)+"','"+str(now)+"')"
        cursor.execute(ins)
        identifier = identifier + 1

cnx.commit()
cursor.close()
cnx.close()