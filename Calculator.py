import re

import requests
from bs4 import BeautifulSoup


def clean_html(raw_html):
    clean_br = re.compile('<br/>')
    raw_html = re.sub(clean_br, ' ', raw_html)
    clean_regular = re.compile('<.*?>')
    clean_text = re.sub(clean_regular, '', raw_html)
    return clean_text


request = requests.get("https://abitur.sstu.ru/vpo/direction/2021/214/a/o/b")

soup = BeautifulSoup(request.content, features="html.parser")
table = soup.find("table")

rows = []

head_row = None

for index, row in enumerate(table.findAll("tr")):
    if index > 0:
        rows.append(row)
    else:
        head_row = row

clean_headers = []

if head_row is not None:
    for header in head_row.findAll('th'):
        clean_th = clean_html(str(header))
        clean_headers.append(clean_th.strip())
