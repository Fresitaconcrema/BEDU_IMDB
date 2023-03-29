from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = "Select distinct genres from title_basics where genres is not null order by 1"
cursor.execute(qry)
result = cursor.fetchall()
identifier = 1

now = datetime.now()
ss = list()
final = list()

for x in result:
    lx = list(x)
    ss = ss+lx
#print(ss, type(ss))

for i in ss:
    if i.find(",") >= 1:
        lx2 = list(i.split(","))
        final = final+lx2
    else:
        final = final+list(i)
fdupli = list(dict.fromkeys(final))


for x in sorted(fdupli):
    if len(x) > 1:
        ins = "Insert Into CAT_GENRE (id_genre, desc_genre, insert_date) values ("+str(identifier)+",'"+str(x)+"','"+str(now)+"')"
        cursor.execute(ins)
        identifier = identifier + 1


cnx.commit()
cursor.close()
cnx.close()


# y= ['Mystery,Short']
# y.append(['Mystery,Short'][1:-1])
# print(y)