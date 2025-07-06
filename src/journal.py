import streamlit as st
import sqlite3
from datetime import datetime
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK sentiment analyzer
try:
    sia = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()

# Database initialization
def init_journal_db():
    conn = sqlite3.connect('journal.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS journal_entries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 entry_text TEXT,
                 sentiment_scores TEXT,
                 detected_mood TEXT,
                 timestamp DATETIME,
                 feedback INTEGER DEFAULT 0,
                 user_id INTEGER,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS favorite_songs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 track_name TEXT,
                 artist TEXT,
                 spotify_url TEXT,
                 timestamp DATETIME,
                 user_id INTEGER,
                 FOREIGN KEY(user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()

init_journal_db()

# Activity suggestions
# st.set_page_config(
#             page_title="Journal Page",
#             page_icon="🫶",
#             layout="wide",)

STUDY_ACTIVITIES = [
    "Try the Pomodoro technique (25min work/5min break)",
    "Listen to lo-fi study beats",
    "Organize your workspace",
    "Do some light stretching"
]

GENERAL_ACTIVITIES = [
    "Take a walk outside",
    "Call a friend for a quick chat",
    "Write in a gratitude journal",
    "Try a new hobby for 30 minutes"
]

def store_journal_entry(text):
    conn = sqlite3.connect('journal.db')
    c = conn.cursor()
    c.execute('''INSERT INTO journal_entries
                 (entry_text, timestamp)
                 VALUES (?, ?)''',
              (text, datetime.now()))
    conn.commit()
    conn.close()

def save_favorite(track, spotify_url):
    try:
        track_parts = track.split(" - ")
        track_name = track_parts[0] if len(track_parts) > 0 else track
        artist = track_parts[1] if len(track_parts) > 1 else "Unknown Artist"

        conn = sqlite3.connect('journal.db')
        c = conn.cursor()
        c.execute('''INSERT INTO favorite_songs
                     (track_name, artist, spotify_url, timestamp)
                     VALUES (?, ?, ?, ?)''',
                  (track_name, artist, spotify_url, datetime.now()))
        conn.commit()
        st.success(f"Saved **{track_name}** by *{artist}* to favorites!")
    except Exception as e:
        st.error(f"Error saving favorite: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

def display_favorites():
    st.subheader("❤️ Your Favorite Songs")
    try:
        conn = sqlite3.connect('journal.db')
        c = conn.cursor()
        c.execute('''SELECT track_name, artist, spotify_url
                     FROM favorite_songs
                     ORDER BY timestamp DESC LIMIT 10''')
        favorites = c.fetchall()

        if favorites:
            for track_name, artist, url in favorites:
                st.markdown(f"🎵 **{track_name}** by {artist} \n[Play]({url})")
        else:
            st.info("You haven't saved any favorite songs yet!")
    except Exception as e:
        st.error(f"Error loading favorites: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

def store_feedback(feedback):
    conn = sqlite3.connect('journal.db')
    c = conn.cursor()
    c.execute("SELECT id FROM journal_entries ORDER BY id DESC LIMIT 1")
    last_entry_id = c.fetchone()
    if last_entry_id:
        entry_id = last_entry_id[0]
        c.execute('''UPDATE journal_entries
                     SET feedback = ?, detected_mood = ?
                     WHERE id = ?''',
                  (feedback['rating'], feedback['mood'], entry_id))
        conn.commit()
    conn.close()

# analyze journel input 
def analyze_sentiment(text, sp):
    scores = sia.polarity_scores(text)
    compound_score = scores['compound']

    if compound_score >= 0.6:
        mood = "Ecstatic 😁"
    elif compound_score >= 0.05:
        mood = "Positive 😊"
    elif compound_score <= -0.6:
        mood = "Distressed 😣"
    elif compound_score <= -0.05:
        mood = "Negative 😔"
    else:
        mood = "Neutral 😐"

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Detected Mood", mood)
    with col2:
        st.metric("Confidence Score", f"{compound_score:.2f}")
    with col3:
        st.write("**Breakdown:**")
        st.write(f"Positive: {scores['pos']:.2f}")
        st.write(f"Neutral: {scores['neu']:.2f}")
        st.write(f"Negative: {scores['neg']:.2f}")

    return mood