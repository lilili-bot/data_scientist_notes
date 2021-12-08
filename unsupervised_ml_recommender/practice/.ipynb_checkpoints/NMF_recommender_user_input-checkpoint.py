import numpy as np
import pandas as pd
from fuzzywuzzy import process
from sklearn.impute import KNNImputer
from sklearn.decomposition import NMF
from interface import ratings, user_rating_matrix, user_ratings,update_new_user_to_user_rating_matrix

""" def read_file(url):
    '''this function is to read file from local path.'''
    with open(url) as f:
        df = pd.read_csv(url, na_values='Nan')
        df.set_index('userid',inplace=True)
    return df """


""" def update_new_user_to_user_rating_matrix(user_rating, user_rating_matrix):           
    
    user_vector = pd.Series(np.nan, index=user_rating_matrix.columns)
    for movie in list(user_rating.keys()): 
        matched_title = process.extractOne(movie, user_vector.index)[0]
        user_vector[matched_title] = user_rating[movie]
    new_user_df = user_vector.to_frame().rename(columns={0:'new_user'}).T
    return user_rating_matrix.append(new_user_df) """

""" def update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix):         
    
    user_vector = pd.Series(np.nan, index=user_rating_matrix.columns)
    user_seened_movie = []
    for movie in list(user_rating.keys()): 
        matched_title = process.extractOne(movie, user_vector.index)[0]
        user_vector[matched_title] = user_rating[movie]
        user_seened_movie.append(process.extractOne(movie, user_vector.index)[0])
    
    new_user_df = user_vector.to_frame().rename(columns={0:np.max(user_rating_matrix.index)+1}).T
    
    return user_rating_matrix.append(new_user_df), user_seened_movie, new_user_df """


def imputer0(imputer,df):
    R_true = imputer.fit_transform(df)
    R_true_df = pd.DataFrame(R_true, columns=df.columns, index = df.index)
    R_true_df.to_csv('imputed_rating_user_matrix.csv')
    return R_true, R_true_df

def get_R_predict(model,R_true,R_true_df):
    model.fit(R_true)
    Q = model.components_
    P = model.transform(R_true)
    R = pd.DataFrame(np.dot(P, Q).round(), index=R_true_df.index, columns=R_true_df.columns)
    return R

def get_highest_rating(user_id, R_true_df):
    
    highest_rating = np.random.choice(sorted(R_true_df.loc[R_true_df.index==user_id].iloc[0,:])[-5:])   
    return highest_rating

def get_reco_pool(user_id, df):
    
    user_data = df.loc[df.index==user_id,:].T
    reco_pool = user_data[user_data[user_id].isnull()].index.values
    return reco_pool

def recommender_nmf(user_id,highest_rating,reco_pool,R_true_df):
    recomendation = []
    
    while len(recomendation)<5:
        movie = np.random.choice(R_true_df.T.loc[R_true_df.T[user_id]==highest_rating].index,1)[0]
        if movie in reco_pool:
            recomendation.append(movie)
        else:
            movie = np.random.choice(R_true_df.T.loc[R_true_df.T[user_id]==highest_rating].index,1)[0]
    return recomendation


""" if __name__ == '__main__':
    
    user_rating_matrix_update, user_seened_movie,new_user_df = update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix)

    #user_rating_matrix_update = update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix)

    imputer = KNNImputer(n_neighbors=2)
    R_true,R_true_df=imputer0(imputer,df=user_rating_matrix_update) 
    
    
    model = NMF(n_components=2)
    R_predict = get_R_predict(model,R_true,R_true_df)
    
    user_id = R_predict.index[-1]
    highest_rating = get_highest_rating(user_id,R_true_df)

    reco_pool=get_reco_pool(user_id,df=user_rating_matrix_update)
    
    recomendation = recommender_nmf(user_id,highest_rating,reco_pool,R_true_df)
    print(recomendation) """