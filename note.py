from bs4 import BeautifulSoup
from tabulate import tabulate
import requests

base_url = "https://sinu.utcluj.ro/Note_up/"

UTILIZATOR = "UTILIZATOR" # Username here
PAROLA = "PAROLA"         # Password here
data = []

payload = {'hidSelfSubmit':'default.asp',
            'hidOperation': 'N',  
            'hidUtilizator': UTILIZATOR,
            'hidParola': PAROLA,
            'txtNume': UTILIZATOR,
            'txtParola':PAROLA}

r1 = requests.session().post(base_url + "default.asp", data=payload) 
soup = BeautifulSoup(r1.content, "lxml")
table = soup.find('table', attrs={'class':'table'})
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
     
print tabulate(data, tablefmt="grid")
