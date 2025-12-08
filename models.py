from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LivroModel(db.Model):
    __tablename__ = 'livros'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    paginas = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'autor': self.autor,
            'ano': self.ano,
            'paginas': self.paginas
        }