from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Insert into brdg_film_gnr(tconst, id_genre, insert_date)"+
" Select T.tconst, CT.id_genre, now()"+
" from title_basics T"+
" inner join cat_genre CT"+
"  On  substring_index(T.genres,',',1)=CT.desc_genre"+
" union "+
" Select T.tconst, CT.id_genre, now()"+
" from title_basics T"+
" inner join cat_genre CT"+
" On  substring_index(substring_index(genres,',',-2),',',1)=CT.desc_genre"+
" union"+
" Select T.tconst, CT.id_genre, now()"+
" from title_basics T"+
" inner join cat_genre CT"+
" On  substring_index(substring_index(genres,',',-1),',',1)=CT.desc_genre"
)
cursor.execute(qry)

cnx.commit()
cursor.close()
cnx.close()
