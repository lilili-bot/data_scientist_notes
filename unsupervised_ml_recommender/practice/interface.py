import pandas as pd
import numpy as np
from fuzzywuzzy import process
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.impute import KNNImputer
from sklearn.decomposition import NMF


def read_file(url):
    '''this function is to read file from local path.'''
    with open(url) as f:
        df = pd.read_csv(url, na_values='Nan')
        df.set_index('userid',inplace=True)
        
    return df

user_ratings = {
    'about time': 5,
    'queen': 5,
    'star wars': 5
    }

ratings = read_file('rating_movie_title.csv')
user_rating_matrix = read_file('../data/user_rating_metrix.csv')
movies = pd.read_csv('../data/movies_clusters.csv', index_col='movieid') 


def update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix):
    """
    convert dict of user_ratings to a user_data frame with the same column names as the user_item_matrix
    that can be easily appended to the user_item_matrix
    """            
    
    user_vector = pd.Series(np.nan, index=user_rating_matrix.columns)
    user_seened_movie = []
    for movie in list(user_ratings.keys()): 
        matched_title = process.extractOne(movie, user_vector.index)[0]
        user_vector[matched_title] = user_ratings[movie]
        user_seened_movie.append(process.extractOne(movie, user_vector.index)[0])
    
    new_user_df = user_vector.to_frame().rename(columns={0:np.max(user_rating_matrix.index)+1}).T
    
    return user_rating_matrix.append(new_user_df), user_seened_movie, new_user_df