# Library Management System

books = []
serial_number = 1


def add_book():
    global serial_number

    print("\n--- Enter Book Details ---")
    book = {}

    book["SL No"] = serial_number
    book["Book ID"] = input("Enter Book ID: ")
    book["Book Name"] = input("Enter Book Name: ")
    book["Author"] = input("Enter Author Name: ")
    book["Publisher"] = input("Enter Publisher Name: ")
    book["Year"] = input("Enter Published Year: ")
    book["Genre"] = input("Enter Genre: ")
    book["Quantity"] = input("Enter Quantity: ")
    book["Availability"] = input("Enter Availability Status: ")

    books.append(book)
    serial_number += 1

    print("\nBook Details Added Successfully!")
    print("Generated SL No:", book["SL No"])


def display_books():
    if not books:
        print("\nNo Book Records Found!")
    else:
        print("\n--- LIBRARY BOOK DETAILS ---")

        for book in books:
            for key, value in book.items():
                print(key, ":", value)
            print()


def search_book():
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["Book ID"] == book_id:
            print("\nBook Record Found!")

            for key, value in book.items():
                print(key, ":", value)

            return

    print("\nBook Record Not Found!")


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book Details")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")