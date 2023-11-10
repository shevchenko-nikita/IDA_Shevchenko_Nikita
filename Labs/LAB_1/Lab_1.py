import pandas as pd
import seaborn as sns
import matplotlib
def get_top(_lst, _gender, _age, _movies_df):
    top_movies = _lst[(_lst['Age'] == _age) & (_lst['Gender'] == _gender)]
    rating_count = top_movies.groupby(['MovieID'])['Rating'].count()
    rating_count.name = 'Rating Count'
    top_movies = pd.merge(top_movies, rating_count, on='MovieID')
    top_movies = top_movies[top_movies['Rating Count'] >= 20]
    top_movies = top_movies.groupby('MovieID')['Rating'].mean()
    top_movies = pd.merge(_movies_df, top_movies, on='MovieID')
    top_movies = top_movies.sort_values(by=['Rating'], ascending=[False])
    return top_movies
def print_top_ten(_lst, _gender, _age, _movies_df):
    top_movies = get_top(_lst, _gender, _age, _movies_df).head(10)
    print(top_movies.to_string())

def show_top_ten(_lst, _gender, _age, _movies_df):
    top_movies = get_top(_lst, _gender, _age, _movies_df).head(10)
    sns.barplot(data=top_movies, x="MovieID", y="Rating")

encoding = 'ISO-8859-1'

movies_df = pd.read_csv('LAB_1/movies.dat', sep='::', names=['MovieID', 'Title', 'Genres'], encoding=encoding, engine='python')
ratings_df = pd.read_csv('LAB_1/ratings.dat', sep='::', names=['UserID', 'MovieID', 'Rating', 'Timestamp'], encoding=encoding, engine='python')
users_df = pd.read_csv('LAB_1/users.dat', sep='::', names=['UserID', 'Gender', 'Age', 'Occupation', 'ZIP_code'], encoding=encoding, engine='python')

merged_df = pd.merge(movies_df, ratings_df, on='MovieID')
merged_df = pd.merge(merged_df, users_df, on='UserID')

print_top_ten(merged_df, 'F', 1, movies_df)

#show_top_ten(merged_df, 'M', 1, movies_df)

