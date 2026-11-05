# Store books as isbn -> {"title": ..., "author": ..., "copies": ..., "issued_to": [...], "ever_issued": ...}
books = {}

def addBook():
    global books
    isbn = str(input("Enter ISBN: ")).strip()
    
    if isbn in books:
        try:
            extra_copies = int(input(f"Book '{books[isbn]['title']}' already exists. Enter number of copies to add: "))
            if extra_copies > 0:
                books[isbn]["copies"] += extra_copies
                print(f"Successfully added {extra_copies} copies. Total copies now: {books[isbn]['copies']}")
            else:
                print("Copies to add must be greater than zero.")
        except ValueError:
            print("Invalid input for copies.")
        return

    title = str(input("Enter Book Title: ")).strip()
    author = str(input("Enter Author Name: ")).strip()
    try:
        copies = int(input("Enter Number of Copies: "))
        if copies < 0:
            print("Copies cannot be negative.")
            return
    except ValueError:
        print("Invalid input for copies.")
        return

    books[isbn] = {
        "title": title, 
        "author": author, 
        "copies": copies, 
        "issued_to": [],
        "ever_issued": False
    }
    print("Book added successfully!")

def issueBook():
    global books
    isbn = str(input("Enter ISBN of the book to issue: ")).strip()
    if isbn not in books:
        print("Book not found!")
        return

    member_id = str(input("Enter Member ID: ")).strip()
    book = books[isbn]

    
    if book["copies"] <= 0:
        print("Book is currently unavailable (0 copies left).")
        return

    
    if member_id in book["issued_to"]:
        print("This member already holds a copy of this book!")
        return

    
    total_held_by_member = sum(
        1 for b_data in books.values() if member_id in b_data["issued_to"]
    )
    if total_held_by_member >= 2:
        print("Member already holds the maximum limit of 2 books!")
        return

    # Issue the book
    book["copies"] -= 1
    book["issued_to"].append(member_id)
    book["ever_issued"] = True
    print(f"Book '{book['title']}' successfully issued to member {member_id}.")

def returnBook():
    global books
    isbn = str(input("Enter ISBN of the book to return: ")).strip()
    if isbn not in books:
        print("Book not found!")
        return

    member_id = str(input("Enter Member ID: ")).strip()
    book = books[isbn]

    
    if member_id not in book["issued_to"]:
        print("Error: This member does not hold this book!")
        return
    book["issued_to"].remove(member_id)
    book["copies"] += 1
    print(f"Book '{book['title']}' successfully returned by member {member_id}.")

def searchBook():
    global books
    if not books:
        print("No books in the library.")
        return

    query = str(input("Enter Title or ISBN to search: ")).strip().lower()
    found = False
    
    print("\n--- Search Results ---")
    for isbn, data in books.items():
        if query in isbn.lower() or query in data["title"].lower():
            print(f"ISBN: {isbn} | Title: {data['title']} | Author: {data['author']} | Available Copies: {data['copies']} | Issued To: {data['issued_to']}")
            found = True
            
    if not found:
        print("No matching books found.")

def showReports():
    global books
    if not books:
        print("No library records available.")
        return

    print("\n--- LIBRARY REPORTS ---")

    
    search_author = str(input("Enter author name to search books: ")).strip().lower()
    author_books = [
        data['title'] 
        for data in books.values() 
        if data['author'].strip().lower() == search_author
    ]
    print(f"\n1. Books by '{search_author.title}':")
    if author_books:
        for title in author_books:
            print(f"   - {title}")
    else:
        print("   None found.")

    
    member_books_dict = {}
    for isbn, data in books.items():
        for member in data['issued_to']:
            member_books_dict.setdefault(member, []).append(data['title'])

    multi_book_members = {
        member: book_list 
        for member, book_list in member_books_dict.items() 
        if len(book_list) > 1
    }

    print("\n2. Members Holding More Than One Book:")
    if multi_book_members:
        for member, book_list in multi_book_members.items():
            print(f"   Member {member} holds {len(book_list)} books: {', '.join(book_list)}")
    else:
        print("   None")

    
    unavailable_books = [
        data['title'] 
        for data in books.values() 
        if data['copies'] == 0
    ]
    print("\n3. Currently Unavailable Books (0 Copies):")
    if unavailable_books:
        for title in unavailable_books:
            print(f"   - {title}")
    else:
        print("   None (All books have available copies)")

    
    never_issued_books = [
        data['title'] 
        for data in books.values() 
        if not data.get("ever_issued", False)
    ]
    print("\n4. Books That Have Never Been Issued:")
    if never_issued_books:
        for title in never_issued_books:
            print(f"   - {title}")
    else:
        print("   None")


while True:
    print("\n--- Library Record System Menu ---")
    print("1. Add a book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Search books")
    print("5. Reports")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == '1':
        addBook()
    elif choice == '2':
        issueBook()
    elif choice == '3':
        returnBook()
    elif choice == '4':
        searchBook()
    elif choice == '5':
        showReports()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")
