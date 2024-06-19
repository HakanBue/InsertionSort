from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from sorter import insertion_sort
from Bug import read_csv_to_bugs

app = Flask(__name__)
CORS(app)

# Liste der Attribute der Bugs-Klasse
bug_attributes = [
    'Bug-ID', 'Erstellungsdatum', 'Schweregrad', 'Status', 'Beschreibung', 'Priorität',
    'Geplantes Behebungsdatum', 'Tatsächliches Behebungsdatum', 'Kategorie',
    'Reproduktionsrate', 'Voraussichtliche Sprints bis Behebung (in Wochen)', 'Beeinträchtigte Nutzer'
]

@app.route('/')
def home():
    return render_template('index.html', bug_attributes=bug_attributes)

@app.route('/sort', methods=['POST'])
def submit():
    data = request.json
    print(data)
    sorting_parameters = data['sorting_parameters']


    # Bugs einlesen
    csv_file_path = 'Bugreport_fixed_csv.csv'
    bugs_list = read_csv_to_bugs(csv_file_path)

    for bug in bugs_list:
        print(f'{vars(bug)} \n \n --------  ')
    
    
    return jsonify(message=f'{data}')



if __name__ == '__main__':
    app.run(debug=True)
