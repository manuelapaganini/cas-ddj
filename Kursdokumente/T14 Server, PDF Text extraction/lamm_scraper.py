from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://daslamm.ch/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
titles = soup.find_all('h2')
lst = []
for title in titles:
   lst.append(title.text)

pd.DataFrame(lst).to_csv("lamm_titel.csv")
