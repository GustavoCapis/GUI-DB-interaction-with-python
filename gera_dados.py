from faker import Faker
from conectar import conexao, cursor

#gerar dados falsos para a tabela PRODUTO
fake = Faker('pt_BR')

for _ in range(10):
    nome = fake.word().capitalize()
    preco = round(fake.random_number(digits=5) / 100, 2)
    print(f"Inserindo produto: {nome} - R$ {preco}")
    cursor.execute("INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)", (nome, preco))

#salvar as alterações no banco de dados
conexao.commit()
#imprimir mensagem de sucesso
print("Dados inseridos com sucesso na tabela PRODUTO!")
#fechar a conexão com o banco de dados
cursor.close()
conexao.close()