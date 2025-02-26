import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

CLIENT_ID = "97c664619fca43d08f8f0c42be11a9c2"
CLIENT_SECRET = "8c1e1bcd273244219ea9460f2c94eefd"
REDIRECT_URI = "http://127.0.0.1:8000/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-read-private,user-library-read"
))

user_data = sp.current_user()
print("\nDados do Usuário:")
print(json.dumps(user_data, indent=4))

playlists = sp.current_user_playlists()
print("\nPlaylists do Usuário:")
print(json.dumps(playlists, indent=4))


playlist_tracks = {}

for playlist in playlists["items"]:
    playlist_name = playlist["name"]
    playlist_id = playlist["id"]

    tracks = sp.playlist_tracks(playlist_id)
    playlist_tracks[playlist_name] = tracks

with open("spotify_tracks.json", "w", encoding="utf-8") as f:
    json.dump(playlist_tracks, f, ensure_ascii=False, indent=4)

print("\n✅ Músicas das playlists salvas em spotify_tracks.json")

