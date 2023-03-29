import pandas as pd
import mysql.connector as mysqlc

cnx = mysqlc.connect(user='root', password='Bendito0', host='127.0.0.1', database='project_imdb')
cursor = cnx.cursor()

qry = ("Select F.tconst, F.primarytitle, F.id_type, CT.desc_type, "+
  "R.averagerating, R.numvotes, TB.genres "+
"from FILM as F "+
"inner join RATING as R "+
" on F.tconst = R.tconst "+
"inner join CAT_TYPE as CT "+
" on F.id_type = CT.id_type "+
"inner join title_basics as TB "+
" on F.tconst = TB.tconst"
)
cursor.execute(qry)
qry_result = cursor.fetchall()
cursor.close()
cnx.close()

df = pd.DataFrame(qry_result, columns=['tconst', 'primarytitle', 'id_type', 'desc_type', 'averagerating', 'numvotes', 'genres'])

"""
def replace_nans(in_variable):
    count_nas = in_variable.isna().sum()
    if count_nas > 0:
        print(f"{count_nas} is greater than zero")
        in_variable.fillna(0)
        print(in_variable.head())
    return in_variable
"""


if df['genres'].isna().sum() > 0:
    print("There are null values")
    df['genres'] = df['genres'].fillna(0)
    print(df['genres'] .head())


#replace_nans(in_variable)

#df['genres'] = df['genres'].fillna(0)