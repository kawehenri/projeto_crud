import mysql
import mysql.connector

conn = mysql.connector.connect(
    user = 'kawe',
    host = 'localhost',
    db = 'projeto_crud',
    password = 'projeto123'
)

if conn.is_connected():
    print('Banco conectado com sucesso! ')
else:
    print('Banco não conectado! ')