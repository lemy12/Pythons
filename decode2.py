import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
r_html = r.text

art_ids = [x for x in range(223,315)]

soup = BeautifulSoup(r_html, 'html.parser')
title = soup.find_all(attrs={"data-reactid": art_ids})

for each in title:
    print (each.text)


"""223-314"""
