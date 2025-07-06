import streamlit as st

CSS_STYLES = r"""
<style>
/* Base colors - these apply universally unless overridden by theme */
:root {
    --primary-color: #71b4d9;
    --secondary-color: #a9a9f5;
    --backgroun-card-color:#def0fa;
    --transition-speed: 0.3s;
}

/* Light Mode Variables - applied when data-theme is 'light' on stAppViewContainer */
[data-testid="stAppViewContainer"][data-theme="light"] {
    --background-color: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    --text-color: #2d3436;
    --card-background-color: rgba(255,255,255,0.98);
    --border-color: rgba(0,0,0,0.05);
}

/* Dark Mode Variables - applied when data-theme is 'dark' on stAppViewContainer */
[data-testid="stAppViewContainer"][data-theme="dark"] {
    --background-color: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    --text-color: #f8f9fa;
    --card-background-color: rgba(40,40,40,0.95);
    --border-color: rgba(78,205,196,0.15);
}

/* Apply theme variables to the stAppViewContainer and its children */
[data-testid="stAppViewContainer"] {
    background: var(--background-color) !important;
    color: var(--text-color) !important;
    font-family: 'Quicksand', 'Comic Sans MS', cursive;
    transition: background var(--transition-speed) ease, color var(--transition-speed) ease;
}

/* Ensure the main content area inside the app container is transparent and inherits color */
.stApp {
    background: var(--background-color) !important;
    color: var(--text-color) !important;
    transition: background var(--transition-speed) ease, color var(--transition-speed) ease;
}

.main {
    background: transparent !important;
    color: inherit !important;
}

[data-testid="stSidebar"] {
    background: var(--card-background-color) !important;
    color: var(--text-color) !important;
    transition: background var(--transition-speed) ease, color var(--transition-speed) ease;
}

h1, h2, h3 {
    background: linear-gradient(45deg, var(--secondary-color), #ff8e8e);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent !important;
    text-shadow: 2px 2px 4px rgba(255,107,107,0.2);
    transition: all var(--transition-speed) ease;
}

.stTextInput input,
.stTextArea textarea {
    border-radius: 15px !important;
    border: 2px solid var(--primary-color) !important;
    padding: 1rem !important;
    background: var(--card-background-color) !important;
    color: var(--text-color) !important;
    transition: all var(--transition-speed) ease !important;
}

.stButton>button {
    background: linear-gradient(145deg, var(--primary-color), #45b7af) !important;
    color: var(--text-color) !important;
    border-radius: 25px;
    padding: 0.75rem 2.5rem;
    font-weight: 700;
    transition: all var(--transition-speed) cubic-bezier(0.4, 0, 0.2, 1);
    border: none !important;
    box-shadow: 0 4px 6px rgba(78,205,196,0.2);
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(78,205,196,0.4);
}

.stMetric {
    background: var(--card-background-color) !important;
    border-radius: 20px;
    padding: 1.5rem;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    border: 2px solid var(--border-color);
    transition: transform var(--transition-speed) ease;
    color: var(--text-color) !important;
}

.stMetric:hover {
    transform: translateY(-3px);
}

section>div:first-child {
    padding: 2rem;
    background: var(--card-background-color) !important;
    border-radius: 20px;
    margin: 1rem 0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    border: 1px solid var(--border-color);
    color: var(--text-color) !important;
}

div[data-testid="stVerticalBlock"] > div[style*="flex-direction"] {
    padding: 1.5rem;
    background: var(--card-background-color) !important;
    border-radius: 20px;
    margin: 1rem 0;
    border-left: 6px solid var(--primary-color);
    box-shadow: 0 4px 15px rgba(78,205,196,0.1);
    color: var(--text-color) !important;
}

.stMarkdown p {
    padding: 1rem;
    background: var(--card-background-color) !important;
    border-radius: 15px;
    margin: 0.5rem 0;
    border-left: 4px solid var(--secondary-color);
    transition: all var(--transition-speed) ease;
    color: var(--text-color) !important;
}

.stMarkdown p:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(255,107,107,0.15);
}

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;700&display=swap');

/* Home Page Components */
.hero {
    text-align: center;
    padding: 4rem 0;
    background: linear-gradient(135deg, var(backgroun-card-color) 0%, var(--secondary-color) 100%);
    border-radius: 15px;
    margin: 2rem 0;
}

.hero h1 {
    font-size: 3rem;
    color: var(--text-color);
    margin-bottom: 1rem;
}

.hero .logo-emoji {
    font-size: 1.2em;
    vertical-align: middle;
    margin-right: 0.5rem;
}

.hero p {
    font-size: 1.2rem;
    color: var(--text-color);
    opacity: 0.9;
}

.feature-card {
    padding: 1.5rem;
    background: var(--card-background-color);
    border-radius: 12px;
    box-shadow: 0 4px 6px var(--border-color);
    margin: 1rem 0;
    transition: transform var(--transition-speed) ease;
}

.feature-card:hover {
    transform: translateY(-5px);
}

.feature-emoji {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.cta-section {
    text-align: center;
    padding: 3rem 0;
}

.cta-button {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 1rem 2rem;
    border-radius: 25px;
    margin: 0 1rem;
    cursor: pointer;
    font-size: 1.1rem;
    transition: all var(--transition-speed) ease;
}

.cta-button.secondary {
    background: transparent;
    color: var(--primary-color);
    border: 2px solid var(--primary-color);
}

.cta-button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(78,205,196,0.4);
}

/* Header navigation */
.header-container {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 0;
    height: 80px;
}

.header-container [data-testid="column"] {
    display: flex;
    align-items: center;
    height: 100%;
}

.header-container button {
    margin: auto 0;
}

.header-logo {
    font-size: 5.5rem !important;
    background: linear-gradient(45deg, var(--secondary-color), #ff8e8e);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent !important;
    text-shadow: 2px 2px 4px rgba(255, 107, 107, 0.2);
    vertical-align: top;
    margin-right: 0.5rem;
}

.header-auth-buttons button {
    border: 2px solid var(--primary-color) !important;
    color: var(--primary-color) !important;
    background: transparent !important;
    transition: all var(--transition-speed) ease !important;
}

.header-auth-buttons button:hover {
    background: var(--primary-color) !important;
    color: white !important;
}
</style>
"""

