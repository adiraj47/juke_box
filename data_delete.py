import table
import sqlite3 as sql
import streamlit as st
table.create_table()
connection = sql.connect("audio.sqlite", check_same_thread=False)


def delete_artist(artist_name):
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("SELECT artist_id FROM artist WHERE artist_name = ?", (artist_name,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM artist WHERE artist_id = ?", (row[0], ))
        cursor.connection.commit()
        st.write("Record Deleted successfully")
    else:
        st.write("Record not found!!")


def delete_playlist(song_name):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM playlist WHERE name = ?", (song_name,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM playlist WHERE id = ?", (row[0], ))
        cursor.connection.commit()
        st.write("Record Deleted successfully")
    else:
        st.write("Record not found!!")