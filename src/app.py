import streamlit as st
from css import CSS_STYLES, apply_theme_js

# Set page config once at startup (centered layout for all pages)
# st.set_page_config(
#     page_title="Cadence",
#     page_icon="🫶",
#     layout="centered"
# )

from login import show_login_form, show_registration_form, authenticate_user, register_user
from journal import (
    init_journal_db,
    store_journal_entry,
    save_favorite,
    display_favorites,
    store_feedback,
    analyze_sentiment,
    STUDY_ACTIVITIES,
    GENERAL_ACTIVITIES
)
import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv
from spotify import init_spotify_client, get_mood_playlist, show_spotify_setup_guide, SPOTIFY_ENABLED
# Feature flag for Spotify integration (disabled in MVP)
SPOTIFY_ENABLED = True  # Disabled until credentials configured

# --- Session State Initialization (MUST be at the very top) ---
if 'dark_mode_enabled' not in st.session_state:
    st.session_state.dark_mode_enabled = False

if 'last_journal_entry' not in st.session_state:
    st.session_state.last_journal_entry = ""

if 'spotify_data' not in st.session_state:
    st.session_state.spotify_data = {
        "title": "🌟 Music Recommendations",
        "tracks": ["No playlist loaded yet."],
        "image": None,
        "url": "#"
    }

