import requests
from bs4 import BeautifulSoup
import lxml

base = "http://www.parlinfo.fr.ch"
base_url = "http://www.parlinfo.fr.ch/de/mitglieder/behoerdenmitglieder/"
link_form = "/de/mitglieder/behoerdenmitglieder/welcome.php?personen_id="

members = {}

def scrape_member(name, url):
    #open member page
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    #find address, add to list
    address = soup.find("div", {"id": "addressPartContent"})
    members[name] = address.get_text(" ")

def scrape_full_page(url):
    #open page
    r = requests.get(url)
    if r.status_code == 200:
        # find all members
        soup = BeautifulSoup(r.content, 'lxml')
        for a in soup.find_all('a', href=True):
            if link_form in a['href']:
                scrape_member(a.get_text(), base + a['href'])

scrape_full_page(base_url)

for address in members.keys():
    print(members[address] + " {" + address + "}")