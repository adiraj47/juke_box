import table
import sqlite3 as sql
import streamlit as st
table.create_table()
connection = sql.connect("audio.sqlite", check_same_thread=False)


def update_artist(artist_name, update_artist_name):
    cursor = connection.cursor()
    cursor.execute("SELECT artist_id FROM artist WHERE artist_name = ?", (artist_name, ))
    row = cursor.fetchone()
    if row:
        cursor.execute("UPDATE artist SET artist_name = ? WHERE artist_id = ?", (update_artist_name, row[0]))
        cursor.connection.commit()
        st.write("Database updated")
    else:
        st.write("Record not found")

def update_playlist(song_name, update_column, update_value):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM playlist WHERE name = ?", (song_name,))
    row = cursor.fetchone()
    if row:
        if update_column == "aritst_id":
            cursor.execute("SELECT artist_id FROM artist WHERE artist_name = ?", (update_value, ))
            artist_id = cursor.fetchone()
            if artist_id:
                cursor.execute("UPDATE playlist SET aritst_id = ? WHERE id = ?", (artist_id[0], row[0]))
                st.write("Database updated")
                cursor.connection.commit()
            else:
                st.write("No such artist present ")
        else:
            query = f"UPDATE playlist SET {update_column} = ? WHERE id = ?"
            cursor.execute(query, (update_value, row[0]))
            cursor.connection.commit()
            st.write("Database updated")
    else:
        st.write("Record not found")




