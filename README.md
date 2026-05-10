# 🤖 Jarvis — Desktop Voice Assistant

A Python-powered desktop voice assistant that wakes up on your command, understands natural language, and responds with AI-generated answers or built-in actions like opening websites, playing music, and fetching the news.

---

## ✨ Features

- 🎙️ **Wake-word detection** — listens continuously for *"Jarvis"*
- 🧠 **AI responses** via OpenAI GPT-3.5-turbo for open-ended questions
- 🔊 **Text-to-Speech** using Google TTS (gTTS) + pygame playback
- 🌐 **Built-in commands** for websites, news, and music
- 🖥️ **GUI mode** (Tkinter) with live transcription and response display
- ⌨️ **CLI mode** for lightweight terminal use

---

## 🗂️ Project Structure

```
jarvis/
├── gui.py            # Tkinter GUI entry point
├── main.py           # Command-line entry point
├── musiclibrary.py   # Dictionary of song names → URLs
└── README.md
```

---

## 🛠️ Requirements

- **Python 3.8+**
- A working **microphone**
- An **internet connection** (for Google STT, gTTS, and OpenAI)
- A valid **OpenAI API key** from [platform.openai.com](https://platform.openai.com)

### Install Dependencies

```bash
pip install speechrecognition pyttsx3 gtts pygame openai
```

| Package            | Purpose                          |
|--------------------|----------------------------------|
| `speechrecognition`| Microphone input & Google STT    |
| `gtts`             | Google Text-to-Speech (primary)  |
| `pygame`           | Audio playback for gTTS output   |
| `openai`           | GPT-3.5-turbo AI responses       |
| `pyttsx3`          | Offline TTS (legacy fallback)    |
| `tkinter`          | GUI framework (built-in)         |

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone (repository url)
cd jarvis
```

### 2. Install dependencies

```bash
pip install speechrecognition pyttsx3 gtts pygame openai
```

### 3. Add your OpenAI API key

Open `gui.py` and `main.py` and replace the placeholder:

```python
# Find this line:
api_key="abcd1234"

# Replace with your actual key:
api_key="sk-..."
```

> **Security tip:** Use environment variables instead of hardcoding your key:
> ```python
> import os
> api_key = os.getenv("OPENAI_API_KEY")
> ```
> Then set the variable in your shell: `export OPENAI_API_KEY="sk-..."`

### 4. Populate the music library

Edit `musiclibrary.py` with your songs:

```python
music = {
    "song name": "https://youtube.com/watch?v=...",
    "another song": "https://youtube.com/watch?v=...",
}
```

---

## 🚀 Running Jarvis

### GUI Mode (Recommended)

```bash
python gui.py
```

Click **Start Listening**, say **"Jarvis"** to activate, then speak your command.

### Command-Line Mode

```bash
python main.py
```

Recognized speech and responses are printed to the terminal. Press `Ctrl+C` to exit.

---

## 🗣️ Built-in Voice Commands

| Voice Command              | Action                          |
|----------------------------|---------------------------------|
| `"Open Google"`            | Opens google.com                |
| `"Open Facebook"`          | Opens facebook.com              |
| `"Open YouTube"`           | Opens youtube.com               |
| `"Open Instagram"` / `"Open Insta"` | Opens instagram.com  |
| `"News"`                   | Opens BBC News                  |
| `"Play <song name>"`       | Plays song from music library   |
| Any other command          | Routed to OpenAI for AI reply   |

---

## 🔄 How It Works

```
1. Wake Word    → Continuously listens for "Jarvis" (2s windows)
2. Activation   → Speaks "Yaa?" and opens a longer listening window
3. Recognition  → Sends audio to Google Speech Recognition
4. Routing      → Matches built-in commands or forwards to OpenAI
5. Response     → Speaks reply aloud via gTTS + pygame
6. GUI Update   → Refreshes transcription and response panels (gui.py only)
```

---

## ⚠️ Known Limitations

- API key is hardcoded by default — use `os.getenv` for security
- gTTS requires an internet connection; pyttsx3 is available as an offline fallback but not wired into the GUI
- Rapid back-to-back responses may conflict on `temp.mp3` writes
- `musiclibrary.py` must be populated manually by the user
- GUI error messages in the status bar may be cryptic

