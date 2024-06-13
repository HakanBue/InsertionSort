from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Liste der Attribute der Bugs-Klasse
bug_attributes = [
    'Bug-ID', 'Erstellungsdatum', 'Schweregrad', 'Status', 'Beschreibung', 'Priorität',
    'Geplantes Behebungsdatum', 'Tatsächliches Behebungsdatum', 'Kategorie',
    'Reproduktionsrate', 'Voraussichtliche Sprints bis Behebung (in Wochen)', 'Beeinträchtigte Nutzer'
]

@app.route('/')
def home():
    return render_template('Index.html', bug_attributes=bug_attributes)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    attribute1 = data['attribute1']
    attribute2 = data['attribute2']
    return jsonify(message=f'You selected {attribute1} and {attribute2}')

if __name__ == '__main__':
    app.run(debug=True)
