from datetime import datetime
import csv

# Ask the user how they're feeling
mood = input("How are you feeling today? (1 = 😞, 10 = 😄) ")

# Get the current date and time
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Save it to mood_log.csv
with open("mood_log.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([timestamp, mood])

print("✅ Your mood has been logged. Take care! 💚")

