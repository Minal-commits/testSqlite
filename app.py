import sqlite3, bcrypt

con = sqlite3.connect('database/example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, password BLOB)''')

# cur.execute("INSERT INTO users (name, age, password) VALUES ('Alice', 30, 'password123')")

# con.commit()
def add_user(name, age, password):

    print(password)
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cur.execute("INSERT INTO users (name, age, password) VALUES (?, ?, ?)", (name, age, hashed))
    con.commit()

def login_user(name, password):
    cur.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = cur.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[3]):
        return True
    else:
        return False

# add_user('Alice', 30, 'password123')
print(login_user('Alice', 'password123'))