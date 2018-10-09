import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
title = soup.find_all('h2')

for each in title:
    print (each.text)
