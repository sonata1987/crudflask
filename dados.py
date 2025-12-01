import sqlite3
from db_connect import connect_db
from interfaces import LivroRepositoryInterface

class LivroRepository(LivroRepositoryInterface):
    #obter livros
    def get_all(self):
        livros = [] 
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM livros")
        rows = cursor.fetchall()
        for row in rows:
            livros.append(dict(row))
        conn.close() 
        return livros


# adicionar livros
    def add(self,livro_data):
        nome = livro_data.get('nome')
        autor = livro_data.get('autor')
        ano = livro_data.get('ano')
        paginas = livro_data.get('paginas')
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO livros (nome, autor, ano, paginas)
            VALUES (?, ?, ?, ?)
        ''', (nome, autor, ano, paginas))
        livro_data['id'] = cursor.lastrowid 
        conn.commit() 
        return livro_data     
        conn.close()

    #deletar livros
    def delete(self,id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM livros
            WHERE id = ?
        ''', (id,))
        
        conn.commit()
        conn.close()
        return cursor.rowcount > 0 
        

    #atualizar livro
    def update(self,id, livro_data):
        nome = livro_data.get('nome')
        autor = livro_data.get('autor')
        ano = livro_data.get('ano')
        paginas = livro_data.get('paginas')
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE livros
            SET nome = ?, autor = ?, ano = ?, paginas = ?
            WHERE id = ?
        ''', (nome, autor, ano, paginas, id))
        
        conn.commit()
        conn.close()
        return cursor.rowcount > 0 

   


