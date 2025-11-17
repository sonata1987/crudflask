from flask import Flask, make_response, request, jsonify, json
import data

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/livros', methods=['GET'])
def get_livros():
    return make_response(
        jsonify(data.get_livros())
    )

@app.route('/livros', methods=['POST'])
def post_livros():
    livro_data = request.json
    livro_inserido = data.add_livro(livro_data) 
    return make_response(jsonify(livro_inserido))
    

@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_livro(id):
    data.delete_livro(id)
    return make_response('', 204)


@app.route('/livros/<int:id>', methods=['PATCH'])
def update_livro(id):
    livro_data = request.json
    livro_atualizado = data.update_livro(id, livro_data)
    return make_response(jsonify(livro_atualizado))


app.run()


