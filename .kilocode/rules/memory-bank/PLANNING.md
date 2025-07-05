# Project Planning: Cadence for Teen Well-being

## 2. Project Phases

### Phase 1: Foundation & Core Mood Detection (Approx. 6 Hours)

* **Objective:** To set up the development environment, build the foundational UI, and implement the initial mood detection logic.
* **Key Activities:**
  * Set up Python environment and install Streamlit.
  * Create the main Streamlit application file.
  * Design and implement a basic UI with a text input area for journaling and placeholder sections for output.
  * Implement initial UI styling for a soft, fun, happy, and inviting aesthetic (color palette, fonts).
  * Install `nltk` and download the `vader_lexicon`.
  * Develop a function to process text input using VADER sentiment analysis.
  * Map VADER scores to simplified mood categories (e.g., "Positive," "Negative," "Neutral," "Stressed," "Happy").

### Phase 2: Music Recommendation & Initial Nudges (Approx. 8 Hours)

* **Objective:** To integrate mood-based music recommendations and implement basic digital wellness nudges.
* **Key Activities:**
  * Curate 3-5 pre-defined, teen-appropriate music playlists directly within Python code.
  * Develop logic to map the detected mood from Phase 1 to the appropriate curated playlist.
  * Display the recommended playlist title and a few sample song names in the UI.
  * Implement a toggle button for "Study Mode" or "Mindful Break" in the UI.
  * When "Study Mode" is active, display a placeholder message indicating paused notifications.
  * Hardcode a variety of age-appropriate, human-centric activity suggestions.
  * Implement logic to display these suggestions based on the activated mode or general user interaction.
  * Add a simple user feedback button (e.g., "Thumbs Up/Down") for music recommendations.

### Phase 3: UI Refinement & Presentation Prep (Approx. 6 Hours)

* **Objective:** To refine the user interface, ensure all features are well-integrated, and prepare for the project demonstration.
* **Key Activities:**
  * Refine the language and tone of all AI responses and nudges to be empowering and teen-friendly.
  * Enhance the overall UI/UX to ensure clarity, intuitiveness, and adherence to the "soft, fun, happy, inviting" aesthetic.
  * Test all implemented features to ensure they work as intended.
  * Prepare presentation slides covering the problem, solution, MVP features, and future enhancements.
  * Practice the live demonstration of the MVP, ensuring a smooth flow.
  * Finalize all project documentation files.

## 3. Milestones

* **Hour 2:** Basic Streamlit UI scaffolded and styled.
* **Hour 6:** Mood detection via VADER sentiment analysis implemented and integrated with text input.
* **Hour 10:** Mood-based music playlist recommendation logic complete and displayed.
* **Hour 14:** "Study Mode" / "Mindful Break" toggle and hardcoded activity suggestions implemented.
* **Hour 17:** UI/UX refinement complete, all core MVP features working smoothly.
* **Hour 20:** Presentation and demo prepared and ready.

## 4. Risks & Mitigation

* **Risk:** Sentiment analysis accuracy with informal teen language.
  * **Mitigation:** Use VADER, which is generally robust for social media text; keep initial mood mapping simple (e.g., broadly positive/negative/neutral) rather than attempting highly nuanced emotion detection for the MVP.
* **Risk:** Over-scoping features for a 20-hour hackathon.
  * **Mitigation:** Strict adherence to MVP prioritization. De-prioritize complex features like full ML training, external API integrations (beyond basic data if time permits), and system-level interactions.
* **Risk:** Technical issues with Streamlit or NLTK setup.
  * **Mitigation:** Pre-emptively set up the environment and install libraries. Have backup plans or simplified alternatives if specific libraries cause significant issues.
* **Risk:** Difficulty in curating relevant music playlists or activity suggestions.
  * **Mitigation:** Rely on pre-defined, generally appealing categories for music and common, accessible activities.
* **Risk:** Presentation time management.
  * **Mitigation:** Practice the demo multiple times, ensure clear and concise articulation of key points.

## 5. Resources

* **Libraries:** Streamlit, NLTK
* **Tools:** Python, Code Editor (VS Code recommended)
* **Documentation:** Streamlit documentation, NLTK documentation
* **Design Inspiration:** Examples of well-designed, teen-friendly apps for UI/UX ideas.
