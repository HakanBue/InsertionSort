from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from sorter import insertion_sort, translate_attributes
from Bug import read_csv_to_bugs, epoch_to_date, reverse_map_values

app = Flask(__name__)
CORS(app)

# Liste der Attribute der Bugs-Klasse
bug_attributes = [
    'Bug-ID', 'Erstellungsdatum', 'Schweregrad', 'Status', 'Priorität',
    'Geplantes Behebungsdatum', 'Tatsächliches Behebungsdatum', 'Kategorie', 'Auswirkung',
    'Reproduktionsrate', 'Voraussichtliche Sprints bis Behebung (in Wochen)', 'Beeinträchtigte Nutzer'
]

@app.route('/')
def home():
    return render_template('index.html', bug_attributes=bug_attributes)

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    sorting_parameters = data['sorting_parameters']
    sorting_parameters = [parameter for parameter in sorting_parameters if parameter.strip()] # löscht die leeren parameter aus der liste, falls kein attribut ausgewählt wurde
    sorting_parameters = translate_attributes(sorting_parameters)  # mapped die Parameter aus dem UI zu den Attribut namen der Bug Klasse

    print(sorting_parameters)


    # Bugliste einlesen
    csv_file_path = 'Bugreport_fixed_csv.csv'
    bugs_list = read_csv_to_bugs(csv_file_path)

    # Daten wieder von UNIX time zu normalem Format konvertieren
    for bug in bugs_list:
        bug.creation_date = epoch_to_date(bug.creation_date)
        bug.pl_resolved_date = epoch_to_date(bug.pl_resolved_date)
        bug.resolve_date = epoch_to_date(bug.resolve_date)


    # insertionSort funktion mit den sortier parametern aus dem frontend callen
    sorted_bugs = insertion_sort(bugs_list, *sorting_parameters)



    # neue Liste mit den Werten der Bugs erstellen, damit wir diese als JSON returnen können
    sorted_bugs_serializable = []
    for bug in sorted_bugs:
        bug_dict = vars(bug)
        bug_dict['severity'] = reverse_map_values(bug.severity)
        bug_dict['priority'] = reverse_map_values(bug.priority)
        bug_dict['reproductionrate'] = reverse_map_values(bug.reproductionrate)
        bug_dict['effect'] = reverse_map_values(bug.effect)
        sorted_bugs_serializable.append(bug_dict)

    print(f'DEBUGGING: {sorted_bugs_serializable}')
    print(f'serialized bugs: {sorted_bugs_serializable}')
    return jsonify(sorted_bugs_serializable=sorted_bugs_serializable)



if __name__ == '__main__':
    app.run(debug=True)
