from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split

df_weeknd = pd.read_csv('../data/df_weeknd.csv')
df_queen = pd.read_csv('../data/df_queen.csv')
corpus_weeknd = list(df_weeknd['song_line'])
corpus_queen = list(df_queen['song_line'])
labels = (['weeknd']*len(corpus_weeknd))+(['queen']*len(corpus_queen))
corpus = list(df_weeknd['song_line'])+list(df_queen['song_line'])

Xtrain, Xtest, ytrain, ytest = train_test_split(corpus, labels, random_state=42)


def train_model(TEXT,LABEL):
    """
Takes in list of songs
trains model on it with labels,
and returns trained model
"""
    print('training model......')    
    con_vec = CountVectorizer(stop_words='english', lowercase=False)
    Tfid = TfidfTransformer()
    lr = LogisticRegression()
    model = make_pipeline(con_vec,Tfid,lr)
    model.fit(TEXT,LABEL)
    return model   

def predict(model, new_text):
    """
    Takes the pre-trained model and predicts new artist.
    """
    prediction = model.predict(new_text)
    #probs = model.predict_proba(new_text)
    return prediction