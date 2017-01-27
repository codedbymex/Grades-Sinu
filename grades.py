from bs4 import BeautifulSoup
import requests

base_url = "https://sinu.utcluj.ro/Note_up/"

UTILIZATOR = "UTILIZATOR" # Username here
PAROLA = "PAROLA"         # Password here
ngrades = 10              # Number of grades +1 here

payload = {'hidSelfSubmit':'default.asp',
            'hidOperation': 'N',  
            'hidUtilizator': UTILIZATOR,
            'hidParola': PAROLA,
            'txtNume': UTILIZATOR,
            'txtParola':PAROLA}

r = requests.session().post(base_url + "default.asp", data=payload) 

soup = BeautifulSoup(r.content, "lxml")

table = soup.find("table", { "class" : "table" })

for row in table.findAll("tr")[1:ngrades]:
    cells = row.findAll("td")
    if len(cells) > 4:
        note = "\n" + cells[0].text + cells[3].text
        print note
        


