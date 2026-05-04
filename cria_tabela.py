from conectar import conexao, cursor

#criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS PRODUTO (
    CODIGO SERIAL PRIMARY KEY,
    NOME VARCHAR(100) NOT NULL,
    PRECO NUMERIC(10, 2) NOT NULL,
    );''')
print("Tabela PRODUTO criada com sucesso!")
#salvar as alterações no banco de dados
conexao.commit()
#fechar a conexão com o banco de dados
cursor.close()