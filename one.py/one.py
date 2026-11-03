# NAME-UJJWAL MAHILANG
# ERP-RU-26-02726
# SECTION-B2
# EMAIL-ujjwal.mahilang@rungta.org
# PS. no- 25
# TOPIC- MOVIE TICKET BOOKING SYSTEM




import os  # Used to check if bookings.txt file exists

# --- Configuration Constants ---
ROWS = ['A', 'B', 'C']  # Total 3 rows in the hall
COLS = [1, 2, 3, 4, 5]  # 5 seats per row
PRICE = 200  # Price per seat
FILE_NAME = "bookings.txt"  # File to store bookings permanently

# --- 2D List Concept using Dictionary ---
# Each row (A,B,C) has a list of 5 seats
# None means empty seat, otherwise stores customer name
seat_map = {r: [None]*5 for r in ROWS}

def is_valid_seat(seat):
    """Validates if seat code is correct (e.g., A1 to C5). Invalid e.g., Z9"""
    if len(seat) < 2:
        return False
    row = seat[0].upper()  # First character is Row
    col_part = seat[1:]  # Remaining part is Column number
    if row not in ROWS or not col_part.isdigit():
        return False
    if int(col_part) not in COLS:
        return False
    return True

def get_status(seat):
    """Returns current status of a seat - None or booked name"""
    r = seat[0].upper()
    c = int(seat[1:]) - 1  # Convert to 0-based index for list
    return seat_map[r][c]

def load_bookings():
    """Loads old bookings from bookings.txt at program start - File Handling"""
    if not os.path.exists(FILE_NAME):
        return  # No file means fresh start
    with open(FILE_NAME, 'r') as f:
        for line in f:
            if ':' in line:  # Expected format: A1:Aman
                seat, name = line.strip().split(':', 1)
                seat = seat.upper()
                if is_valid_seat(seat):
                    r = seat[0]
                    c = int(seat[1:]) - 1
                    seat_map[r][c] = name.strip()

def save_bookings():
    """Saves all bookings to file after every book/cancel operation"""
    with open(FILE_NAME, 'w') as f:
        for r in ROWS:
            for i, name in enumerate(seat_map[r]):
                if name:  # Save only booked seats
                    f.write(f"{r}{i+1}:{name}\n")

def seats_left():
    """Counts number of empty seats left"""
    return sum(1 for r in ROWS for s in seat_map[r] if s is None)

def book_seats(seat_input, name):
    """Books single or multiple seats (e.g., A2,A3)"""
    # Split comma separated seats and normalize to uppercase
    seats = [s.strip().upper() for s in seat_input.split(',') if s.strip()]
    
    # --- Validation Phase ---
    for s in seats:
        if not is_valid_seat(s):
            # Handles TestCase 3(b) - Invalid seat
            print("Invalid seat. Rows are A to C and seat numbers 1 to 5.")
            return
        if get_status(s) is not None:
            # Handles TestCase 3(a) - Already booked
            print(f"Seat {s} is already booked.")
            return

    # --- Booking Phase ---
    for s in seats:
        r, c = s[0], int(s[1:])-1
        seat_map[r][c] = name

    save_bookings()  # Persist to file
    amount = len(seats) * PRICE  # Calculate total amount

    # Output as per Test Cases
    if len(seats) == 1:
        print(f"Seat {seats[0]} booked for {name}. Amount:{amount}")  # TestCase 1
    else:
        print(f"Seats {','.join(seats)} booked for {name}. Amount:{amount}")  # TestCase 4

    # Handles TestCase 2 - Housefull check
    if seats_left() == 0:
        print("Seats left: 0")
        print("Show is now housefull.")

def cancel_booking(seat_input):
    """Cancels a booked seat"""
    s = seat_input.strip().upper()
    if not is_valid_seat(s):
        print("Invalid seat. Rows are A to C and seat numbers 1 to 5.")
        return
    if get_status(s) is None:
        print(f"Seat {s} is not booked.")
        return
    r, c = s[0], int(s[1:])-1
    seat_map[r][c] = None  # Make seat empty
    save_bookings()
    print(f"Seat {s} cancelled.")

def display_seatmap():
    """Displays seat map: X = Booked, _ = Empty - For TestCase 4(b)"""
    for r in ROWS:
        line = "".join("X" if s else "_" for s in seat_map[r])
        print(f"Row{r}: {line}")
    print(f"Seats left: {seats_left()}")

def main():
    """Main menu function - Bare Minimum Requirement"""
    load_bookings()  # Load at start
    while True:
        print("\n--- Movie Ticket Booking System ---")
        print("1. Book")    # Book seats
        print("2. Cancel")  # Cancel seats
        print("3. Seatmap") # Show seat map
        print("4. Exit")
        ch = input("Enter option: ").strip()
        if ch == '1':
            seat = input("Seat: ").strip()
            name = input("Name: ").strip()
            book_seats(seat, name)
        elif ch == '2':
            seat = input("Seat: ").strip()
            cancel_booking(seat)
        elif ch == '3':
            display_seatmap()
        elif ch == '4':
            break
        else:
            print("Invalid option.")

# Program entry point
if __name__ == "__main__":
    main()