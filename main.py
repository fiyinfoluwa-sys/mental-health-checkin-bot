import subprocess

def main():
    while True:
        print("\n🧠 Mental Health Check-in Bot Menu")
        print("1. Check in")
        print("2. View mood graph")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == '1': 
            subprocess.run(["python3", "checkin.py"])
        elif choice == '2':
            subprocess.run(["python3", "plot_mood.py"])
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

