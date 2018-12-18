print('***************Recommender System for Movies*********************')
import pandas as pd
import random

ratings_data = pd.read_csv("ml-latest-small/ratings.csv")
# print(ratings_data.head())
movie_names = pd.read_csv("ml-latest-small/movies.csv")
a = movie_names['title']
cn = random.randint(0,100)
ab = cn +10
Mo_na = []
for names in a:
    Mo_na.append(names)
while True :
    print(Mo_na[cn])
    cn = cn +1
    if cn == ab:
        break
print('---------------------------------Chose any of the  following Flim name-----------------------------------------')
print('Copy and paste it ')
mov_na = input("Paste here:")
movie_data = pd.merge(ratings_data, movie_names, on='movieId')
# print(movie_data.head())
# print(movie_data.groupby('title')['rating'].mean().head())
# print(movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head())
# print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
# print(ratings_mean_count.head())
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['rating_counts'].hist(bins=50)
plt.title('Rating Distribution')
plt.show()
plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
ratings_mean_count['rating'].hist(bins=50)
plt.title('Rating Distribution Mean')
plt.show()
plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)
plt.title('Combination Of Both')
plt.show()

user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')
# print(user_movie_rating.head())
forrest_gump_ratings = user_movie_rating[mov_na]
# print(forrest_gump_ratings.head() )

movies_like_forest_gump = user_movie_rating.corrwith(forrest_gump_ratings)

corr_forrest_gump = pd.DataFrame(movies_like_forest_gump, columns=['Correlation'])
corr_forrest_gump.dropna(inplace=True)
# print(corr_forrest_gump.head())

# print(corr_forrest_gump.sort_values('Correlation', ascending=False).head(10)  )
corr_forrest_gump = corr_forrest_gump.join(ratings_mean_count['rating_counts'])
# print(corr_forrest_gump.head())
print('----------------------------------------------------Output--------------------------------------------------------------')
print(corr_forrest_gump[corr_forrest_gump ['rating_counts']>50].sort_values('Correlation', ascending=False).head(10))
print('----------------------------------------------------Output--------------------------------------------------------------')
