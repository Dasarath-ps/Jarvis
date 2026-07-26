# J.A.R.V.I.S. - Voice Command Assistant (Python)

A small voice assistant I built in Python that listens for spoken commands and responds by opening apps, playing music, or setting up my whole workspace. Nothing fancy under the hood - it's basic speech-to-text and text-to-speech wired together - but it was a fun way to learn how these pieces actually connect.

This is an early version. The plan is to eventually rebuild it in React and give it a real AI brain instead of simple keyword matching.

## What it does

- Listens continuously through the microphone for commands
- Talks back using a natural-sounding voice (edge-tts)
- Recognizes speech using Google's speech-to-text API
- Opens a full workspace with one command - browser, VS Code, ChatGPT, and YouTube Music together
- Responds to a few voice shortcuts:
  - "set up workspace" - opens the full dev environment
  - "open YouTube" - opens YouTube
  - "play music" - starts a track on YouTube Music
  - "open WhatsApp" - opens WhatsApp Web
  - "open Telegram" - opens Telegram Web
  - "sleep" or "shut down" - closes the assistant

## Tech used

- speech_recognition (Google's Speech-to-Text API) for listening
- edge-tts combined with mpg123 for speaking
- Python's subprocess module to open and control apps
- Brave Browser for all web-based commands

## What you'll need

- Python packages: SpeechRecognition, pyttsx3, edge-tts
- mpg123 installed on your system
- A working microphone
- Brave Browser and VS Code installed and available from the terminal
- An internet connection, since both the speech recognition and text-to-speech rely on it

Install the Python side with:

```bash
pip install SpeechRecognition pyttsx3 edge-tts
sudo apt install mpg123
```

## How to run it

1. Clone the repo:
   ```bash
   git clone <your-repo-link>
   cd <repo-folder>
   ```
2. Install the requirements listed above.
3. Run the script:
   ```bash
   python jarvis.py
   ```
4. Wait until you hear "Jarvis is online. I am listening for your commands."
5. Say a command, like "set up my workspace" or "play music."
6. Say "shut down" or "sleep" whenever you want it to stop.

One thing to watch out for: the microphone device index is hardcoded in the script. If it doesn't pick up your mic, you'll need to find your device's index and update it yourself.

## Where it's limited

Right now this is just keyword matching, not real understanding. If your sentence contains a trigger word, it runs that function - it doesn't actually interpret what you're asking or hold any context between commands.

## What's next

- Rebuilding this as a React app with a proper interface
- Giving it a real AI brain so it can understand intent instead of just matching words
- Adding more commands and smarter conversation handling over time

## License

Feel free to fork it, learn from it, or build on top of it. Credit is appreciated but not required.
