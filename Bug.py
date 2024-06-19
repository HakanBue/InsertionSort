import csv
from datetime import datetime

class Bug:
    def __init__(self, bug_id, creation_date, severity, status, description, priority, pl_resolved_date, resolve_date,
                 category, reproductionrate, sprints, user):
        self.bug_id = bug_id
        self.creation_date = creation_date
        self.severity = severity
        self.status = status
        self.description = description
        self.priority = priority
        self.pl_resolved_date = pl_resolved_date
        self.resolve_date = resolve_date
        self.category = category
        self.reproductionrate = reproductionrate
        self.sprints = sprints
        self.user = user

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

def read_csv_to_bugs(csv_file_path, delimiter=';'):
    bugs_list = []

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        for row in reader:
            reproductionrate = map_values(row['Reproduktionsrate'])
            if isinstance(reproductionrate, str):
                reproductionrate = float(reproductionrate.replace(',', '.'))
            bug = Bug(
                bug_id=row['Bug-ID'],
                creation_date=date_to_epoch(row['Erstellungsdatum']),
                severity=map_values(row['Schweregrad']),
                status=row['Status'],
                description=row['Beschreibung'],
                priority=map_values(row['Priorität']),
                pl_resolved_date=date_to_epoch(row['Geplantes Behebungsdatum']),
                resolve_date=date_to_epoch(row['Tatsächliches Behebungsdatum']) if row['Tatsächliches Behebungsdatum'] else None,
                category=row['Kategorie'],
                reproductionrate=reproductionrate,
                sprints=float(row['Voraussichtliche Sprints bis Behebung (in Wochen)'].replace(',', '.')),
                user=int(row['Beeinträchtigte Nutzer'].replace('.', '').replace(',', ''))
            )
            bugs_list.append(bug)

    return bugs_list