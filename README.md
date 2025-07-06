# Cadence

## Project for Sonoma Sonoma Hacks 4.0 Hackathon

Cadence is a smart wellness companion that uses AI and music to help teens understand and manage their emotions. 
It starts by analyzing journal entries and listening habits to detect your mood. 
Then, it recommends music that either reflects how you're feeling or gently guides you toward a better emotional state. 
Cadence also supports digital balance—helping teens set healthy screen time boundaries, avoid digital overload, and reconnect with the rhythm of real life.
It also suggests offline activities and lets users invite friends or family as accountability partners for support.

## Built With

- python
- streamlit
- spotify
- vader-sentiment-analyzer

## Installation

### 1. Create virtual environment

```bash
python -m venv venv  
```

### 2. Activate virtual environment

```bash
venv\Scripts\activate
```

### 3. Install requirements

```bash
pip -r requirements.txt
```

## Creating User Credentials for Spotify

### 1. Goto [Spotify](https://developer.spotify.com/)

### 2. Log in to the dashboard using your Spotify account.

### 3. Create an app and select "Web API" for the question asking which APIs you are planning to use. 
 
Once you have created your app, you will have access to the app credentials. 

### 4. Make a copy of the .emv-example file and rename to .env

### 5. Change the credentials in the .env file

## Running the App

```python
python -m streamlit run src/app.py
```

