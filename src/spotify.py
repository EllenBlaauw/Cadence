import streamlit as st
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import requests

# Feature flag for Spotify integration
SPOTIFY_ENABLED = True

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize Spotify client
def init_spotify_client():
    try:
        if not all([os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET")]):
            raise ValueError("Missing Spotify credentials in .env")
            
        return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
        ))
    except Exception as e:
        st.error(f"Spotify integration disabled: {str(e)}")
        return None

def validate_spotify_credentials():
    """Check if required environment variables are set"""
    required_env_vars = [
        "SPOTIFY_CLIENT_ID",
        "SPOTIFY_CLIENT_SECRET",
        "SPOTIFY_REDIRECT_URI"
    ]
    missing = [var for var in required_env_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing Spotify credentials: {', '.join(missing)}")

# Get mood-based playlist
def get_mood_playlist(sp, mood):
    mood_keywords = {
        "Ecstatic 😁": "upbeat happy",
        "Positive 😊": "positive vibes",
        "Neutral 😐": "chill lofi",
        "Negative 😔": "sad songs",
        "Distressed 😣": "zen music"
    }

    try:
        if not sp or not hasattr(sp, 'search'):
            raise ValueError("Spotify client not initialized")
            
        results = sp.search(q=mood_keywords.get(mood, "mixed emotions"), type='playlist', limit=1)
        if not results or not results.get('playlists', {}).get('items'):
            st.warning(f"No Spotify playlist found for mood: {mood}. Using a fallback.")
            return {
                "title": "🌟 General Music Recommendation",
                "tracks": ["No specific playlist found, enjoy some chill tunes!", "Lofi Study Beats"],
                "image": None,
                "url": "#"
            }

        playlist = results['playlists']['items'][0]
        if not playlist:
            raise ValueError("Invalid playlist data")

        tracks = sp.playlist_tracks(playlist.get('id', ''), limit=4).get('items', [])

        valid_tracks = []
        for t in tracks:
            if t and t.get('track'):
                track_name = t['track'].get('name', 'Unknown Track')
                artist_name = t['track'].get('artists', [{}])[0].get('name', 'Unknown Artist')
                valid_tracks.append(f"{track_name} - {artist_name}")

        if not valid_tracks:
            st.warning(f"Playlist '{playlist.get('name', 'Unknown Playlist')}' has no playable tracks. Using a fallback.")
            return {
                "title": "🌟 General Music Recommendation",
                "tracks": ["No playable tracks in this playlist, try another!", "Relaxing Piano Music"],
                "image": None,
                "url": "#"
            }

        playlist_image = 'https://via.placeholder.com/100'
        if playlist.get('images'):
            playlist_image = playlist['images'][0].get('url', playlist_image)
            
        return {
            "title": playlist.get('name', 'Mood Playlist').strip() or 'Curated Playlist',
            "tracks": valid_tracks[:4],  # Ensure max 4 tracks
            "image": playlist_image,
            "url": playlist.get('external_urls', {}).get('spotify', '#')
        }

    except spotipy.SpotifyException as e:
        st.error(f"Spotify API Error: {e.msg} (code {e.code})")
        return get_fallback_playlist()
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {str(e)}")
        return get_fallback_playlist()
    except Exception as e:
        st.error(f"""Unexpected error: {str(e)}
        Please try again later or check your Spotify credentials""")
        return get_fallback_playlist()

def get_fallback_playlist():
    """Returns a curated fallback playlist when Spotify integration fails"""
    return {
        "title": "🎵 Cadence Curated Playlist",
        "tracks": [
            "Chill Study Beats - Lofi Vibes",
            "Pump Up Jams - Energy Boost Mix",
            "Sad But Safe Space - Melancholy Melodies",
            "Happy Vibes - Upbeat Anthems"
        ],
        "image": "https://via.placeholder.com/100",
        "url": "#"
    }

def show_spotify_setup_guide():
    st.markdown("""
    ### Spotify Integration Setup Guide
    1. Create a Spotify Developer account at [developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/)
    2. Create a new app in the Dashboard.
    3. Add `http://localhost:8501` to Redirect URIs in your app settings (if running locally).
    4. Create a `.env` file in your project root with:
        ```
        SPOTIFY_CLIENT_ID="your-client-id"
        SPOTIFY_CLIENT_SECRET="your-client-secret"
        SPOTIFY_REDIRECT_URI="http://localhost:8501"
        ```
    """)