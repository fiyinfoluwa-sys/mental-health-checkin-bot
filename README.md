# 🧘 Mental Health Check-In Bot

**Independent Project | 2025 | Python CLI Application**

The **Mental Health Check-In Bot** is a beginner-friendly Python-based chatbot designed to promote emotional self-awareness and mental well-being through regular check-ins. Initially built as a Command Line Interface (CLI) tool, it engages users in private, supportive conversations using empathy-driven prompts and AI-powered feedback mechanisms. The project aims to serve as a foundation for future mobile or web deployment with interactive UI, sentiment analysis, and condition-specific support (e.g., for PCOS, anxiety, burnout).

---

## 🎯 Project Goals

- Encourage **self-reflection** and **daily emotional tracking**
- Provide gentle nudges or affirmations through friendly dialogue
- Use **natural language processing (NLP)** to analyze responses
- Lay the groundwork for **personalized support suggestions**
- Explore how AI can support mental wellness ethically and accessibly

---

## 🧰 Tech Stack

| Technology         | Description                                              |
|--------------------|----------------------------------------------------------|
| **Python 3.11**     | Core bot logic and CLI interface                         |
| **NLTK / spaCy**    | Text preprocessing and sentiment analysis (WIP)          |
| **OpenAI API**      | Empathetic dialogue generation and tone classification   |
| **SQLite (Planned)**| Store check-in history and emotional trends              |
| **Tkinter/Streamlit (Planned)** | GUI version with enhanced UX               |
| **GitHub Issues/Forms** | Collecting user feedback to refine prompt design     |

---

## ✅ Features

- Daily or on-demand mood check-in
- Free-text journaling with optional AI feedback
- Mood scale selection (1–10) + emotion labeling
- NLP-driven tone detection and journaling sentiment (in progress)
- Prompts tailored to emotional state (e.g., "I'm tired" triggers coping tips)
- Local session-based storage (WIP: persistent tracking with SQLite)

---

## 🔮 Future Improvements

- Deploy to mobile using React Native or Flutter
- Integrate with a larger mental wellness dashboard
- Add symptom-specific modules (e.g., PCOS, ADHD, social anxiety)
- Gentle daily reminders with opt-in check-in scheduling
- Web-based platform with anonymous login or journaling via OAuth

---

## 💡 Sample Use Case

**Scenario:** A student working through midterm stress opens the bot from the terminal.

1. The bot asks: *"Hey there 👋 How are you feeling today on a scale of 1 to 10?"*
2. The user types: `4`
3. The bot replies: *"Thanks for sharing. Want to tell me more about what's going on?"*
4. The user responds: *"I'm feeling burned out. Too many deadlines and not enough sleep."*
5. The bot uses the OpenAI API to analyze tone and detect symptoms of academic burnout.
6. It replies with:
   > "It sounds like you’re under a lot of pressure. You might want to take a short break—maybe even just a walk. Would you like a list of simple stress relievers?"
7. The user types `yes`, and the bot shares 3 short coping strategies.
8. Afterward, the session is saved locally, and a positive affirmation is shared.

---

## 📁 Project Structure
mental-health-checkin-bot/
│
├── bot/
│ ├── prompts.py # Bank of mood-based and journaling prompts
│ ├── analyzer.py # Sentiment and keyword analysis (WIP)
│ ├── affirmations.py # Positive quote/affirmation generator
│ └── main.py # Main chatbot logic and CLI handling
├── tests/ # Unit tests for future reliability
├── README.md # Project documentation
└── requirements.txt # Python dependencies
