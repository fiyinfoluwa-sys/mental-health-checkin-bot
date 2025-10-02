import os
from dotenv import load_dotenv
import openai

# Load .env file
load_dotenv()

# Get API key
openai.api_key = os.getenv("OPENAI_API_KEY")

import csv
from datetime import datetime

# Define the mood options
moods = [
    "Happy",
    "Sad",
    "Anxious",
    "Angry",
    "Neutral",
    "Excited",
    "Tired",
    "Stressed"
]

def give_suggestion(mood, intensity):
    suggestions = {
        "Happy": "Great! Keep spreading the good vibes.",
        "Sad": "It's okay to feel sad. Maybe try talking to a friend or journaling.",
        "Anxious": "Try deep breathing exercises or a short walk to calm your mind.",
        "Angry": "Take some time to cool down and consider writing your feelings down.",
        "Neutral": "Sometimes, just taking a moment to relax can help.",
        "Excited": "Awesome! Channel that energy into something creative.",
        "Tired": "Make sure to get enough rest and hydrate.",
        "Stressed": "Try a short meditation or mindfulness exercise."
    }
    
    if intensity >= 7:
        print("\nSuggestion based on your mood:")
        print(suggestions.get(mood, "Take care of yourself today!"))
    else:
        print("\nThanks for sharing. Remember to take breaks and breathe!")

def log_mood(mood, intensity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('mood_log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, mood, intensity])
    print(f"\nMood '{mood}' with intensity {intensity} recorded at {timestamp}.")

def main():
    print("Welcome to your Mental Health Check-in Bot!")
    print("How are you feeling today? Choose a mood from the list below:")
    for i, mood in enumerate(moods, 1):
        print(f"{i}. {mood}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your mood: "))
            if 1 <= choice <= len(moods):
                mood = moods[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(moods)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            intensity = int(input("On a scale of 1 (low) to 10 (high), how intense is this feeling? "))
            if 1 <= intensity <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    log_mood(mood, intensity)
    give_suggestion(mood, intensity)

    print("\nThank you for checking in. Take care!")

if __name__ == "__main__":
    main()

