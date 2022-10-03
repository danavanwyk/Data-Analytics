#Compulsory Task
#Dana van Wyk
#29-11-2021
#Import sqlite3
import sqlite3
#create database with name ebookstore
db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER )''')

db.commit()

#Create variables for all instances of existing books.

cursor = db.cursor()

id_1 = 3001
title_1 = "A Tale of Two Cities"
author_1 = "Charles Dickens"
qty_1 = 30

id_2 = 3002
title_2 = "Harry Potter and the Philosopher's Stone"
author_2 = "J.K. Rowling"
qty_2 = 40

id_3 = 3003
title_3 = "The Lion, the Witch and the Wardrobe"
author_3 = "C. S. Lewiss"
qty_3 = 25

id_4= 3004
title_4= "The Lord of the Rings"
author_4= "J.R.R Tolkien"
qty_4= 37

id_5 = 3005
title_5 = "Alice in Wonderland"
author_5 = "Lewis Carrol"
qty_5 = 12

#Insert books into table.

cursor.execute('''INSERT OR IGNORE INTO books (id, title, author, qty) VALUES(?,?,?,?)''', (id_1, title_1, author_1, qty_1))

cursor.execute('''INSERT OR IGNORE INTO books (id, title, author, qty) VALUES(?,?,?,?)''', (id_2, title_2, author_2, qty_2))

cursor.execute('''INSERT OR IGNORE INTO books (id, title, author, qty) VALUES(?,?,?,?)''', (id_3, title_3, author_3, qty_3))

cursor.execute('''INSERT OR IGNORE INTO books (id, title, author, qty) VALUES(?,?,?,?)''', (id_4, title_4, author_4, qty_4))

cursor.execute('''INSERT OR IGNORE INTO books (id, title, author, qty) VALUES(?,?,?,?)''', (id_5, title_5, author_5, qty_5))

db.commit()

##Create user menu
#Create a class with all the attributes of books in the store.
class Book(object):
    def __init__(self, id, title, author, qty):
        self.id = id
        self.title = title
        self.author = author
        self.qty = qty
#1. Enter book
#Create a method to create a new book.
    def add_new_book(self):
        self.new_id = input("Enter new book ID: ")
        self.new_title = input("Enter new Book Title: ")
        self.new_author = input("Enter new Book Author: ")
        self.new_qty = input("Enter new Book quantity: ")
        #INSERT INTO will alow us to add a new book into the books table.
        cursor.execute('''INSERT INTO books (id, title, author, qty)
                VALUES(?,?,?, ?)''', (self.new_id, self.new_title, self.new_author, self.new_qty))


#2. Update book 
#create new method to allow us to update the quantities of the books in stock.
    def update_book(self):
        self.current_id = input("Enter current book ID, which you would like to update: ")
        self.qty_update = input("Please update the current amount of books in stock :")
        cursor.execute('''UPDATE books SET qty = ? WHERE id = ? ''', (self.qty_update, self.current_id))


#3. Delete book 
    def remove_book(self):
        self.delete_book = input("Enter book ID, which you would like to Remove from your stocklist: ")
        # DELETE FROM will delete a specific book according to its id in the table.
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (self.delete_book,))

    
#4. Search books 
#CReate a new method for finding a book and dispaying the book details.
    def find_books(self):
        self.search = input("Enter the book ID of the book you are looking for : ")
        #SELECT ALL(*) FROM will run through all thebooks in the table and return the one with the coorelating id the user puts in.
        cursor.execute('''SELECT * FROM books WHERE id = ?''', (self.search,))
        books_found = cursor.fetchall()
        print(books_found)

db.commit()

#new variables which acts a a placeholder to add, update, delete or search for books.
new_book = Book(0-5000, "Book Name", "Author Name", int())
updated_book = Book(0-5000, "Book Name", "Author Name", int())
deleted_book = Book(0-5000, "Book Name", "Author Name", int())
search_books = Book(0-5000, "Book Name", "Author Name",int())

user_input = input("To enter a book press 1, \nTo update a book press 2, \nTo delete a book press 3, \nto search books press 4, \nTo display all books in stock press: 5, \n Press 0 to exit program")
while user_input != 'quit':

    if user_input == '1':
        #User functionality
        new_book.add_new_book()
        #Check Stock 
        cursor.execute('''SELECT id, title, author, qty FROM books WHERE qty > 0''')
        all_books_in_stock = cursor.fetchall()
        db.commit()
        db.close()
        print(all_books_in_stock)
        quit()

    elif user_input == '2':
        #User functionality
        updated_book.update_book()
        #Check Stock 
        cursor.execute('''SELECT id, title, author, qty FROM books WHERE qty > 0''')
        all_books_in_stock = cursor.fetchall()
        db.commit()
        db.close()
        print(all_books_in_stock)
        quit()

    elif user_input == '3':
        #User functionality
        deleted_book.remove_book()
        #Check Stock 
        cursor.execute('''SELECT id, title, author, qty FROM books WHERE qty > 0''')
        all_books_in_stock = cursor.fetchall()
        db.commit()
        db.close()
        print(all_books_in_stock)
        quit()

    elif user_input == '4':
        #User functionality
        search_books.find_books()
        db.commit()
        db.close()
        quit()

    elif user_input == '5':
        #User functionality
        #will display all stock if necessary
        cursor.execute('''SELECT id, title, author, qty FROM books WHERE qty > 0''')
        all_books_in_stock = cursor.fetchall()
        print(all_books_in_stock)
        db.commit()
        db.close()
        quit()
    
    elif user_input == '0':
        db.commit()
        db.close()
        quit()

