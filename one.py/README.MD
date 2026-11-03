🎬 Movie Ticket Booking System
Project Details
Field	Information
Project Name	Movie Ticket Booking System
Name	Ujjwal Mahilang
ERP ID	RU-26-02726
Section	B2
Email	ujjwal.mahilang@rungta.org

PS. No.	25
Programming Language	Python
________________________________________
1. Introduction
The Movie Ticket Booking System is a console-based application developed using Python. It allows users to book movie tickets, cancel bookings, and view the current seat availability in a cinema hall.
The system provides a simple and user-friendly interface through a menu-driven program. It also uses file handling to store booking information permanently, so previously booked seats remain booked even after restarting the program.
2. Features
•	Book Tickets: Users can book one or multiple seats.
•	Cancel Tickets: Users can cancel previously booked seats.
•	Seat Availability: Displays the current status of all seats.
•	Seat Validation: Prevents users from selecting invalid seats.
•	Duplicate Booking Prevention: Prevents booking seats that are already occupied.
•	Automatic Price Calculation: Calculates the total amount based on the number of seats.
•	File Handling: Saves and loads booking details using a text file.
•	Housefull Detection: Displays a message when all seats are booked.
3. Technologies Used
•	Programming Language: Python
•	Module: OS
•	Data Structures: Lists and Dictionaries
•	File Handling: Text File (bookings.txt)
•	Interface: Command-Line Interface (CLI)
4. System Configuration
The cinema hall has the following configuration:
Parameter	Value
Total Rows	3 (A, B, C)
Seats Per Row	5
Total Seats	15
Ticket Price	₹200 per seat
Storage File	bookings.txt
5. Menu Options
When the program runs, the following menu is displayed:
--- Movie Ticket Booking System ---
1. Book
2. Cancel
3. Seatmap
4. Exit
Enter option:
•	Option 1 – Book: Books the selected seat or seats.
•	Option 2 – Cancel: Cancels an existing booking.
•	Option 3 – Seatmap: Displays booked and available seats.
•	Option 4 – Exit: Terminates the program.
6. Seat Map Representation
The seat map uses the following symbols:
•	X = Booked Seat
•	_ = Available Seat
Example:
RowA: XX___
RowB: X____
RowC: _____
Seats left: 12
7. How to Run the Project
Step 1: Install Python on your computer.
Step 2: Save the Python source code in a file named:
movie_booking.py
Step 3: Open the terminal or command prompt in the project folder.
Step 4: Run the following command:
python movie_booking.py
Step 5: Select an option from the menu and follow the instructions.
8. Sample Output
Booking a Ticket
--- Movie Ticket Booking System ---
1. Book
2. Cancel
3. Seatmap
4. Exit

Enter option: 1
Seat: A1
Name: Ujjwal
Seat A1 booked for Ujjwal. Amount:200
Booking Multiple Tickets
Enter option: 1
Seat: A2,A3
Name: Rahul
Seats A2,A3 booked for Rahul. Amount:400
Displaying Seat Map
Enter option: 3

RowA: XXX__
RowB: _____
RowC: _____
Seats left: 12
Cancelling a Ticket
Enter option: 2
Seat: A1
Seat A1 cancelled.
9. File Handling
The project uses a text file named bookings.txt to store booking information.
Example:
A1:Ujjwal
A2:Rahul
A3:Rahul
•	The load_bookings() function reads previously saved bookings.
•	The save_bookings() function writes current booking details into the file.
•	The os.path.exists() function checks whether the file exists.
This ensures that booking information is maintained even after the program is closed.
10. Python Concepts Used
1.	Variables and Constants
2.	Lists and Dictionaries
3.	User-Defined Functions
4.	Conditional Statements
5.	For and While Loops
6.	String Manipulation
7.	File Handling
8.	Input Validation
9.	Data Management
10.	Modular Programming
11. Advantages
•	Simple and easy to use.
•	Supports single and multiple ticket bookings.
•	Prevents duplicate seat bookings.
•	Provides automatic ticket price calculation.
•	Maintains booking records permanently using file handling.
•	Allows users to cancel tickets and check seat availability.
12. Limitations
•	The system is console-based and does not have a graphical user interface.
•	It supports only 15 seats.
•	It does not include online payment facilities.
•	It does not support multiple movies or show timings.
•	It does not include customer authentication.
13. Future Improvements
•	Add a graphical user interface (GUI).
•	Integrate online payment methods.
•	Add multiple movies and show timings.
•	Introduce customer login and registration.
•	Generate digital movie tickets.
•	Use a database such as MySQL or SQLite.
14. Conclusion
The Movie Ticket Booking System is a basic Python application that demonstrates the practical implementation of programming concepts such as functions, dictionaries, lists, loops, conditional statements, and file handling.
It provides an efficient way to manage movie ticket bookings, cancellations, and seat availability. This project helps in understanding how real-world booking systems work using basic Python programming.
________________________________________
Developed by: Ujjwal Mahilang
ERP ID: RU-26-02726
Section: B2
Email: ujjwal.mahilang@rungta.org
Mentored by: Mr. Satyaprakash Sethy
Github: @SATYAPRAKASHSETHY
Role: Python mentor/ Technical guide
