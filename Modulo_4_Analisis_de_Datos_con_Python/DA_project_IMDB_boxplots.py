"""
Developer: Omar Cr
Date:
Description:
#to get genre group
#1,197,093
"""
import pandas as pd
import mysql.connector as mysqlc
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis


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
df_rename['average_rating'] = df_rename['average_rating'].astype(int)

sns.set(style='white')

iqr = df_rename['number_of_votes'].quantile(0.75) - df_rename['number_of_votes'].quantile(0.25)
filtro_inferior = df_rename['number_of_votes'] > df_rename['number_of_votes'].quantile(0.25) - (iqr * 1.5)
filtro_superior = df_rename['number_of_votes'] < df_rename['number_of_votes'].quantile(0.75) + (iqr * 1.5)
df_filtrado_v = df_rename[filtro_inferior & filtro_superior]

metrics = df_filtrado_v.groupby(level=0)[['number_of_votes', 'average_ranking']]
plt.figure(figsize=(5, 10))
sns.violinplot(data=metrics)
plt.show()


"""
sns.distplot(x=df_filtrado_v['number_of_votes'], kde_kws={'shade': True}, hist=False, axlabel='rating vs votes')
sns.distplot(x=df_filtrado_r['average_rating'],  kde_kws={'shade': True}, hist=False, axlabel='rating vs votes')
plt.legend(['votes', 'ranking'])
#plt.show()


iqr = df_rename['average_rating'].quantile(0.75) - df_rename['average_rating'].quantile(0.25)
filtro_inferior = df_rename['average_rating'] > df_rename['average_rating'].quantile(0.25) - (iqr * 1.5)
filtro_superior = df_rename['average_rating'] < df_rename['average_rating'].quantile(0.75) + (iqr * 1.5)
df_filtrado_r = df_rename[filtro_inferior & filtro_superior]

iqr = df_rename['number_of_votes'].quantile(0.75) - df_rename['number_of_votes'].quantile(0.25)
filtro_inferior = df_rename['number_of_votes'] > df_rename['number_of_votes'].quantile(0.25) - (iqr * 1.5)
filtro_superior = df_rename['number_of_votes'] < df_rename['number_of_votes'].quantile(0.75) + (iqr * 1.5)
df_filtrado_v = df_rename[filtro_inferior & filtro_superior]



counts_r =df_filtrado_r['average_rating'].value_counts()
counts_v =df_filtrado_v['number_of_votes'].value_counts()

#print(counts_r)
#print(counts_v)


as_percentages_r = counts_r * 100 / counts_r.sum()
ax = sns.barplot(as_percentages_r.index, as_percentages_r)
ax.set_title('Conteo de Rating')
ax.set(ylabel='Porcentaje del total')
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)
plt.show()

as_percentages_v = counts_v * 100 / counts_v.sum()
ax = sns.barplot(as_percentages_v.index, as_percentages_v)
ax.set_title('Conteo de Votos')
ax.set(ylabel='Porcentaje del total')
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)
plt.show()
"""
