import sqlite3

conn = sqlite3.connect('emails.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM emails")
conn.commit()
conn.close()