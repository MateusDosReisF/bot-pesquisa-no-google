from googlesearch import search
from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
import requests
import re

perg = input('desejas pesquisar ?  (s/sim)')

while True:
    if perg.lower() == 's' or 'sim':
        pg = input('o que deseja pesquisar ?')
        for url in search(pg, stop=20):
            print('--')
            print(url)
            print('--')
            pesquisar = ('https://www.google.com.br/search?source=hp&ei=2dfGXoO9NYKy5OUPlLW0-AI&q=')

            webbrowser.open_new(url)
            html = urlopen(url)
            bs = BeautifulSoup(html, 'lxml')




            print('----------TITULO DA PESQUISA----------\n')
            print(bs.select('title\n'))

            print('-----------TEXTO DA PESQUISA--------------\n')
            print(bs.select('p\n'))

            html = requests.get(url)
            # res=html.text
