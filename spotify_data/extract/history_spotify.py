import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# Configuração de credenciais
CLIENT_ID = "97c664619fca43d08f8f0c42be11a9c2"
CLIENT_SECRET = "8c1e1bcd273244219ea9460f2c94eefd"
REDIRECT_URI = "http://127.0.0.1:8000/callback"

# Autenticação com o Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read user-read-recently-played"))

# Pega o histórico de reprodução recente
history = sp.current_user_recently_played(limit=50)  # Você pode aumentar o limit se precisar de mais registros

# Salva o histórico em um arquivo JSON
with open('historico_spotify.json', 'w', encoding='utf-8') as f:
    json.dump(history, f, ensure_ascii=False, indent=4)

print("Histórico salvo em 'historico_spotify.json'")
