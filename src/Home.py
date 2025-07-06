import streamlit as st
from css import CSS_STYLES

def home():
    # st.set_page_config(
    #         page_title="Home Page",
    #         page_icon="🫶",
    #         layout="centered",)
    # Apply CSS styles
    st.markdown(CSS_STYLES, unsafe_allow_html=True)
    
    # Header with logo and auth buttons
    header_col1, header_col2 = st.columns([1,4])
    with header_col1:
        st.markdown('<div class="header-logo">🫶</div>', unsafe_allow_html=True)
    with header_col2:
        _, btn_col1, btn_col2 = st.columns([3,1,1])
        with btn_col1:
             if st.button("Login", key="header_login", use_container_width=True,
                       help="Access your existing account"):
                st.session_state.show_login = True
                st.session_state.show_home = False
                st.rerun()
        with btn_col2:
            if st.button("Register", key="header_register",
                       help="Create a new account"):
                st.session_state.show_login = False
                st.session_state.show_home = False
                st.rerun()

    # Hero section
    st.markdown("""
    <div class="hero">
        <h1><span class="logo-emoji">🫶 Cadence</span><br>Your Digital Well-being Companion</h1>
        <p>Find balance in your digital life through personalized music and mindful breaks</p>
    </div>
    """, unsafe_allow_html=True)

    # Features grid
    with st.container():
        st.subheader("Why Choose Cadence?")
        cols = st.columns(3)
        features = [
            ("🎵 Adaptive Music", "Get personalized playlists that match your emotional state"),
            ("🧘 Digital Detox Tools", "Smart nudges for healthier screen habits"),
            ("📈 Progress Tracking", "Visualize your emotional journey over time")
        ]
        for col, (emoji, text) in zip(cols, features):
            with col:
                st.markdown(f"""
                <div class="feature-card">
                    <div class="feature-emoji">{emoji.split()[0]}</div>
                    <h3>{emoji}</h3>
                    <p>{text}</p>
                </div>
                """, unsafe_allow_html=True)

    # Call to action
    st.markdown("""
    <div class="cta-section">
        <h2>Ready to Find Your Rhythm?</h2>
        <div class="cta-buttons">
            <button class="cta-button">Get Started</button>
            <button class="cta-button secondary">Learn More</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home()