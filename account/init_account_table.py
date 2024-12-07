import sqlite3

connection = sqlite3.connect('C:/Users/cyair/run-app-backend/database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Account (username, password) VALUES (?, ?)",
            ('Cyaira', 'Gemini')
            )

cur.execute("INSERT INTO Account (username, password) VALUES (?, ?)",
            ('Sonya', 'Aries')
            )

cur.execute("INSERT INTO Account (username, password) VALUES (?, ?)",
            ('Zoey', 'Gemini')
            )
connection.commit()
connection.close()