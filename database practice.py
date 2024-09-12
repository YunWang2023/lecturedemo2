import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='aaa',
    user='root',
    password='200687',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_unicode_ci'
    )

