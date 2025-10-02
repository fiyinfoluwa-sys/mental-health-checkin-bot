import csv

def fix_mood_log(file_path="mood_log.csv"):
    fixed_rows = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                # Add default intensity
                row.append("5")
            if len(row) == 3:
                fixed_rows.append(row)

    with open(file_path, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(fixed_rows)

    print("mood_log.csv has been fixed.")

if __name__ == "__main__":
    fix_mood_log()

