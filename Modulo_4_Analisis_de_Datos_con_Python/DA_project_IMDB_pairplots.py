import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
df['genres'] = df['genres'].fillna('No genre')

column_name_mapping = {
'tconst' : 'id_movie',
'primarytitle' : 'title',
'id_type' : 'id_type',
'desc_type' : 'description_type',
'averagerating' : 'average_rating',
'numvotes' : 'number_of_votes',
'genres' : 'genre'
}

df_rename = df.rename(columns=column_name_mapping)
df_rename['average_rating'] = df_rename['average_rating'].astype(float)


new_df = df_rename.drop(columns=['id_movie','title', 'id_type'])

print('Sample')
print(new_df.head())

plt.figure(figsize=(8, 6))
sns.heatmap(new_df.corr(), annot=True, linewidths=.5)
#plt.show()

sns.pairplot(new_df.head())
plt.show()