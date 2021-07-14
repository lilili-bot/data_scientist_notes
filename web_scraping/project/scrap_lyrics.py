import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

def get_link_name(url):
    res = requests.get(url)
    soup_weeknd = BeautifulSoup(res.text,'html.parser')
    soup_component = soup_weeknd.find_all('td',class_="tal qx")
    link = []
    name = []
    for component in soup_component:
        link.append('https://www.lyrics.com'+component.a['href'])
        name.append(component.a.text)
    return (link, name)

def get_lyrics_lines(url_list):
    line=[]
    for url in tqdm(url_list):
        try:
            res = requests.get(url)
            soup_lines= BeautifulSoup(res.text, 'html.parser')
            line.append(soup_lines.find('pre', id='lyric-body-text').text)
        except Exception as e:
            print(e)
            continue
    return line