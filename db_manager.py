import sqlite3


DATABASE = 'todo.db'

'''
from flask import g

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
'''


#def query_db(query, args=(), one=False):
    #cur = get_db().execute(query, args)
    #rv = cur.fetchall()
    #cur.close()
    
    #return (rows[0] if rv else None) if one else rows

def listeTodo():   
    # old school
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("""SELECT * FROM todo_items""")
    rows = cursor.fetchall();

    cursor.close()
    return rows

    #return (rv[0] if rv else None) if one else rv

def maj_state_item():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("""UPDATE todo_items SET state = ? WHERE id = ?""", (state,id))
    cursor.close()


def add_item(item):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO todo_items(name, state) VALUES(?, ?)""", (item, "do"))
'''
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
'''