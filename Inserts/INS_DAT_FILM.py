from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')

cursor = cnx.cursor()
qry = ("Select TB.tconst, CT.id_type, replace(TB.primarytitle,'\"',''), replace(TB.originaltitle,'\"',''), TB.isadult,"+
" CASE when TB.startyear is NULL then '9999-01-01' else Concat(TB.startyear,'-01-01') end as startyear,"+
" CASE when TB.endyear is NULL"+
" then '9999-12-31'"+
" else Concat(TB.endyear,'-01-01')"+
" end as endyear, IFNULL(TB.runtimeminutes, 0)"+
" From title_basics as TB"+
" Inner join CAT_TYPE as CT"+
" On TB.titletype = CT.desc_type")
cursor.execute(qry)
result = cursor.fetchall()
identifier = 1

now = datetime.now()
timestamp = datetime.timestamp(now)

def add_quote(a):
    return '"{0}"'.format(a)

for x in result:
    ins = "Insert Into FILM (tconst, primarytitle, originaltitle, id_type, isadult, startyear, endyear, runtimeminutes, insert_date) values ('"+str(x[0])+"',"+add_quote(str(x[2]))+","+add_quote(str(x[3]))+","+str(x[1])+",'"+str(x[4])+"','"+str(x[5])+"','"+str(x[6])+"',"+str(x[7])+",'"+str(now)+"')"

    try:
        cursor.execute(ins)
    except Exception as e:
        print(ins)
        print(e)

cnx.commit()
cursor.close()
cnx.close()
