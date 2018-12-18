print('Recommender System for Movies')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# pass in column names for each CSV and read them using pandas.
# Column names available in the readme file

#Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,
 encoding='latin-1')

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
 encoding='latin-1')

#Reading items file:
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,
 encoding='latin-1')
#-----------Data-----------
print('----------Users-------------')
print (users.shape)
print(users.head())
print('----------Ratings-------------')
print (ratings.shape)
print(ratings.head())
print('----------Items-------------')
print (items.shape)
print(items.head())
#-----------Finding the rating Distribution-----------
plt.rc("font", size=15)
ratings.rating.value_counts(sort=False).plot(kind='bar')
plt.title('Rating Distribution\n')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.savefig('system2.png', bbox_inches='tight')
#plt.show()
#---------------Recommendations based on correlations-------
average_rating = pd.DataFrame(ratings.groupby('movie_id')['rating'].mean())
average_rating['ratingCount'] = pd.DataFrame(ratings.groupby('movie_id')['rating'].count())
#print(average_rating.sort_values('ratingCount', ascending=False).head())
#--------------Excluding user with less than 200 rating and books with <100--------------
ratings_pivot = ratings.pivot(index='user_id', columns='movie_id',values='rating')
print(ratings_pivot.shape)
#print(ratings_pivot.head(5))
#-------------Testing-----------------
bones_ratings = ratings_pivot[5]
similar_to_bones = ratings_pivot.corrwith(bones_ratings)
corr_bones = pd.DataFrame(similar_to_bones, columns=['pearsonR'])
corr_bones.dropna(inplace=True)
corr_summary = corr_bones.join(average_rating['ratingCount'])
corr_summary = corr_summary.join(items ['movie title'])
corr_summary = corr_summary.join(items ['movie id'])
fin = corr_summary.sort_values('pearsonR', ascending=False).head(10)
print(fin,end=' ')
#--------------final-----------------------------




