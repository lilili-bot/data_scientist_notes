import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from model_lyric import train_model, predict
from model_lyric import text_corpus, labels
import sys
import argparse

parser = argparse.ArgumentParser(description='Predict aritst based of user-input. Currently only works for Weeknd and Queen.')

parser.add_argument('--text',type=str,help='Enter some text, bounded by double-quotes',default="as the mind evolves menaces are born")

args = parser.parse_args()
if args.text:
     user_input = [args.text]  # corpus with 1 document

     m = train_model(text_corpus,labels)
     pred, probs = predict(m, user_input)

     print(f'Based on your input, I predict: "{pred[0]}" with class probabilities {probs[0]}%.')
else:
     print('no text entered')