# Creating a library management system in python
# PROJECT DETAILS:
# This project allows user to :
# 1. Add books in details like title, author, book id
# 2. View all books that are available in the library.
# 3. Search for a book by title or author.
# 4. Exit the program gracefully when the user chooses to do so.

print("=====Welcome to Library Management System=====")
print("Enter your choice")
print("1. Add a book")
print("2. View all books")
print("3. Search for a book")
print("4. Exit")

choice=0
books=[]

while True:
    # Taking user input for choice
    choice=int(input("Enter a choice(1-4): "))

    # Code block for storing a book
    if (choice==1):
        # Take user input for book details
        title=input("Enter the title of the book: ")
        author=input("Enter the author name: ")
        book_id=int(input("Enter the book id: "))

        book = {
            "title":title,
            "author":author,
            "book_id":book_id
        }
        books.append(book)
    
    # Code block for viewing all books
    elif (choice==2):
        if(len(books)==0):
            print("No books are stored yet")
        else:
            print("====Available Books====")
            count=1
            for i in books:
                print(f"{count}. Title : {i["title"]}")
                print(f"{count}. Author : {i["author"]}")
                print(f"{count}. Book Id : {i["book_id"]}")
                count+=1
    
    # Code block for searching a book
    elif (choice==3):
        search_term = input("Enter the title of the book to search: ").lower()
        found_book=None
        for i in books:
            if i["title"].lower()==title.lower():
                found_book = i
                break
        
        if found_book:
            print(f"{choice}. Title : {i["title"]}")
            print(f"{choice}. Author : {i["author"]}")
            print(f"{choice}. Book Id : {i["book_id"]}")
        else:
            print("Book not found")
    
    # Code block to exit the program
    elif (choice==4):
        print("Exit successfully")
        break

    else:
        print("Invalid choice")
