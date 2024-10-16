import requests
from bs4 import BeautifulSoup
url='https://2023ntcu.ntcu.edu.tw/'
html=requests.get(url)
html.encoding='utf-8'
soup=BeautifulSoup(html.text,'html.parser')
keyword="臺中"
n=0
for text in soup.stripped_strings:
    if keyword in text:
        n+=1
print("找到{}次".format(n))
