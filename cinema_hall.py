class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        seats = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[id] = seats

    def book_seats(self, id, seats_to_book):
        if id in self._seats:
            for seat in seats_to_book:
                row, col = seat
                if 0 <= row < self._rows and 0 <= col < self._cols:
                    if self._seats[id][row][col] == 0:
                        self._seats[id][row][col] = 1
                        print(f"Seat at row {row} and column {col} booked successfully.")
                    else:
                        print(f"Seat at row {row} and column {col} is already booked.")
                else:
                    print(f"Invalid seat at row {row} and column {col}")
        else:
            print(f"Show with ID {id} not found.")

    def view_show_list(self):
        print("Shows running:")
        for show in self._show_list:
            print(show)

    def view_available_seats(self, id):
        if id in self._seats:
            print(f"Available seats for show with ID {id}:")
            for row in self._seats[id]:
                print(row)
        else:
            print(f"Show with ID {id} not found.")


hall1 = Hall(3, 4, 1)
hall1.entry_show(1, "Avengers", "5:00 PM")
hall1.entry_show(2, "Spiderman", "8:00 PM")

run = True

while run:
    print("\n1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKETS")
    print("4. Exit")
    choice = input("Enter Option: ")

    if choice == "1":
        hall1.view_show_list()
    elif choice == "2":
        show_id = int(input("Enter show's id: "))
        hall1.view_available_seats(show_id)
    elif choice == "3":
        show_id = int(input("Enter show's id: "))
        row = int(input("Enter seat's row: "))
        col = int(input("Enter seat's col: "))
        hall1.book_seats(show_id, [(row, col)])
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose again.")
