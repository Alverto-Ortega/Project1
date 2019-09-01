import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    b = open("books.csv")
    reader = csv.reader(b)
    

    #later on figure out how to insert into two tables through books table's reference authorid to insert as a authorname value in authours table
    
    #asks user input for choices of adding data to book table or displaying current data table contents
    userInput = input("would you like to add data to your books table? YES or NO: ")
    if userInput == "YES":
        addBook(reader)
        userInput=input("Would you like to display your current book table data? YES or NO: ")
        if userInput =="YES":
            displayData()
        else:
            print("Thank you, have a great day! ")

    else:
        userInput =input("Would you like to display your current book table data? YES or NO: ")
        if userInput =="YES":
            displayData()
        else:
            print("Thank you, have a great day! ")

def addBook(reader):
    #an if statement for checking if we want to insert new data but not repeating the same insertion of the same previous data
    next(reader) #skips over the first line headings in content so that it doesnt store the headings into the database
    for isbnnumber, title,authorname,publicyear, in reader:
        db.execute("INSERT INTO books(isbnnumber,title,authorname,publicyear) VALUES (:isbnnumber, :title,  :authorname, :publicyear)",
                    {"isbnnumber": isbnnumber, "title": title,  "authorname": authorname,"publicyear": publicyear}) 
        #print(f"added book: {title} from {authorname} published in {publicyear} with and isbn number : {isbnnumber}.")
   
    db.commit()
    print("You have Successfully inserted all of your requested Data, now the data will be displayed upon request... \n")

def displayData():
    books = db.execute("SELECT * FROM books").fetchall()
    print(books)
    db.commit()

    #for book in books:
    #   print(f" isbn number: {book.isbnnumber} title: {book.title} author Name:{book.authorname} public year:{book.publicyear}")


if __name__ == "__main__":
    main()


    