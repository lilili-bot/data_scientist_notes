import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.decomposition import NMF
from interface import ratings, user_rating_matrix, user_ratings

""" def read_file(url):
    '''this function is to read file from local path.'''
    with open(url) as f:
        df = pd.read_csv(url, na_values='Nan')
        df.set_index('userid',inplace=True)
        
    return df

ratings = read_file('rating_movie_title.csv')
user_rating_matrix = read_file('user_rating_metrix.csv') """


def imputer0(imputer,df):
    R_true = imputer.fit_transform(df)
    R_true_df = pd.DataFrame(R_true, columns=rating_movie.columns, index = rating_movie.index)
    return R_true, R_true_df

def get_R_predict(model,R_true):
    model.fit(R_true)
    Q = model.components_
    P = model.transform(R_true)
    #Q_df = pd.DataFrame(model.components_, columns=user_rating_metrix.columns, index=['feature1', 'feature2'])
    #P_df = pd.DataFrame(model.transform(Rtrue), columns=['feature1', 'feature2'], index= user_rating_metrix.index)
    R = pd.DataFrame(np.dot(P, Q).round(), index=rating_movie.index, columns=rating_movie.columns)
    return R


def get_highest_rating(userid, R_true_df):
    highest_rating = np.random.choice(sorted(R_true_df.loc[R_true_df.index==userid].iloc[0,:])[-5:])   
    return highest_rating


def get_reco_pool(userid, df):
    user_data = df.loc[df.index==userid,:].T
    reco_pool = user_data[user_data[userid].isnull()].index.values
    return reco_pool



def recommender(highest_rating,reco_pool,R_true_df):
    recomendation = []
    while len(recomendation)<5:
        movie = np.random.choice(R_true_df.T.loc[R_true_df.T[userid]==highest_rating].index,1)[0]
        if movie in reco_pool:
            recomendation.append(movie)
        else:
            movie = np.random.choice(R_true_df.T.loc[R_true_df.T[userid]==highest_rating].index,1)[0]
    return recomendation


if __name__ == '__main__':

    imputer = KNNImputer(n_neighbors=2)
    df = user_rating_matrix
    R_true,R_true_df=imputer0(imputer,df) 
    model = NMF(n_components=2)
    r_data = R_true_df
    R_predict = get_R_predict(model,R_true)
    df=rating_movie
    userid=int(input('Please type in your ID'))
    highest_rating = get_highest_rating(userid, R_true_df)
    reco_pool=get_reco_pool(userid,df)
    recomendation = recommender(highest_rating,reco_pool,R_true_df)
    print(recomendation)


