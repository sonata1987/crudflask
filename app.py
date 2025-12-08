import dados
from flask import Flask, make_response, request, jsonify, json
from dados import LivroRepository
from models import db

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

livro_repo = LivroRepository()     

@app.route('/livros', methods=['GET'])
def get_all():
    return make_response(
        jsonify(livro_repo.get_all())
    )

@app.route('/livros', methods=['POST'])
def post():
    livro_data = request.json
    livro_inserido = livro_repo.add(livro_data) 
    return make_response(jsonify(livro_inserido))
    

@app.route('/livros/<int:id>', methods=['DELETE'])
def delete(id):
    livro_repo.delete(id)
    return make_response('', 204)


@app.route('/livros/<int:id>', methods=['PATCH'])
def update(id):
    livro_data = request.json
    livro_atualizado = livro_repo.update(id, livro_data)
    return make_response(jsonify(livro_atualizado))


if __name__ == '__main__':
    app.run(debug=True)


