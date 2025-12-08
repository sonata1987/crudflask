import sqlite3
from interfaces import LivroRepositoryInterface
from models import db, LivroModel

class LivroRepository(LivroRepositoryInterface):
    #obter livros
    def get_all(self) -> list[dict]:
        livros_objs = LivroModel.query.all()
        return [livro.to_dict() for livro in livros_objs]

# adicionar livros
    def add(self, livro_data: dict) -> dict:
        novo_livro = LivroModel(
            nome=livro_data.get('nome'),
            autor=livro_data.get('autor'),
            ano=livro_data.get('ano'),
            paginas=livro_data.get('paginas')
        )
        db.session.add(novo_livro)
        db.session.commit()
        
        return novo_livro.to_dict()


    #deletar livros
    def delete(self, id: int) -> bool:
        livro = LivroModel.query.get(id)
        if livro:
            db.session.delete(livro)
            db.session.commit()
            return True
        return False 
        

    #atualizar livro
    def update(self, id: int, livro_data: dict) -> bool:
        livro = LivroModel.query.get(id)
        if livro:
            livro.nome = livro_data.get('nome', livro.nome)
            livro.autor = livro_data.get('autor', livro.autor)
            livro.ano = livro_data.get('ano', livro.ano)
            livro.paginas = livro_data.get('paginas', livro.paginas)
            
            db.session.commit()
            return True
        return False 

   


