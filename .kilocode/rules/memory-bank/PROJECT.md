# Project: Cadence for Teen Well-being

## 1. Project Overview

"Cadence" is an AI-powered digital companion designed to support the mental well-being of teenagers navigating the complexities of their digital lives. It aims to address challenges such as digital overload, mental health impacts from social comparison, sleep disruption, fragmented attention, and the erosion of authentic connections. The core of the solution involves mood-adaptive music recommendations and personalized nudges for healthier digital habits and fostering real-world connections.

## 2. Goals

* To develop an AI-powered companion that understands a teenager's emotional state.
* To intelligently recommend music to support their mental well-being.
* To guide teenagers toward healthier digital habits through personalized "digital boundaries."
* To encourage and facilitate meaningful real-world connections.
* To provide an empowering, teen-centric platform that promotes self-regulation over restriction.

## 3. Scope

### In-Scope

* **Adaptive Mood Detection:** Inferring user mood via journal entries/text input using NLP sentiment analysis.
* **Music Recommendation:** Curating personalized music playlists based on inferred mood (initial focus on pre-defined playlists).
* **Digital Detox Nudges:** Implementing a "Study Mode" or "Mindful Break" feature to simulate notification blocking and offer pre-defined human-centric activity suggestions.
* **User Feedback Mechanism:** Simple "thumbs up/down" for music recommendations.
* **Teen-Centric UI/UX:** Design focused on being soft, fun, happy, inviting, and empowering.
* **MVP Development:** Focusing on core functionalities for a 20-hour hackathon timeframe using Streamlit and Python.

### Out-of-Scope

* Passive behavior monitoring (e.g., app usage tracking beyond self-reported data).
* Full reinforcement learning loop for dynamic adaptation in the MVP.
* Complex habit learning and highly adaptive, dynamic boundary setting.
* Comprehensive social accountability network with real-time peer monitoring.
* Extensive, automated music analysis (beyond initial self-tagging concept).
* Direct system-level notification blocking or app usage restriction.
* Full parental consent integration and advanced parental controls.
* Complex API integrations beyond basic data fetching (e.g., full Spotify playback).

## 4. Key Deliverables

* A functional Minimum Viable Product (MVP) demonstrating:
  * Text input for journaling.
  * Sentiment analysis of journal entries.
  * Mood-based music playlist recommendations (from pre-defined lists).
  * A "Study Mode" / "Mindful Break" toggle with simulated notification pausing.
  * Display of human-centric activity suggestions.
  * A simple user feedback mechanism for recommendations.
* A presentation outlining the problem, solution, MVP features, and future enhancements.
* Project documentation (PROJECT.md, PLANNING.md, TASK.md, README.md).

## 5. Technology Stack

* **Frontend/UI:** Streamlit (Python library for rapid web app development)
* **Backend/Logic:** Python
  * **Sentiment Analysis:** `nltk.sentiment.vader`
* **Data Storage:** Simple JSON files or Python dictionaries (for MVP, temporary user input)

## 6. Team and Roles

* **Role 1: Project Lead/Full-stack Developer (You)** - Overall project management, core logic implementation, UI development, presentation.

## 7. Development Phases

* **Phase 1: Foundation & Core Mood Detection**
* **Phase 2: Music Recommendation & Initial Nudges**
* **Phase 3: UI Refinement & Presentation Prep**

## 8. Success Metrics

* Successful demonstration of the MVP's core functionalities (mood detection, music recommendation, digital detox nudge).
* Positive feedback on the intuitiveness and teen-centric design of the UI.
* Clear articulation of the problem and the value proposition during the presentation.
* Completion of planned MVP features within the 20-hour hackathon timeframe.
