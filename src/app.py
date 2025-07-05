import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize NLTK resources
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Configure page settings
st.set_page_config(
    page_title="Cadence - Teen Well-being Companion",
    page_icon="🌱",
    layout="wide"
)

# Main application layout
def main():
    st.title("🌱 Cadence - Your Digital Well-being Companion")
    st.markdown("### Share your thoughts, and let's find your rhythm together!")
    
    # Journal input section
    with st.form("journal_entry"):
        journal_text = st.text_area(
            "How are you feeling today? Write freely here:",
            height=200,
            placeholder="Today I felt...",
            help="Write about your day, feelings, or anything on your mind"
        )
        submitted = st.form_submit_button("Analyze Mood")
    
    if submitted and journal_text:
        analyze_sentiment(journal_text)

# Sentiment analysis and display
def analyze_sentiment(text):
    # Get sentiment scores
    scores = sia.polarity_scores(text)
    compound_score = scores['compound']
    
    # Determine mood category
    if compound_score >= 0.05:
        mood = "Positive 😊"
    elif compound_score <= -0.05:
        mood = "Negative 😔"
    else:
        mood = "Neutral 😐"
    
    # Display results in columns
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
    
    # Mood-based recommendations section
    st.subheader("Suggested Activities")
    show_study_mode = st.toggle("Activate Study Mode 🎧")
    
    if show_study_mode:
        st.success("🔕 Notifications paused - Focus time activated!")
        st.write("""
        - Try the Pomodoro technique (25min work/5min break)
        - Listen to lo-fi study beats
        - Stay hydrated with water breaks
        """)
    else:
        st.write("""
        - Take a walk outside
        - Call a friend for a quick chat
        - Practice deep breathing exercises
        """)

if __name__ == "__main__":
    main()