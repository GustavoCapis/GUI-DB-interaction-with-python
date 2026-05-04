import psycopg2

#criar conexão com o banco de dados
conexao = psycopg2.connect(
    database="postgresDB",
    user="admin",
    password="admin123",
    host="127.0.0.1",
    port="5432"
)
print("Conexão com o banco de dados estabelecida com sucesso!")

#criar um cursor para executar comandos SQL
cursor = conexao.cursor()