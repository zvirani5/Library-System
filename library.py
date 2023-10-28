'''
CS1026a 2023
Assignment 02
Zanan Virani
zvirani5
10/19/2023
'''

'''
This code is a library system where the user can add, return, borrow, and list books in the system.
'''

# to start program
def start():
    # store books in library
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    # store books that are unavailable.
    borrowedISBNs = []

    while True:
        printMenu()
        selection = getSelection()   # Already returned in lowercase form.

        if selection in "1a":
            addNewBook(allBooks)
        elif selection in "2r":
            borrowBook(allBooks, borrowedISBNs)
        elif selection in "3t":
            returnBook(allBooks, borrowedISBNs)
        elif selection in "4l":
            listBooks(allBooks, borrowedISBNs)
        else:
            print("\n$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            listBooks(allBooks, borrowedISBNs)
            break        # end the program if "x" or "5" is selected.

# Print the menu at the start of every iteration.
def printMenu():
    print("\n" + "#" * 23)
    print("1: (A)dd a new book.")
    print("2: Bo(r)row books.")
    print("3: Re(t)urn a book.")
    print("4: (L)ist all books.")
    print("5: E(x)it.")
    print("#" * 23 + "\n")

# keeps prompting until a valid selection is entered.
def getSelection():
    selection = input("Your selection> ")
    while selection.lower() not in "12345artlx" or len(selection) > 1:
        print("Wrong selection! Please selection a valid option.")
        printMenu()
        selection = input("Your selection> ")
    return selection.lower()

# adds new book
def addNewBook(allBooks):
    bookName = getBookName()
    authorName = input("Author Name> ")
    edition = getEdition()
    ISBN = getISBN()

    valid = validityCheck(ISBN, allBooks)      # checks validity of ISBN entry.
    if valid:                                  # if its valid, the entry will be appended to allBooks library.
        allBooks.append([ISBN, bookName, authorName, edition, []])

# prompts book name until something without a "*" or "%" is entered.
def getBookName():
    bookName = input("Book Name> ")
    while "*" in bookName or "%" in bookName:
        print("Invalid book name!")
        bookName = input("Book Name> ")
    return bookName

# prompts until decimal number or integer is entered.
def getEdition():
    edition = input("Edition> ")
    done = False
    while not done:
        try:
            edition = float(edition)
            done = True
        except:
            print("Invalid Edition!")
            edition = input("Edition> ")
    return int(edition)

# prompts until 13-digit number is entered.
def getISBN():
    ISBN = input("ISBN> ")
    while not ISBN.isdigit() or len(ISBN) != 13:
        print("Invalid ISBN!")
        ISBN = input("ISBN> ")
    return ISBN

# checks validity of 13-digit ISBN
def validityCheck(ISBN, allBooks):
    # will be used for sum of ISBN digits
    total = 0

    # check if ISBN digit is multiplied by 1 or 3 (odd or even). Starts at 1 for 13 digits.
    counter = 1

    # sums the digits according to the factor.
    for char in ISBN:
        if counter % 2 == 0:
            total += int(char) * 3
            counter += 1
        elif counter % 2 == 1:
            total += int(char) * 1
            counter += 1

    # if sum is multiple of 10
    if total % 10 == 0:
        for book in allBooks:    # checks if ISBN is already entered.
            if ISBN in book:
                print("Duplicate ISBN is found! Cannot add the book.")
                return False
        else:        # adds book if multiple of 10 and not entered.
            print("A new book is added successfully.")
            return True
    else:
        print("Invalid ISBN!")
        return False

# borrow a book
def borrowBook(allBooks, borrowedISBNs):
    # borrow name
    borrowerName = input("Enter the borrow name> ")

    # search term converted to lowercase
    userSearchTerm = input("Search term> ").lower()

    # lowercase and last suffix (% or *) taken out.
    searchTerm = userSearchTerm[0 : -1]

    # if the search term is ANYWHERE in the book name and the book is not borrowed already, book will be borrowed.
    if userSearchTerm.endswith("*"):
        found = False       # flag to see whether a match was found.
        for book in allBooks:
            if searchTerm in book[1].lower() and book[0] not in borrowedISBNs:
                print(f"-\"{book[1]}\" is borrowed!")
                borrowedISBNs.append(book[0])            # append ISBN to borrowed list.
                book[4].append(borrowerName)             # append name of borrower to book list.
                found = True
        if not found:
            print("No books found!")

    # if the search term is AT THE START of the book name and the book is not borrowed already, book will be borrowed.
    # variables and procedures are repeated from the previous 'if' block of code.
    elif userSearchTerm.endswith("%"):
        found = False
        for book in allBooks:
            if book[1].lower().startswith(searchTerm) and book[0] not in borrowedISBNs:
                print(f"-\"{book[1]}\" is borrowed!")
                borrowedISBNs.append(book[0])
                book[4].append(borrowerName)
                found = True
        if not found:
            print("No books found!")

    # if the search term MATCHES EXACTLY book name and the book is not borrowed already, book will be borrowed.
    # variables and procedures are repeated from the previous 'if' block of code.
    else:
        found = False
        for book in allBooks:
            if userSearchTerm == book[1].lower() and book[0] not in borrowedISBNs:
                print(f"-\"{book[1]}\" is borrowed!")
                borrowedISBNs.append(book[0])
                book[4].append(borrowerName)
                found = True
        if not found:
            print("No books found!")

# return book
def returnBook(allBooks, borrowedISBNs):
    # prompts user for ISBN. No validation checking
    ISBN = input("ISBN> ")

    # checks if ISBN is borrowed
    if ISBN in borrowedISBNs:
        borrowedISBNs.pop(borrowedISBNs.index(ISBN))     # gets rid of ISBN from borrowed list
        for book in allBooks:
            if ISBN in book:
                print(f"\"{book[1]}\" is returned.")
                break
    else:
        print("No book is found!")

# lists all the books in the library according to formatting specifications.
def listBooks(allBooks, borrowedISBNs):
    for book in allBooks:
        print("-" * 15)
        if book[0] in borrowedISBNs:
            print("[Unavailable]")
        else:
            print("[Available]")
        print(f"{book[1]} - {book[2]}")
        print(f"E: {book[3]} ISBN: {book[0]}")
        print(f"borrowed by: {book[4]}")

# invokes program to start
start()
