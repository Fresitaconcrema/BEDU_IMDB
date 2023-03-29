from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Select R.tconst, R.averagerating, R.numvotes"+
" from title_ratings as R"+
" inner join Film as F"+
" On F.tconst=R.tconst")
cursor.execute(qry)
result = cursor.fetchall()
identifier = 1

now = datetime.now()
timestamp = datetime.timestamp(now)

def add_quote(a):
    return '"{0}"'.format(a)

for x in result:
    ins = "Insert Into RATING (tconst, averagerating, numvotes, insert_date) values ('"+str(x[0])+"',"+str(x[1])+","+str(x[2])+",'"+str(now)+"')"

    try:
        cursor.execute(ins)
    except Exception as e:
        print(ins)
        print(e)

cnx.commit()
cursor.close()
cnx.close()
