import table
import sqlite3 as sql
import streamlit as st
table.create_table()
connection = sql.connect("audio.sqlite", check_same_thread=False)

def store_artist(artist_name):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM artist WHERE artist_name = ?", (artist_name,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        cursor.execute("INSERT INTO artist (artist_name) VALUES (?)", (artist_name, ))
        cursor.connection.commit()
        cursor.execute("SELECT artist_id FROM artist WHERE artist_name = ?", (artist_name, ))
        id = cursor.fetchone()

        return id[0]


def store_audio(name, file, artist_name):
    cursor = connection.cursor()
    artist_id = store_artist(artist_name)
    st.write(artist_id)
    cursor.execute("INSERT INTO playlist (name, song, aritst_id) VALUES (?, ?, ?)", (name, file, artist_id))
    cursor.connection.commit()



if __name__ == "__main__":
    with open("bts.mp3", "rb") as read_song:
        data = read_song.read()
        print(type(data))
        # store_audio("bts", data)

