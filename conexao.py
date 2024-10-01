import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'root',
    host = 'localhost',
    db = 'projeto_crud'
)