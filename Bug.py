import csv


class Bugs:
    def __init__(self, bug_id, creation_date, severity, status, description, priority, pl_resolved_date, resolve_date,
                 category, reproductionrate, sprints, user):
        self.bug_id = bug_id
        self.creation_date = creation_date
        self.severity = severity
        self.status = status
        self.description = description
        self.priority = priority
        self.pl_resolve_date = pl_resolved_date
        self.resolve_date = resolve_date
        self.category = category
        self.reproductionrate = reproductionrate
        self.sprints = sprints
        self.user = user

# Macht aus Spalten wie z.B Priorität oder Schweregrad Nummern damit man danach sortieren kann
def map_values(value):
    mapping = {
        'Niedrig': 0,
        'Mittel': 1,
        'Hoch': 2,
        'Sehr hoch': 3,
        'Kritisch': 4,
    }
    return mapping.get(value, value)

def read_csv_to_bugs(csv_file_path, delimiter=';'):
    bugs_list = []

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            bug = Bugs(
                bug_id=row['Bug-ID'],
                creation_date=row['Erstellungsdatum'],
                severity=map_values(row['Schweregrad']),
                status=row['Status'],
                description=row['Beschreibung'],
                priority=map_values(row['Priorität']),
                pl_resolved_date=row['Geplantes Behebungsdatum'],
                resolve_date=row['Tatsächliches Behebungsdatum'],
                category=row['Kategorie'],
                reproductionrate=map_values(row['Reproduktionsrate']),
                sprints=row['Voraussichtliche Sprints bis Behebung (in Wochen)'],
                user=row['Beeinträchtigte Nutzer']
            )
            bugs_list.append(bug)

    return bugs_list


# Beispielverwendung
csv_file_path = 'Bugreport.csv'
bugs_list = read_csv_to_bugs(csv_file_path)

# Überprüfung der ersten Einträge
for bug in bugs_list[:5]:
    print(f'{vars(bug)} \n')
