# 🧠 Mental Health Check-in Bot
This is a Python-based command-line tool to help users check in with their mental health. It allows you to log your mood and its intensity, get simple suggestions based on how you feel, and generate a graph to visualize your mood trends over time.

## ✅ What It Does
- Prompts the user to choose a mood (e.g., Happy, Sad, Stressed).  
- Asks for intensity (1–10 scale).  
- Saves your mood, intensity, and timestamp to a CSV file (`mood_log.csv`).  
- Gives self-care suggestions for negative or high-intensity moods.  
- Plots a graph of mood intensity over time.  
- Everything is managed through a single CLI menu script.

## 🧱 Project Structure
├── checkin.py # Logs mood + intensity and gives suggestions
├── plot_mood.py # Reads mood_log.csv and plots intensity over time
├── main.py # CLI menu to run the bot (log mood or show graph)
├── mood_log.csv # Automatically created to store mood check-ins
├── .gitignore # Ignores system and cache files (e.g., pycache)
└── README.md # This file

## 💻 How to Set Up
1. Clone the Repo  
   ```bash
   git clone https://github.com/fiyinfoluwa-sys/mental-health-checkin-bot.git
   cd mental-health-checkin-bot

## 🕹️ How to Use It
- Run the main CLI menu script:
  ```bash
  python3 main.py
- Then you'll see:
   1. Check in with your mood
   2. View mood graph
   3. Exit


   
