from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Insert into episodev2(tconst, parenttconst, seasonnumber, episodenumber, insert_date)"+
" Select parenttconst, parenttconst, 0,0, now()"+
" From title_episode as p"+
" Where p.parenttconst not in ('tt13891328','tt4965588','tt1895139','tt4824012','tt6403604','tt6567314','tt7063582','tt7315308','tt9810440')"+
" Group by parenttconst, parenttconst"+
" union all"+
" Select tconst, parenttconst, IFNULL(seasonnumber,-1), IFNULL(episodenumber,-1), now()"+
" from title_episode p"
" Where p.parenttconst not in ('tt13891328','tt4965588','tt1895139','tt4824012','tt6403604','tt6567314','tt7063582','tt7315308','tt9810440')"
)
cursor.execute(qry)

cnx.commit()
cursor.close()
cnx.close()
