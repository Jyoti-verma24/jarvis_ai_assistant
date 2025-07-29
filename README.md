# 🤖 Jarvis – Web-based AI Voice Assistant with Flask

Jarvis is a powerful, browser-based virtual assistant that listens to your voice commands, responds intelligently using AI, and performs tasks such as playing music, summarizing content, answering questions, and more — all through a stylish, responsive, and secure web interface.

This project blends the power of modern web technologies with Python's AI capabilities to deliver a fully functional assistant experience – ideal for personal projects, AI portfolios, and student research showcases.

---

## ✨ Key Features

- 🔐 **User Authentication System**
  - Register any username, fixed password (`jarvis123`)
  - Dynamic username display after login

- 🗣️ **Voice Command Input via Browser**
  - Uses JavaScript for real-time microphone input
  - Sends input to backend for AI processing

- 🧠 **AI-Powered Replies**
  - Gemini or GPT integrated
  - Smart replies based on user's query

- 🎵 **Music Player**
  - Voice-enabled song listing
  - Plays selected music from preloaded list

- 🎨 **Modern UI + Animation**
  - Bootstrap 5 styling
  - Boomerang bounce animations for character
  - Responsive, mobile-friendly interface

- 🧩 **Modular Code**
  - Assistant logic in `main.py`
  - Music config in `musiclibrary.py`
  - Flask routing in `app.py`

---

## 🏗️ Tech Stack

| Layer        | Tools/Frameworks                                 |
|--------------|--------------------------------------------------|
| 🧠 AI Engine | Gemini API (Google), OpenAI (optional fallback)   |
| 🎙 Voice     | JavaScript `webkitSpeechRecognition`, pyttsx3     |
| 🖥 Backend   | Python 3, Flask                                   |
| 🎨 Frontend | HTML5, CSS3, Bootstrap 5, JavaScript               |
| 📦 Storage   | JSON (for users), session cookies (Flask)         |

---

## 📁 Folder Structure

jarvis-project/
│
├── app.py # Flask server logic
├── main.py # Voice assistant core
├── musiclibrary.py # Song list and URL mapping
├── users.json # JSON-based user storage
│
├── templates/ # HTML files
│ ├── login.html
│ ├── dashboard.html
│ └── register.html # Optional if enabled
│
├── static/
│ ├── style.css # Custom CSS + animations
│ └── (JS, icons, etc.)
│
├── requirements.txt
└── README.md

---

## 🔐 Login Credentials (Default)

- ✅ **Username**: Any name (saved dynamically)
- ✅ **Password**: `jarvis123`

---

🙋‍♀️ Author
Jyoti Verma
GitHub: Jyoti-verma24





