from NMF_recommender_user_input import imputer0, get_R_predict,get_highest_rating, get_reco_pool
from recommender_cos_simi import nor, get_similarity
import numpy as np
import pandas as pd
from fuzzywuzzy import process
from sklearn.impute import KNNImputer
from sklearn.decomposition import NMF
from interface import ratings, user_rating_matrix, user_ratings,update_new_user_to_user_rating_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from interface import ratings, user_rating_matrix, user_ratings, update_new_user_to_user_rating_matrix, movies


def recommend_most_popular(user_ratings, movies, ratings, k=5):
    """
    return k most popular unseen movies for user
    """
    #ratings.drop('movie_title',axis=1,inplace=True)
    df_ratings = ratings.merge(movies['title'], left_on='movieid', right_on = movies.index )
 
    df = df_ratings.groupby('title')[['rating', 'movieid']].mean().sort_values(ascending=False, by='rating')
    df = df.reset_index()

    movie_recommendations = []
    i = 0
    while len(movie_recommendations) < k and i < df.shape[0]:
        title = df.iloc[i,0]
        movie_id = df.iloc[i]['movieid']
        title_id = (title, movie_id)
        i = i+1

        movie_in_user_dict = False 
        for user_movie in user_ratings:
            if user_movie.lower() in title.lower():
                movie_in_user_dict = True   
        if not movie_in_user_dict:
            movie_recommendations.append(title)

    print (movie_recommendations)
recommend_most_popular(user_ratings, movies, ratings, k=5)

def recommend_from_same_cluster(user_rating, movies, k=3):
    """
    Return k most similar movies to the one spicified in the movieID
    
    INPUT
    - user_rating: a dictionary of titles and ratings
    - movies: a data frame with movie titles and cluster number
    - k: number of movies to recommend

    OUTPUT
    - title: the matched movie title (with fuzzy wuzzy) of the best ranked entry
    - movie_titles 
    """
    user_df = pd.DataFrame({'title':list(user_ratings.keys()), 'rating':list(user_ratings.values())})
    favourite_movie = user_df.loc[user_df['rating'] == user_df['rating'].max(), 'title'].sample()
    favourite_movie_title = process.extractOne(favourite_movie.iloc[0], movies['title'])[0]
    cluster = movies.loc[movies['title']==favourite_movie_title, 'cluster_no'].iloc[0]
    movie_titles = list(movies.loc[movies['cluster_no']==cluster, 'title'].sample(n=k)) 

    return favourite_movie_title, movie_titles

#recommend_from_same_cluster(user_ratings, movies, k=3)

def recommender_nmf():

    #user_id,highest_rating,reco_pool,R_true_df

    user_rating_matrix_update, user_seened_movie,new_user_df = update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix)

    imputer = KNNImputer(n_neighbors=2)
    R_true,R_true_df=imputer0(imputer,df=user_rating_matrix_update) 
    
    model = NMF(n_components=2)
    R_predict = get_R_predict(model,R_true,R_true_df)
    
    user_id = R_predict.index[-1]
    highest_rating = get_highest_rating(user_id,R_true_df)

    reco_pool=get_reco_pool(user_id,df=user_rating_matrix_update)

    recomendation_nmf = []
    
    while len(recomendation)<5:
        movie = np.random.choice(R_true_df.T.loc[R_true_df.T[user_id]==highest_rating].index,1)[0]
        if movie in reco_pool:
            recomendation_nmf.append(movie)
        else:
            movie = np.random.choice(R_true_df.T.loc[R_true_df.T[user_id]==highest_rating].index,1)[0]
    return recomendation_nmf

#recommender_nmf()
    

def recommender_sim():

    user_rating_matrix_update, user_seened_movie,new_user_df = update_new_user_to_user_rating_matrix(user_ratings, user_rating_matrix)
    user_rating_matrix_update_scaled=nor(scaler=StandardScaler(), df=user_rating_matrix_update.fillna(0))
    similarity_movie, similarity_user=get_similarity(cosine=cosine_similarity, df=user_rating_matrix_update_scaled) 
    
    recommendation_sim = []
    new_user_t=new_user_df.T
    new_user_t.loc[new_user_t[611]>=4].index.to_list()

    for movie in new_user_t.loc[new_user_t[611]>=4].index.to_list():
        recommendation_sim.append(similarity_movie.loc[(similarity_movie[movie]>=0.7)&(similarity_movie[movie]<1)].index.to_list())
    print (recommendation_sim)


#recommender_sim()

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
    print(recomendation)

    user_rating_matrix_update_scaled=nor(scaler=StandardScaler(), df=user_rating_matrix_update.fillna(0))
    
    similarity_movie, similarity_user=get_similarity(cosine=cosine_similarity, df=user_rating_matrix_update_scaled)
    recommendation_cosin = recommender_sim()
    
    print(recommendation_cosin) """