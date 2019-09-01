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
   
    next(reader) #skips over the first line headings in content so that it doesnt store the headings into the database
    for isbnnumber, title,authorname,publicyear, in reader:
        db.execute("INSERT INTO books(isbnnumber,title,authorname,publicyear) VALUES (:isbnnumber, :title,  :authorname, :publicyear)",
                    {"isbnnumber": isbnnumber, "title": title,  "authorname": authorname,"publicyear": publicyear})
 
        print(f"added book: {title} from {authorname} published in {publicyear} with and isbn number : {isbnnumber}.")
    db.commit()
def displayData():
    books = db.execute("SELECT isbnnumber,title, authorname,publicyear FROM books").fetchall()

    for book in books:
        print(f" isbn number: {book.isbnnumber} title: {book.title} author Name:{book.authorname} public year:{book.publicyear}")
if __name__ == "__main__":
    main()
displayData()
    