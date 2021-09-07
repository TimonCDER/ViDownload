import streamlit as st
from pytube import YouTube

st.title("ViDownloader")
st.subheader("Indiquez l'URL de la vidéo que vous souhaitez télécharger")
url = st.text_input(label='URL')

if url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=300)
    st.subheader('''
    {}
    ## Durée: {} seconds
    ## Note: {} 
    '''.format(yt.title, yt.length, yt.rating))
    video = yt.streams
    if len(video) > 0:
        downloaded, download_audio = False, False
        download_video = st.button("Télécharger la vidéo")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Télécharger le son uniquement")
        if download_video:
            video.get_lowest_resolution().download()
            downloaded = True
        if download_audio:
            video.filter(only_audio=True).first().download()
            downloaded = True
        if downloaded:
            st.subheader("Téléchargement terminé")
    else:
        st.subheader("Désolé, cette vidéo ne peut pas être téléchargée")
