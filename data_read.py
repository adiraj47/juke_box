import sqlite3 as sql
import table
table.create_table()
connection = sql.connect("audio.sqlite", check_same_thread=False)


def display_data(name):
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM playlist WHERE name = ?", (name, ))
    row = cursor.fetchall()
    return row
def display_all_data(artist_id):
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM playlist WHERE aritst_id = ?", (artist_id, ))
    row = cursor.fetchall()
    return row


def play_song(song_id):
    cursor = connection.cursor()
    cursor.execute("SELECT song FROM playlist WHERE id = ?", (song_id,))
    row = cursor.fetchone()
    return row


def display_artist():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM artist")
    row = cursor.fetchall()
    return row


def display_artist_id(artist_name):
    cursor = connection.cursor()
    cursor.execute("SELECT artist_id FROM artist WHERE artist_name = ?", (artist_name, ))
    row = cursor.fetchone()
    return row[0]


if __name__ == "__main__":
    data = play_song(1)
    print(data)
    # with open("play_song.mp3", "wb") as write_song:
    #     write_song.write(data[0])
    # with open("play_song.mp3", "rb") as read_song:
    #     audio = read_song.read()


