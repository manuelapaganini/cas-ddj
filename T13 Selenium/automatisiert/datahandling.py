# alles zusammen

from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import re
from tqdm import tqdm

final_list = []
lst =os.listdir('pages')

def extract_bakeries(elem):
    rows = elem.find_all('tr', {'class': "ng-scope"})
    b_list = []
    for row in rows:
        name = row.find("div").text
        u_id = row.find_all('div')[2].text
        place = row.find_all('div')[4].text
        canton = row.find_all('div')[5].text
        link = row.find('div').find_next('div').find('a')['href']

        mini_dict = {
            "Unternehmen": name,
            "ID": u_id,
            "Ort": place,
            "Kanton": canton}
        b_list.append(mini_dict)
    return b_list


for filename in lst:
    file = open('pages/' + filename, 'r')
    text = file.read()
    h = BeautifulSoup(text, 'html.parser')

    final_list = final_list + extract_bakeries(h)

df= pd.DataFrame(final_list)

df.to_csv("alle_baeckereien.csv", index=False)
