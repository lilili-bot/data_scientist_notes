import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer, CountVectorizer
from sklearn. naive_bayes import GaussianNB, MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

df_weeknd = pd.read_csv('../data/df_weeknd.csv')
df_queen = pd.read_csv('../data/df_queen.csv')
corpus_weeknd = list(df_weeknd['song_line'])
corpus_queen = list(df_queen['song_line'])

labels = (['weeknd']*len(corpus_weeknd))+(['queen']*len(corpus_queen))
corpus = list(df_weeknd['song_line'])+list(df_queen['song_line'])

Xtrain, Xtest, ytrain, ytest = train_test_split(corpus, labels, random_state=42)

len(Xtrain), len(Xtest), len(ytrain), len(ytest)

# build model
def mul_model(text,label):
    """
    Takes in list of songs
    trains model on it with labels,
    and returns trained model
    """
    print('Training model...\n')
    cv = CountVectorizer(stop_words='english', ngram_range=(2,3))
    tf = TfidfTransformer()
    nb = MultinomialNB(alpha=1)
    model = make_pipeline(cv,tf,nb)
    model.fit(text, label)
    return model
    
def mul_predict(m, test):
    """
    Takes the pre-trained pipeline model and predicts new artist.
    """
    predict = m.predict(test)
    probs = m.predict_proba(test).round(2)
    return predict