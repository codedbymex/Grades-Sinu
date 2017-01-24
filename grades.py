from bs4 import BeautifulSoup
import requests

base_url = "https://sinu.utcluj.ro/Note_up/"

UTILIZATOR = "UTILIZATOR"
PAROLA = "PAROLA"
ngrades = "n" #number of grades + 1


payload1 = {'hidSelfSubmit':'default.asp',
            'hidOperation': 'N',  
            'hidUtilizator': 'UTILIZATOR',
            'hidParola': 'PAROLA',
            'txtNume': 'UTILIZATOR',
            'txtParola':'PAROLA'}

session = requests.session()
r1 = session.post(base_url + "default.asp", data=payload1) #1

soup = BeautifulSoup(r1.content, "lxml")

table = soup.find("table", { "class" : "table" })

def noteall():
    for row in table.findAll("tr")[1:ngrades]:
        cells = row.findAll("td")
        if len(cells) > 4:
            note = "\n" + cells[0].text + cells[3].text
            print note
        else:
            return None


