
# 🧠 Jarvis AI Assistant

**Jarvis** is a smart, voice-enabled AI Assistant built using **Python**, **Flask**, and the **Gemini API**. It responds to your voice commands, plays music, generates summaries, and interacts with you in a human-like way — all through a modern web-based interface.

---

## 🔥 Features

- 🎙️ **Voice Recognition**: Speak commands directly into your browser
- 🤖 **AI Responses**: Uses Gemini API to generate intelligent replies
- 🎵 **Music Playback**: Search and play songs from a built-in library
- 🌐 **Web Interface**: Login system with a modern dashboard
- 📝 **Summary Generator**: Create topic/URL-based summaries with image generation
- 📄 **PDF Download**: Save generated summaries as styled PDFs
- 🧠 **Prompt Engineering**: Smart prompts dynamically built from your voice
- 🧪 **Hugging Face API**: For AI-generated summary images

---

## 🧠 Prompt Engineering Concepts Used

This project applies Prompt Engineering techniques:
- Voice commands are captured and converted into **text prompts**.
- Prompts are customized dynamically based on task (e.g., summarization, chatting).
- Gemini API uses these crafted prompts to generate **context-aware** responses.
- Used **multi-function prompt templates** to handle different AI functions (summary, question-answering, assistant replies).

---

## 📁 Project Structure

jarvis_ai_assistant/
├── app.py
├── main.py
├── musiclibrary.py
├── users.json
├── requirements.txt
├── static/
│ └── mic.gif
├── templates/
│ ├── login.html
│ └── dashboard.html
└── README.md

## 🧪 Technologies Used
- Python
- Flask
- SpeechRecognition
- pyttsx3 / gTTS
- Gemini API
- Bootstrap 5 (Frontend)

## 💡 Prompt Engineering Concepts Used
- Natural language instructions for Gemini API
- Voice input converted to prompt dynamically
- Prompt templates for summarization and search


## 🙋‍♀️ Author
**Jyoti Verma**



