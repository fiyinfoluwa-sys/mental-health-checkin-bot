import csv
from datetime import datetime
import matplotlib.pyplot as plt

def plot_mood_trends():
    dates = []
    intensities = []

    try:
        with open('mood_log.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                timestamp_str, mood, intensity_str = row
                date = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                intensity = int(intensity_str)

                dates.append(date)
                intensities.append(intensity)
    except FileNotFoundError:
        print("No mood log found. Please log your mood first.")
        return
    except Exception as e:
        print("Error reading mood log:", e)
        return

    if not dates:
        print("No mood data to plot.")
        return

    plt.figure(figsize=(10,5))
    plt.plot(dates, intensities, marker='o', linestyle='-', color='blue')
    plt.title('Mood Intensity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Intensity (1-10)')
    plt.ylim(0, 10)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_mood_trends()

