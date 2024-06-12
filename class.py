import csv

class Bug:
    def __init__(self, bug_id, erstellungsdatum, schweregrad, status, beschreibung, priorität, gepBehebungsdatum, tatBehebungsdatum, kategorie, auswirkung, reproduktionsrate, sprints, betNutzer):
        self.bug_id = bug_id
        self.erstellungsdatum = erstellungsdatum
        self.schweregrad = schweregrad
        self.status = status
        self.beschreibung = beschreibung
        self.priorität = priorität
        self.gepBehebungsdatum = gepBehebungsdatum
        self.tatBehebungsdatum = tatBehebungsdatum
        self.kategorie = kategorie
        self.auswirkung = auswirkung
        self.reproduktionsrate = reproduktionsrate
        self.sprints = sprints
        self.betNutzer = betNutzer

def read_csv_to_bugs(csv_file_path):
    bugs = []
    with open(csv_file_path ,mode='r', codierung ='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bug = Bug(bug_id['Bug-ID'],erstellungsdatum['Erstellungsdatum'],schweregrad['Schweregrad'],status['Status'], beschreibung['Beschreibung'], priorität['Priorität'], gepBehebungsdatum['Geplantes Behebungsdatum'], tatBehebungsdatum['Tatsächliches Behebungsdatum'], kategorie['Kategorie'], auswirkung['Auswirkung'], reproduktionsrate['Reproduktionsrate'], sprints['Voraussichtliche Sprints bis Behebung (in Wochen)'], betNutzer['Beeinträchtigte Nutzer'])
            bugs.append(bug)
            return bugs


csv_file_path = "Bugreport.csv"
bugs = read_csv_to_bugs(csv_file_path)
for bug in bugs:
    print(vars(bug))
