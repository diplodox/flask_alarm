from db_manager import *
import sqlite3

# INIT BDD


'''
cursor.execute("""
CREATE TABLE IF NOT EXISTS todo_items(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     state TEXT
)
""")

conn.commit()

print "Table created successfully";
'''

# INSERT TODO test
'''
cursor.execute("""INSERT INTO todo_items(id, name, state) VALUES(?, ?, ?)""", (2, "a faire", "wait"))
cursor.execute("""INSERT INTO todo_items(id, name, state) VALUES(?, ?, ?)""", (3, "a faire 2", "done"))
cursor.execute("""INSERT INTO todo_items(id, name, state) VALUES(?, ?, ?)""", (4, "a faire 3", "done"))

print "insert ok" 
conn.close()



cursor.execute("""SELECT * FROM todo_items""")
for row in cursor:
   print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))	



conn.close()
'''

    
#for row in rows:
#    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))  

todoListe = listeTodo()
for t in todoListe:
    print ('{0} '.format ) t[0], t[1],t[2]

# Change state of 1 items

# drop 1 item