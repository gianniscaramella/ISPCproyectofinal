from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laws.db'
db = SQLAlchemy(app)


class Law(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))

    def __init__(self, number, title, description):
        self.number = number
        self.title = title
        self.description = description

# Ruta para consultar por número de ley


@app.route('/consulta/numero/<number>', methods=['GET'])
def consulta_numero(number):
    law = Law.query.filter_by(number=number).first()
    if law:
        result = {
            'number': law.number,
            'title': law.title,
            'description': law.description
        }
        return jsonify(result)
    else:
        return jsonify({'message': 'No se encontró la ley solicitada.'})

# Ruta para consultar por palabras clave


@app.route('/consulta/palabras', methods=['GET'])
def consulta_palabras():
    keywords = request.args.get('keywords')
    laws = Law.query.filter(Law.title.contains(
        keywords) | Law.description.contains(keywords)).all()
    if laws:
        results = []
        for law in laws:
            result = {
                'number': law.number,
                'title': law.title,
                'description': law.description
            }
            results.append(result)
        return jsonify(results)
    else:
        return jsonify({'message': 'No se encontraron leyes relacionadas a las palabras clave.'})


if __name__ == '__main__':
    app.run(debug=True)
