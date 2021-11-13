import streamlit as st
import data_store
import data_read
import data_update
import data_delete
side_box = st.sidebar.selectbox("Please select your choice", ("upload", "available songs", "listen", "delete", "update"))
if side_box == "upload":
    with st.form("audio_store"):
        artist_name = st.text_input("Enter the name of artist")
        name = st.text_input("Please enter the name of the song")
        uploaded_audio = st.file_uploader("Please put the mp3 file here", type="mp3")
        audio_submit = st.form_submit_button("submit")

        if audio_submit:
            bytes_data = uploaded_audio.getvalue()

            data_store.store_audio(name, bytes_data, artist_name)

elif side_box == "available songs":
    with st.form("playlist"):
        name = st.text_input("Please enter the song name")

        playlist_submit = st.form_submit_button("Submit")

        if playlist_submit:
            data = data_read.display_data(name)
            st.write(data)
elif side_box == "listen":

    # with st.form("form_id"):
    artist = st.selectbox("Enter the artist name: ", data_read.display_artist())
    id = st.selectbox("Enter the id of the song",  data_read.display_all_data(artist[0]))
    audio = data_read.play_song(id[0])
    st.audio(audio[0], format="audio/mp3")

elif side_box == "update":
    table_choice = st.selectbox("Please select which table you want to update", ("Artist", "Playlist"))
    if table_choice == "Artist":
        with st.form("update_artist_form"):
            original_name = st.text_input("Please enter the artist name present in the database")
            update_name = st.text_input("Please enter the artist name which you want to put on database")

            artist_submit = st.form_submit_button("Submit")

            if artist_submit:
                data_update.update_artist(original_name, update_name)
    elif table_choice == "Playlist":
        with st.form("update_playlist_form"):
            song_name = st.text_input("Please enter the song name you want to update")
            column_name = st.selectbox("Please select the column you want to update", ("aritst_id", "name"))
            update_column = st.text_input("The value which you want to put in database")

            playlist_submit = st.form_submit_button("submit")
            if playlist_submit:
                data_update.update_playlist(song_name, column_name, update_column)
elif side_box == "delete":

    table_choice = st.selectbox("Please select which table you want to Delete", ("Artist", "Playlist"))
    if table_choice == "Artist":
        with st.form("Delete_artist_form"):
            name = st.text_input("Please Enter the name of artist")

            delete_artist_submit = st.form_submit_button("Submit")

            if delete_artist_submit:
                data_delete.delete_artist(name)

    elif table_choice == "Playlist":
        with st.form("Delete_playlist_form"):
            song_name = st.text_input("Please enter the song name")

            playlist_delete_submit = st.form_submit_button("Submit")
            if playlist_delete_submit:
                data_delete.delete_playlist(song_name)






