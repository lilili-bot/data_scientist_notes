
import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def read_file(url):
    '''this function is to read file from local path.'''
    with open(url) as f:
        df = pd.read_csv(url, na_values='Nan')
        df.set_index('movieid',inplace=True)
        na_values='Nan'
        
    return df


def pca(p, df):

    return p.fit_transform(df)

    
def cluster(model, k):
    model.fit(m_pca[:,0:k])
    return model.labels_


def fuzz_wuzz(input_title, df):
    #user_input1 = str(input('What movies do you like, please give me one movie name.'))
    fuzz_wuzz_movie = []
    while len(fuzz_wuzz_movie)==0:
        for movie_title in movies['title']:
            if fuzz.partial_ratio(input_title, str(movie_title)) >= 80:
                fuzz_wuzz_movie.append(movie_title)
        if len(fuzz_wuzz_movie)==0:
            input_title = str(input('Opps °_° the movie name does not seem perfect, please try another one.'))
    return fuzz_wuzz_movie

def get_cluster_num(fuzz_wuzz_movie,df):
    
    cluster_num = []
    for movie in fuzz_wuzz_movie:
        cluster_num.append(df.loc[df['title'].isin(fuzz_wuzz_movie)].cluster_no.values[0])
        #recomendation_clustering.append(movies.loc[movies['cluster_no'].isin(cluster_num)].title.values[0])
    return  set(cluster_num) #recomendation_clustering


def recomender_clustering(df,cluster_nummber):
    recommendation_clustering = []
    recommendation_clustering.append(np.random.choice(movies.loc[movies['cluster_no'].isin(cluster_nummber)].title.values, 5))
    return recommendation_clustering


if __name__ == '__main__':
    
    
    url = 'movies_cluster.csv'
    movies = read_file(url)
    df = movies
    input_title = str(input('Enter a cool movie name, which happens to make you happy.'))
    fuzz_wuzz_movie = fuzz_wuzz(input_title,df)
    cluster_nummber = get_cluster_num(fuzz_wuzz_movie, df)
    #recomender_clustering(df,cluster_nummber)
    t = recomender_clustering(df,cluster_nummber)
    print('Here are the movies, try them out:%s'%([i for i in t]))