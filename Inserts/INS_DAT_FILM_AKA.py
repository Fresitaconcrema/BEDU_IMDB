from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Select ta.titleid, ta.ordering, ta.title,"+
       " IFNULL(cc.id_country,-1) id_country,"+
       " IFNULL(cl.id_language,-1) id_language,"+
       " IFNULL(cat.id_aka_type,-1) id_aka_type,"+
       " IFNULL(ta.attributes,'NULL') attributes,"+
       " IFNULL(ta.isoriginaltitle,'NULL') isoriginaltitle"+
" from title_akas as ta"+
" inner join cat_country as cc"+
"  on ta.region = cc.code_alpha2"+
" left outer join cat_language as cl"+
"  on ta.language = cl.desc_language"+
" left outer join cat_aka_type as cat"+
"  on ta.types = cat.desc_aka_type"+
" Where id_country>0")
cursor.execute(qry)
result = cursor.fetchall()
identifier = 1

now = datetime.now()
timestamp = datetime.timestamp(now)

def add_quote(a):
    return '"{0}"'.format(a)

for x in result:
    if str(x[6]) == 'NULL':
        attr = 'NULL'
    else:
        attr = "'"+str(x[6])+"'"

    ins = ("Insert Into FILM_AKA (tconst, ordering, title_name, id_country, id_language, id_aka_type, attributes, isoriginaltitle, insert_date) "+
           "values ('"+str(x[0])+"',"+str(x[1])+","+add_quote(str(x[2]))+","+str(x[3])+","+str(x[4])+","+str(x[5])+","+
           attr+",'"+str(x[7])+"','"+str(now)+"')")
    try:
        cursor.execute(ins)
    except:
        pass

cnx.commit()
cursor.close()
cnx.close()
