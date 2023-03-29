from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Insert into principal(tconst, ordering, nconst, id_category, desc_job, characters, insert_date)"+
" Select tp.tconst, tp.ordering, tp.nconst,"+
" cc.id_category,"+
" tp.job,"+
" tp.characters,"+
" now()"+
" from title_principal as tp"+
" inner join cat_category as cc"+
" On cc.desc_category = tp.category")
cursor.execute(qry)

cnx.commit()
cursor.close()
cnx.close()
