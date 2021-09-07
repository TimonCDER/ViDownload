import os
import streamlit as st
from pytube import YouTube

st.title("ViDownloader par Timon")
st.subheader("Indiquez l'URL de la vidéo que vous souhaitez télécharger")
url = st.text_input(label='URL')


if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=400)
    st.subheader('''
    {}
    ## Durée: {} seconds 
    '''.format(yt.title, yt.length))
    video = yt.streams
    if len(video) > 0:
        downloaded, download_audio = False, False
        download_video_lowquality = st.button("Télécharger la vidéo en basse résolution")
        download_video_highquality = st.button("Télécharger la vidéo en haute résolution")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Télécharger le son uniquement")
        if download_video_lowquality:
            video.get_lowest_resolution().download()
            downloaded = True
        if download_video_highquality:
            video.get_highest_resolution().download()
            downloaded = True
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Téléchargement terminé")
    else:
        st.subheader("Désolé, cette vidéo ne peut pas être téléchargée")

