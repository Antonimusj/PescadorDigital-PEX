import mysql.connector

# Conecte ao MySQL sem especificar o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # seu usuário MySQL
    password="1234",   # sua senha MySQL
    port=3306          # porta padrão do MySQL
)
conn.autocommit = True
cursor = conn.cursor()

# Crie o banco
cursor.execute("CREATE DATABASE IF NOT EXISTS pescadores;")

cursor.close()
conn.close()

print("Banco de dados 'pescadores' criado com sucesso!")
