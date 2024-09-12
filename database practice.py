import mysql.connector
connection = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='aaa',
    user='root',
    password='123456',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci'
    )