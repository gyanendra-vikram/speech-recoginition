# Audio Translation and Speech Playback Tool

This Python application performs the following tasks:

1. **Audio Recording** (optional).
2. **Speech Recognition** from a `.wav` file.
3. **Language Translation** using `translate-cli`.
4. **Speech Output** using `pyttsx3`.

---

## Features

- Record audio via microphone (`sounddevice` and `wavio`).
- Recognize speech using Google’s Speech Recognition API.
- Translate text from one language to another using `translate-cli`.
- Read out translated text using text-to-speech.

---

## Requirements

### Python Packages

Install the following Python packages:

```bash
pip install sounddevice wavio SpeechRecognition pyttsx3

