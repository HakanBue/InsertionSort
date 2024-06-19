from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

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
    # sorting_parameters = []
    return jsonify(message=f'test')



if __name__ == '__main__':
    app.run(debug=True)
