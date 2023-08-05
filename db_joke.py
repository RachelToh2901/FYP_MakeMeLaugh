import sqlite3

db_joke = "database.db"
conn = sqlite3.connect(db_joke)

def create_table():
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS jokes
        (joke_id INTEGER PRIMARY KEY AUTOINCREMENT,
        joke TEXT NOT NULL,
        keyword TEXT NOT NULL,
        BERT_rating INTEGER NOT NULL,
        user_rating INTEGER NOT NULL,
        username TEXT NOT NULL,
        FOREIGN KEY (username) REFERENCES users (username))"""
    )
    insert_joke("a_joke", "a_keyword", 3, 2, "admin")
    conn.commit()
    conn.close()

def delete_table():
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS jokes")
    conn.commit()
    conn.close()

def insert_joke(joke, keyword, BERT_rating, user_rating, username):
    c = conn.cursor()
    c.execute(
        "INSERT INTO jokes (joke, keyword, BERT_rating, user_rating, username) VALUES (?, ?, ?, ?, ?)",
        (joke, keyword, BERT_rating, user_rating, username),
    )
    conn.commit()
    conn.close()

def get_jokes_by_username(username):
    c = conn.cursor()
    c.execute("SELECT * FROM jokes WHERE username=?", (username,))
    result = c.fetchall()
    conn.close()
    return result 

def get_all_jokes():
    c = conn.cursor()
    c.execute("SELECT * FROM jokes")
    jokes = c.fetchall()
    conn.close()
    return jokes

def delete_jokes_by_username(username):
    c = conn.cursor()
    c.execute("DELETE FROM jokes WHERE username=?", (username,))
    conn.commit()
    conn.close()

def delete_all_jokes():
    c = conn.cursor()
    c.execute("DELETE FROM jokes")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # delete_table()
    # create_table()
    print(get_all_jokes())
    