import csv
import os

FileName = "books.csv"

def initialize_file():
    if not os.path.exists(FileName):
        try:
            with open(FileName, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Author", "Year"])
        except IOError:
            print("Error: Could not initialize the file.")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter publication year: ")

    try:
        with open(FileName, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
        print(f"{title} added successfully!")
    except IOError:
        print("Error: Could not add the book.")
    except FileNotFoundError:
        print(f"{FileName} not found. Please initialize the file first.")

def search_book():
    search_title = input("Enter book title to search: ").strip().lower()
    try:
        with open(FileName , mode="r")as file:
            reader=csv.reader(file)
            for row in reader:
                if row and row[0].strip().lower() == search_title:
                       print(f"Book Found:Title:{row[0]} , Author:{row[1]} , Year:{row[2]}")
                       return
            print("Book not Found")
    except FileNotFoundError:
        print(f"{FileName} not found. Please initialize the file first.")

def remove_book():
    remove_title = input("Enter Book you want to remove:")
    remaining_books=[]
    try:
        with open (FileName , mode = "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != remove_title:
                    remaining_books.append(row)
        with open(FileName , mode="w")as file:
            writer=csv.writer(file)
            writer.writerows(remaining_books)
        print(f"{remove_title} removed successfully")
    except FileNotFoundError:
        print(f"{FileName} not found. Please initialize the file first.")
def main():
    initialize_file()
    while True:
        print("Library Book Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Remove Book")
        print("4. Done")
        Choice=int(input("Select Options-1,2,3,4:"))
        if Choice == 1:
            print("ADD BOOKS")
            add_book()
        elif Choice == 2:
            print("SEARCH BOOK")
            search_book()
        elif Choice == 3:
            print("REMOVE BOOK")
            remove_book()
        elif Choice == 4:
            print("Done")
            break
        else:
            print("Not in Option, Select Again")
if __name__ : "__main__"
main()
   
  




