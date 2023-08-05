import sqlite3

db_user = "database.db"
conn = sqlite3.connect(db_user)

def create_table():
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS users
        (username TEXT NOT NULL PRIMARY KEY,
        password TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        country TEXT NOT NULL,
        fav_comedian TEXT,
        personality TEXT)"""
    )
    create_user("admin", "admin", 21, "female", "Malaysia", "Kevin Hart", "Analysts")
    conn.commit()
    conn.close()

def delete_table():
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    conn.close()

def create_user(username, password, age, gender, country, fav_comedian=None, personality=None):
    c = conn.cursor()
    c.execute(
        # "INSERT INTO users (username, password, age, gender, country, fav_comedian) VALUES (?, ?, ?, ?, ?, ?)",
        # (username, password, age, gender, country, fav_comedian),
        "INSERT INTO users (username, password, age, gender, country, fav_comedian, personality) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (username, password, age, gender, country, fav_comedian, personality),
    )
    conn.commit()
    conn.close()

def login_user(username, password):
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None

def get_user_info_by_username(username):
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result 

def get_all_user():
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users

def delete_user_by_username(username):
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username <> 'admin' AND username=?", (username,))
    conn.commit()
    conn.close()

def delete_all_users():
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username <> 'admin'")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # delete_table()
    # create_table()
    print(get_all_user())