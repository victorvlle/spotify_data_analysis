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


with open("spotify_data.json", "w", encoding="utf-8") as f:
    json.dump(playlists, f, ensure_ascii=False, indent=4)

print("\n Dados salvos em spotify_data.json")
