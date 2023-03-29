import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Insert into tcast(ncosnt, primaryname, birthyear, deathyear, insert_date)"+
" Select ncosnt, primaryname,"+
" CASE when nb.birthyear is NULL then '9999-01-01' else Concat(nb.birthyear,'-01-01') end as birthyear,"+
" CASE when nb.deathyear is NULL then '9999-12-31' else Concat(nb.deathyear,'-12-31') end as deathyear,"+
" now()"+
" from name_basics as nb")
cursor.execute(qry)

cnx.commit()
cursor.close()
cnx.close()
