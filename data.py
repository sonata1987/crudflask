import sqlite3

#conexão
def connect_db():
    conn=sqlite3.connect('data.db')
    return conn

   
#criação da tabela
def create_table():
    conn = connect_db()
    conn.execute('''
        Create Table if not exists livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,       
            autor TEXT NOT NULL,      
            ano INTEGER NOT NULL,     
            paginas INTEGER NOT NULL  
        );
    ''')
    conn.close()
  

#obter livros
def get_livros():
    livros = [] 
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM livros")
    rows = cursor.fetchall()
    for row in rows:
        livro = {
            'id': row['id'],
            'nome': row['nome'],
            'autor': row['autor'],
            'ano': row['ano'],
            'paginas': row['paginas']
        }
        livros.append(livro)
    conn.close() 
    return livros


# adicionar livros
def add_livro(livro_data):
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
def delete_livro(id):
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
def update_livro(id, livro_data):
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
    

create_table()
