from bs4 import BeautifulSoup
import requests

from spotipy.oauth2 import SpotifyOAuth
import spotipy

SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'

BILLBOARD_HOT_TOP_100_URL = "https://www.billboard.com/charts/hot-100/"
Client_ID ='your id'
Client_Secret ='your client sec'

#---------Scraping the names of the top 100-------------#
date = input("Which year do you want to travel to? type the date in this format 'YYYY-MM-DD':\n")
response = requests.get(url=BILLBOARD_HOT_TOP_100_URL+date)
html_page = response.text
soup = BeautifulSoup(html_page, "html.parser")
music_list = soup.select(selector='li #title-of-a-story')
music_titles = [_.getText().strip() for _ in music_list]
print(music_titles)

#------Creating spotify object and search for the songs on spotify ------#
Spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(Client_ID,
Client_Secret,
redirect_uri="http://localhost:8888/callback/",
scope="playlist-modify-private",
show_dialog=True,
cache_path=".cache"))
user_id = Spotify.current_user()["id"]
musics_dict = {}
for album in music_titles:
    try:
        result = Spotify.search(q=f"track:{album} year:{date.split('-')[0]}", type="track", limit=1, offset=0)
        song_dic = result["tracks"]
        song_items = song_dic["items"]
        song = song_items[0]["external_urls"]["spotify"]
        musics_dict[album] = song
    except:
        pass
    print(musics_dict)

#-------------- Create the playlist and add the songs ----------#
playlist = Spotify.user_playlist_create(user_id, f"{date} Billboard 100", public=False, collaborative=False, description='')
for _ in musics_dict.keys():
    song_id = musics_dict[_].split("/")[-1]
    add_song = Spotify.playlist_add_items(
    playlist_id=playlist["id"],
    items=[f'spotify:track:{song_id}'],
    position=None
    )