def apply_theme_js():
    theme = "dark" if st.session_state.dark_mode_enabled else "light"
    js_code = f"""
    <script>
        var appContainer = window.parent.document.querySelector('[data-testid="stAppViewContainer"]');
        var sidebarContainer = window.parent.document.querySelector('[data-testid="stSidebar"]');

        if (appContainer) {{
            appContainer.setAttribute('data-theme', '{theme}');
            window.parent.document.body.style.setProperty('background', '{'#1a1a1a' if theme == 'dark' else '#f8f9fa'}', 'important');
            window.parent.document.body.style.setProperty('color', '{'#f8f9fa' if theme == 'dark' else '#2d3436'}', 'important');
            appContainer.style.setProperty('background', '{'#1a1a1a' if theme == 'dark' else '#f8f9fa'}', 'important');
            appContainer.style.setProperty('color', '{'#f8f9fa' if theme == 'dark' else '#2d3436'}', 'important');

            if (sidebarContainer) {{
                sidebarContainer.style.setProperty('background', '{'rgba(40,40,40,0.95)' if theme == 'dark' else 'rgba(255,255,255,0.98)'}', 'important');
                sidebarContainer.style.setProperty('color', '{'#f8f9fa' if theme == 'dark' else '#2d3436'}', 'important');
            }}
        }}

        document.body.style.setProperty('background', '{'#1a1a1a' if theme == 'dark' else '#f8f9fa'}', 'important');
        document.body.style.setProperty('color', '{'#f8f9fa' if theme == 'dark' else '#2d3436'}', 'important');
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)
