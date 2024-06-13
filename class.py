import csv


class Bugs:
    def __init__(self, bug_id, creation_date, severity, status, discription, priority, pl_resolved_date, resolve_date, kategory, reproductionrate, sprints, user):
        self.bug_id = bug_id
        self.creation_date = creation_date
        self.severity = severity
        self.status = status
        self.discription = discription
        self.priority = priority
        self.pl_resolve_date = pl_resolved_date
        self.resolve_date = resolve_date
        self.kategory = kategory
        self.reproductionrate = reproductionrate
        self.sprints = sprints
        self.user = user


def read_csv_to_bugs(csv_file_path, delimiter=';'):
    bugs_list = []

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            bug = Bugs(
                bug_id=row['Bug-ID'],
                creation_date=row['Erstellungsdatum'],
                severity=row['Schweregrad'],
                status=row['Status'],
                discription=row['Beschreibung'],
                priority=row['Priorität'],
                pl_resolved_date=row['Geplantes Behebungsdatum'],
                resolve_date=row['Tatsächliches Behebungsdatum'],
                kategory=row['Kategorie'],
                reproductionrate=row['Reproduktionsrate'],
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
    print(vars(bug))
