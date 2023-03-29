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

df = pd.DataFrame(qry_result, columns = ['tconst', 'primarytitle', 'id_type', 'desc_type', 'averagerating', 'numvotes', 'genres'])

#print(df.head())

#Validate if there is NAN by column
print(df.isna().sum())

#filling Nans
df['genres'] = df['genres'].fillna('No genre')


#print(df.isna().sum())

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
#print(df_rename.isna().sum())

df_rename['average_rating'] = df_rename['average_rating'].astype(float)
df_rename['title'] = df_rename['title'].str.title()


print(f"Mean Votes:  {df_rename['number_of_votes'].mean()}")
print(f"Mean Rating: {df_rename['average_rating'].mean()}")

print(f"Median Votes:  {df_rename['number_of_votes'].median()}")
print(f"Median Rating: {df_rename['average_rating'].median()}")


print(f"Threshold Votes:  {df_rename['number_of_votes'].max() - df_rename['number_of_votes'].min()}")
print(f"Threshold Rating: {df_rename['average_rating'].max() - df_rename['average_rating'].min()}")

print("\n")
print(f'Min Value Votes: {df_rename["number_of_votes"].min()}')
print(f'Percentil Votes 10: {df_rename["number_of_votes"].quantile(0.1)}')
print(f'Percentil Votes 25: {df_rename["number_of_votes"].quantile(0.25)}')
print(f'Percentil Votes 75: {df_rename["number_of_votes"].quantile(0.75)}')
print(f'Percentil Votes 90: {df_rename["number_of_votes"].quantile(0.9)}')
print(f'Maximum Value Votes: {df_rename["number_of_votes"].max()}')
print("\n")
print(f'Min Value Rating: {df_rename["average_rating"].min()}')
print(f'Percentil Rating 10: {df_rename["average_rating"].quantile(0.1)}')
print(f'Percentil Rating 25: {df_rename["average_rating"].quantile(0.25)}')
print(f'Percentil Rating 75: {df_rename["average_rating"].quantile(0.75)}')
print(f'Percentil Rating 90: {df_rename["average_rating"].quantile(0.9)}')
print(f'Maximum Value Rating: {df_rename["average_rating"].max()}')


sns.set(style='whitegrid')

iqr = df_rename['number_of_votes'].quantile(0.75) - df_rename['number_of_votes'].quantile(0.25)
filtro_inferior = df_rename['number_of_votes'] > df_rename['number_of_votes'].quantile(0.25) - (iqr * 1.5)
filtro_superior = df_rename['number_of_votes'] < df_rename['number_of_votes'].quantile(0.75) + (iqr * 1.5)

df_filtrado_v = df_rename[filtro_inferior & filtro_superior]
plt.axvline(df_filtrado_v['number_of_votes'].mean(), c='y')
sns.boxplot(df_filtrado_v['number_of_votes'])
plt.show()

sns.violinplot(data=df_filtrado_v['number_of_votes'])
plt.show()

"""
"""

sns.set(style='whitegrid')

iqr = df_rename['average_rating'].quantile(0.75) - df_rename['average_rating'].quantile(0.25)
filtro_inferior = df_rename['average_rating'] > df_rename['average_rating'].quantile(0.25) - (iqr * 1.5)
filtro_superior = df_rename['average_rating'] < df_rename['average_rating'].quantile(0.75) + (iqr * 1.5)

df_filtrado_a = df_rename[filtro_inferior & filtro_superior]
plt.axvline(df_filtrado_a['average_rating'].mean(), c='y')
sns.boxplot(df_filtrado_a['average_rating'])
plt.show()

sns.violinplot(data=df_filtrado_v['average_rating'])
plt.show()

rango_cut_votes = pd.cut(df_rename['num_of_votes'], 10000)
table_votes = df_rename['num_of_votes'].groupby(rango_cut_votes).count()

rango_cut_rank = pd.cut(df_rename['average_rating'], 100)
table_rank = df_rename['average_rating'].groupby(rango_cut_rank).count()

print(table_votes)


