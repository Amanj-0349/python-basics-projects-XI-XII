import  sqlite3

# Database setup
conn = sqlite3.connect('railway_reservationdb')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS passengers (
    passenger_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY,
    passenger_id INTEGER,
    source_station TEXT NOT NULL,
    destination_station TEXT NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES passengers (passenger_id)
)
''')
conn.commit()

def create_passenger(name, age, gender):
    cursor.execute("INSERT INTO passengers (name, age, gender) VALUES (?, ?, ?)", (name, age, gender))
    conn.commit()
    return cursor.lastrowid

def create_reservation(passenger_id, source_station, destination_station):
    cursor.execute("INSERT INTO reservations (passenger_id, source_station, destination_station) VALUES (?, ?, ?)", (passenger_id, source_station, destination_station))
    conn.commit()
    return cursor.lastrowid

def display_reservations():
    cursor.execute("SELECT passengers.name, reservations.source_station, reservations.destination_station FROM passengers JOIN reservations ON passengers.passenger_id = reservations.passenger_id")
    reservations = cursor.fetchall()
    for reservation in reservations:
        print(f"Passenger: {reservation[0]}, Source: {reservation[1]}, Destination: {reservation[2]}")

while True:
    print("\nRailway Reservation System")
    print("1. Create Passenger")
    print("2. Create Reservation")
    print("3. Display Reservations")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        gender = input("Enter passenger gender: ")
        passenger_id = create_passenger(name, age, gender)
        print(f"Passenger created with ID: {passenger_id}")

    elif choice == '2':
        passenger_id = int(input("Enter passenger ID: "))
        source_station = input("Enter source station: ")
        destination_station = input("Enter destination station: ")
        reservation_id = create_reservation(passenger_id, source_station, destination_station)
        print(f"Reservation created with ID: {reservation_id}")

    elif choice == '3':
        display_reservations()

    elif choice == '4':
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
