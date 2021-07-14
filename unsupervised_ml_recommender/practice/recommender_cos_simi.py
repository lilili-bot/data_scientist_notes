import pandas as pd
import numpy as np
from fuzzywuzzy import process
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from interface import ratings, user_rating_matrix, user_ratings, update_new_user_to_user_rating_matrix

""" def read_file(url):
    '''this function is to read file from local path.'''
    with open(url) as f:
        df = pd.read_csv(url, na_values='Nan')
        df.set_index('userid',inplace=True)
        
    return df
 """




""" def update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix):

    user_vector = pd.Series(np.nan, index=user_rating_matrix.columns)
    user_seened_movie = []
    for movie in list(user_rating.keys()): 
        matched_title = process.extractOne(movie, user_vector.index)[0]
        user_vector[matched_title] = user_rating[movie]
        user_seened_movie.append(process.extractOne(movie, user_vector.index)[0])
    
    new_user_df = user_vector.to_frame().rename(columns={0:np.max(user_rating_matrix.index)+1}).T
    
    return user_rating_matrix.append(new_user_df), user_seened_movie, new_user_df """


def nor(scaler, df):
    df_scale = pd.DataFrame(scaler.fit_transform(df) , columns= df.columns, index= df.index)
    return df_scale 


def get_similarity(cosine, df):
    similarity_movie=pd.DataFrame(cosine_similarity(df.T),columns= df.columns, index=df.columns)
    similarity_user =pd.DataFrame (cosine_similarity(df),columns=df.index,  index= df.index)
    return similarity_movie,similarity_user.sort_values(similarity_user.columns[-1],axis=0, ascending=False)


def recommender_sim():
    
    recommendations = []
    new_user_t=new_user_df.T
    new_user_t.loc[new_user_t[611]>=4].index.to_list()

    for movie in new_user_t.loc[new_user_t[611]>=4].index.to_list():
        recommendations.append(similarity_movie.loc[(similarity_movie[movie]>=0.7)&(similarity_movie[movie]<1)].index.to_list())
    return recommendations

""" if __name__ == '__main__':
    

    
    user_rating_matrix_update, user_seened_movie,new_user_df = update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix)
    user_rating_matrix_update_scaled=nor(scaler=StandardScaler(), df=user_rating_matrix_update.fillna(0))
    
    similarity_movie, similarity_user=get_similarity(cosine=cosine_similarity, df=user_rating_matrix_update_scaled)
    recommendation_cosin = recommender_sim()
    
    print(recommendation_cosin) """