# main.py
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load .env variables
load_dotenv()

# OAuth2 Authenticator
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-modify-public"
))


# Create a playlist with 10 songs from a specific genre
def generate_playlist(genre, playlist_name):
    print(f"🔍 Searching for songs in genre: {genre}")
    results = sp.search(q=f'genre:{genre}', type='track', limit=10)

    tracks = [item['id'] for item in results['tracks']['items']]

    if not tracks:
        print("❌ No songs found.")
        return

    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name)
    sp.playlist_add_items(playlist_id=playlist['id'], items=tracks)

    print(f"✅ Playlist '{playlist_name}' created successfully!")


# Example usage
generate_playlist("jazz swing", "Swingin'")

