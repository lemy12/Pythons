import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
title = soup.find_all('h2')

open_file = open("nytimes.txt", "w")
for each in title:
    open_file.write(each.text + "\n")
open_file.close()
