# Cadence for Teen Well-being

Cadence is an AI-powered digital companion designed to support the mental well-being of teenagers by offering mood-adaptive music recommendations and personalized guidance towards healthier digital habits and stronger real-world connections.

## Features

* **Mood-Adaptive Music Recommendations:** Analyzes text input to understand a teenager's emotional state and recommends personalized music playlists to match or shift their mood.
* **Digital Detox Nudges:** Provides empowering suggestions for taking mindful breaks from digital devices and encourages engagement in human-centric activities.
* **"Study Mode" / "Mindful Break" Feature:** A user-activated toggle that simulates pausing digital notifications to aid focus and promote offline engagement.
* **Teen-Centric Design:** All interactions, language, and design elements are tailored to resonate with teenagers, fostering a supportive and empowering user experience.
* **Simple User Feedback:** Allows users to provide basic feedback on music recommendations to help refine future suggestions (conceptual for MVP).

## Usage

To run the Cadence application (MVP):

1. **Clone the repository:**

    ```bash
    git clone [your-repository-link]
    cd cadence-app
    ```

2. **Set up the Python environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (You will need to create a `requirements.txt` file containing `streamlit` and `nltk`. Alternatively, run `pip install streamlit nltk`.)
4. **Download NLTK data:**
    Open a Python interpreter or add the following to your `app.py` file:

    ```python
    import nltk
    nltk.download('vader_lexicon')
    ```

5. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    (Replace `app.py` with the actual name of your main Streamlit application file.)

Once running, you will see a web interface where you can:

* Enter text about your feelings or day in the journaling section.
* Receive a mood-based music playlist recommendation.
* Toggle "Study Mode" / "Mindful Break" to see activity suggestions.

## Development Setup

This project is designed for rapid prototyping during a hackathon. The MVP focuses on demonstrating core concepts using Streamlit for the frontend and Python for backend logic.

## Technologies Used

* **Streamlit:** For building the interactive web user interface.
* **Python:** The primary programming language for all logic.
* **NLTK (Natural Language Toolkit):** Specifically, `nltk.sentiment.vader` for sentiment analysis of text input.

Contributions are welcome! If you have suggestions for improvements or encounter issues, please open an issue or submit a pull request.

## License

This project is open-sourced under the MIT License.
