import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS expense_splitter_db")
    print("Database created successfully")
except Exception as e:
    print(f"Error creating database: {e}")
