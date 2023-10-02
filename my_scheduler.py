import datetime

class Event:
    def __init__(self, date, description):
        self.date = date
        self.description = description

def add_event(events, date, description):
    event = Event(date, description)
    events.append(event)
    print(f"Event added: {event.description} on {event.date.strftime('%Y-%m-%d %H:%M:%S')}")

def list_events(events):
    if not events:
        print("No events scheduled.")
    else:
        print("Upcoming events:")
        for event in events:
            print(f"{event.date.strftime('%Y-%m-%d %H:%M:%S')} - {event.description}")

def main():
    events = []
    
    while True:
        print("\nEvent Scheduler Menu:")
        print("1. Add Event")
        print("2. List Events")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            date_input = input("Enter event date and time (YYYY-MM-DD HH:MM:SS): ")
            description = input("Enter event description: ")
            try:
                date = datetime.datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')
                add_event(events, date, description)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
        elif choice == '2':
            list_events(events)
        elif choice == '3':
            print("Exiting Event Scheduler.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()