# --- Database Initialization ---
def init_db():
    conn = sqlite3.connect('journal.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE NOT NULL,
                 email TEXT UNIQUE NOT NULL,
                 password_hash TEXT NOT NULL,
                 birthdate DATE NOT NULL,
                 created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                 last_login DATETIME)''')

    conn.commit()
    conn.close()
    init_journal_db()

init_db()

# Initialize Spotify client
sp = init_spotify_client() if SPOTIFY_ENABLED else None

if SPOTIFY_ENABLED and not sp:
    show_spotify_setup_guide()


# --- CSS Styling ---
st.markdown(CSS_STYLES, unsafe_allow_html=True)


# --- Music Recommendations ---
def get_mood_playlist_wrapper(mood):
    # First check if Spotify is enabled and initialized
    if SPOTIFY_ENABLED and sp:
        try:
            return get_mood_playlist(sp, mood)
        except Exception as e:
            st.error(f"Failed to get playlist: {str(e)}")
    
    # Fallback response if Spotify isn't available
    return {
        "title": "🌟 Music Recommendations",
        "tracks": ["Enable Spotify integration for personalized recommendations"],
        "image": None,
        "url": "#"
    }

def analyze_sentiment_ui(text):
    mood = analyze_sentiment(text, sp)
    
    playlist = get_mood_playlist_wrapper(mood)
    st.session_state.spotify_data = playlist

    st.subheader("🎵 Your Personalized Playlist")
    
    if st.session_state.spotify_data['image']:
        st.image(st.session_state.spotify_data['image'], width=300)

    st.write(f"**[{st.session_state.spotify_data['title']}]({st.session_state.spotify_data['url']})**")
    
    col_fb1, col_fb2, col_fb3 = st.columns([1,1,3])
    with col_fb1:
        if st.button("👍 Helpful", use_container_width=True, key="feedback_helpful"):
            st.session_state.feedback = {'mood': mood, 'rating': 1}
            store_feedback(st.session_state.feedback)
            st.success("Thanks for your feedback!")
    with col_fb2:
        if st.button("👎 Not Helpful", use_container_width=True, key="feedback_not_helpful"):
            st.session_state.feedback = {'mood': mood, 'rating': -1}
            store_feedback(st.session_state.feedback)
            st.info("We'll use your feedback to improve recommendations.")

    st.write("Featured tracks:")
    for track in st.session_state.spotify_data['tracks'][:4]:
        with st.container(border=True):
            col1_track, col2_track = st.columns([1, 4])
            with col1_track:
                image_url = st.session_state.spotify_data['image'] or 'https://via.placeholder.com/100'
                st.image(image_url, width=100)
            with col2_track:
                track_name_display = track.split(' - ')[0] if ' - ' in track else track
                artist_name_display = track.split(' - ')[1] if ' - ' in track and len(track.split(' - ')) > 1 else "Unknown Artist"
                st.markdown(f"**{track_name_display}** \n*{artist_name_display}*")
                if st.button("❤️ Save Favorite", key=f"fav_btn_{track}", type="secondary"):
                    save_favorite(track, st.session_state.spotify_data.get('url', '#'))

    st.markdown(f"[Play on Spotify]({st.session_state.spotify_data['url']}) 🎧")
    display_favorites()

    st.subheader("📱 Digital Well-being Tools")
    show_study_mode = st.toggle("Activate Study Mode 🎧",
                                help="Pause notifications and get focused activity suggestions",
                                key="study_mode_toggle")

    if show_study_mode:
        st.success("🔕 Notifications paused - Focus time activated! (Task 2.2.2)")
        st.markdown("**Recommended Focus Activities:**")
        for activity in STUDY_ACTIVITIES:
            st.markdown(f"🍃 {activity}")
    else:
        st.markdown("**Well-being Suggestions:**")
        for activity in GENERAL_ACTIVITIES:
            st.markdown(f"🌻 {activity}")


# --- Authentication Functions ---

# Main application layout
def main():
    # st.set_page_config(
    #         page_title="Home Page",
    #         page_icon="🫶",
    #         layout="centered",)
    # Apply the theme JavaScript at the beginning of each rerun
    apply_theme_js()
        
    if not hasattr(st.session_state, 'logged_in'):
        st.session_state.logged_in = False
    if not hasattr(st.session_state, 'show_home'):
        st.session_state.show_home = True

    if not st.session_state.logged_in:
        if 'show_home' not in st.session_state or st.session_state.show_home:
            from Home import home
            home()
            return

        st.title("🫶 Cadence - Digital Well-being Companion")
        if not hasattr(st.session_state, 'show_login') or st.session_state.show_login:
            st.set_page_config(
              page_title="Login",
              page_icon="🫶",
              layout="centered",)
            show_login_form()
            if st.button("Create New Account"):
                st.session_state.show_login = False
                st.rerun()
        else:
            st.set_page_config(
              page_title="Registration",
              page_icon="🫶",
              layout="centered",)
            show_registration_form()
            if st.button("Back to Login"):
                st.session_state.show_login = True
                st.rerun()
        return

    # Main app content for logged in users
    st.set_page_config(
            page_title="Journal Page",
            page_icon="🫶",
            layout="wide",)
    st.title("🫶 Cadence - Your Digital Well-being Companion")

    col1, col2, col3 = st.columns([4,1,1])
    with col1:
        st.markdown("### Share your thoughts, and let's find your rhythm together!")
    # with col2:
    #     # dark_mode_enabled_toggle = st.toggle(
    #     #     "🌙 Dark Mode",
    #     #     value=st.session_state.dark_mode_enabled,
    #     #     key='dark_mode_toggle'
    #     # )
    #     # if dark_mode_enabled_toggle != st.session_state.dark_mode_enabled:
    #     #     st.session_state.dark_mode_enabled = dark_mode_enabled_toggle
    #     #     st.rerun()
    with col3:
        if st.button("Logout"):
            del st.session_state.logged_in
            del st.session_state.user_id
            st.rerun()

    # Journal input section
    with st.form("journal_entry"):
        journal_text = st.text_area(
            "How are you feeling today? Write freely here:",
            height=200,
            value=st.session_state.last_journal_entry,
            placeholder="Today I felt...",
            help="Write about your day, feelings, or anything on your mind"
        )
        submitted = st.form_submit_button("Analyze Mood")

    if submitted and journal_text:
        st.session_state.last_journal_entry = journal_text
        analyze_sentiment_ui(journal_text)
        store_journal_entry(journal_text)
    elif st.session_state.last_journal_entry:
        analyze_sentiment_ui(st.session_state.last_journal_entry)


if __name__ == "__main__":
    # Validate Spotify credentials before starting app
    if SPOTIFY_ENABLED and (not os.getenv("SPOTIFY_CLIENT_ID") or not os.getenv("SPOTIFY_CLIENT_SECRET")):
        st.error("Missing Spotify API credentials in .env")
        st.stop()
    
    main()