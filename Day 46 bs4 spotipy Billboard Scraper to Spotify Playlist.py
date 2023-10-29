from bs4 import BeautifulSoup
import requests
import spotipy

spotify_id = "bd354cc595e9497588949e5c84846f26"
spotify_secret = "1828ad4d52b9499580ccf85180f09f06"

date = input("Enter the desired date in the following format: 1988-03-16.\nThe app will generate a Spotify playlist based on the entered date's Billboard chart.\n")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "html.parser")

artist_names_list = [x.getText().strip() for x in soup.find_all(name="span", class_="a-no-trucate")]
song_names_list = [x.h3.getText().strip() for x in soup.find_all(class_="o-chart-results-list-row-container")]

combined_song_artist_list = dict(zip(song_names_list, artist_names_list))

spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=spotify_id, client_secret=spotify_secret, redirect_uri="http://example.com", scope="playlist-modify-private", cache_path=".spotipyoauthcache")
sp = spotipy.Spotify(auth_manager=spotify_auth)
user_id = sp.current_user()["id"]

songs_uris = []
date_year = date.split("-")[0]
for (song, artist) in combined_song_artist_list.items():
    result1 = sp.search(q=f"track:{song} artist:{artist}", type="track")
    try:
        songs_uris.append(result1["tracks"]["items"][0]["uri"])
    except IndexError:
        try:
            result2 = sp.search(q=f"track:{song}", type="track")
            songs_uris.append(result2["tracks"]["items"][0]["uri"])
        except IndexError:
            None

sp_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, collaborative=False, description=f"ear penetrating trackz from Billboard's {date} chart")

sp_playlist_add_tracks = sp.playlist_add_items(playlist_id=sp_playlist["id"], items=songs_uris)

playlist_link = sp_playlist["external_urls"]["spotify"]
print(f"Here's the link to your custom playlist containing the tracks from Billboard's {date} chart: {playlist_link}")