import sqlite3

# Conecta ao banco
def connect_db():
    return sqlite3.connect('dados.db')

   
#criação da tabela
def init_db():
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
init_db()