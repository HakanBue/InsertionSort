import csv
from datetime import datetime
from sorter import insertionSort

# Convert date to epoch time
def date_to_epoch(date_str):
    dt = datetime.strptime(date_str, '%d.%m.%Y')
    return int(dt.timestamp())

# Map values for severity, priority, and reproduction rate
def map_values(value):
    mapping = {
        'Niedrig': 0,
        'Mittel': 1,
        'Hoch': 2,
        'Sehr hoch': 3,
        'Kritisch': 4,
    }
    return mapping.get(value, value)

    # Warum eigene Klasse implementieren, wenn es Dictionaries gibt?

def read_csv_to_bugs(csv_file_path, delimiter=';'):
    bugs_list = []

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            reproductionrate = map_values(row['Reproduktionsrate'])
            if isinstance(reproductionrate, str):
                reproductionrate = float(reproductionrate.replace(',', '.'))
            bug = {
                "bug_id":row['Bug-ID'],
                "creation_date":date_to_epoch(row['Erstellungsdatum']),
                "severity":map_values(row['Schweregrad']),
                "status":row['Status'],
                "description":row['Beschreibung'],
                "priority":map_values(row['Priorität']),
                "pl_resolved_date":date_to_epoch(row['Geplantes Behebungsdatum']),
                "resolve_date":date_to_epoch(row['Tatsächliches Behebungsdatum']) if row['Tatsächliches Behebungsdatum'] else None,
                "category":row['Kategorie'],
                "reproductionrate":reproductionrate,
                "sprints":float(row['Voraussichtliche Sprints bis Behebung (in Wochen)'].replace(',', '.')),
                "user":int(row['Beeinträchtigte Nutzer'].replace('.', '').replace(',', ''))
            }
            bugs_list.append(bug)

    return bugs_list

# Example usage
csv_file_path = 'Bugreport_fixed_csv.csv'
bugs_list = read_csv_to_bugs(csv_file_path)

test1 = input("Erste Wahl: ")
test2 = input("Zweite Wahl: ")

#Insertion Sort Funktion mit den 2 zu sortierenden Feldern aufrufen --- Mit der GUI Verknüpfen
insertionSort(bugs_list, test1, test2)

# Check the first entries
for bug in bugs_list:
    print(bug[test1], bug[test2])
