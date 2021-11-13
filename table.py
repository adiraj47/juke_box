import sqlite3 as sql
connection = sql.connect("audio.sqlite", check_same_thread=False)


def create_table():
    connection.execute("CREATE TABLE IF NOT EXISTS artist (artist_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                       "artist_name VARCHAR)")

    connection.execute("CREATE TABLE IF NOT EXISTS  playlist("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT, aritst_id INTEGER,  name VARCHAR, "
                       "song BLOB, foreign KEY(aritst_id) references artist(artist_id) ON DELETE CASCADE)")
