import csv
from datetime import datetime

class Bug:
    def __init__(self, bug_id, creation_date, severity, status, description, priority, pl_resolved_date, resolve_date,
                 category, effect, reproductionrate, sprints, user):
        self.bug_id = bug_id
        self.creation_date = creation_date
        self.severity = severity
        self.status = status
        self.description = description
        self.priority = priority
        self.pl_resolved_date = pl_resolved_date
        self.resolve_date = resolve_date
        self.category = category
        self.effect = effect
        self.reproductionrate = reproductionrate
        self.sprints = sprints
        self.user = user

# Convert date to epoch time
def date_to_epoch(date_str):
    dt = datetime.strptime(date_str, '%d.%m.%Y')
    return int(dt.timestamp())

# Converts epoch time to date
def epoch_to_date(epoch_time):
    if epoch_time is None:
        return None
    dt = datetime.fromtimestamp(epoch_time)
    return dt.strftime('%d.%m.%Y')

# Mappt die Attribute zu Zahlen, damit wir sie sortieren können
def map_values(value):
    mapping = {
        'Niedrig': 0,
        'Mittel': 1,
        'Hoch': 2,
        'Sehr hoch': 3,
        'Kritisch': 4,
        'Sicherheit': 5,
        'Backend': 6,
        'UI': 7
    }
    return mapping.get(value, value)

# Die selbe Funktion in reverse, damit wir im frontend wieder die richtigen Werte anzeigen
def reverse_map_values(value):
    reverse_mapping = {
        0: 'Niedrig',
        1: 'Mittel',
        2: 'Hoch',
        3: 'Sehr hoch',
        4: 'Kritisch',
        5: 'Sicherheit',
        6: 'Backend',
        7: 'UI'
    }
    return reverse_mapping.get(value, value)


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
                effect=map_values(row['Auswirkung']),
                reproductionrate=reproductionrate,
                sprints=float(row['Voraussichtliche Sprints bis Behebung (in Wochen)'].replace(',', '.')),
                user=int(row['Beeinträchtigte Nutzer'].replace('.', '').replace(',', ''))
            )
            bugs_list.append(bug)

    return bugs_list