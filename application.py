from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Book(BaseModel):

    book_id: int
    book_name: str
    book_author: str
    book_publisher: Optional[str] = None


Books = {
    1: {
        "book_id": 1,
        "book_name": "Cat in the Hat",
        "book_author": "Dr. Seuss",
        "book_publisher": "Houghton Mifflin",
    }
}


@app.get('/')
def index():
    return 'Hello!'


@app.get('/books')
def get_books():
    return Books


@app.post("/add-book")
def add_book(book_id: int, book: Book):

    if book.book_id in Books:
        return {"Error": f"Book {book.book_id} already exists"}
    Books[book.book_id] = book
    return Books[book.book_id]


@app.get("/get-book/{book_id}")
def get_book(book_id: int):
    book = Books.get(book_id)
    if book:
        return book
    else:
        return "does not exist"


@app.put("/update-book/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    if book_id not in Books:
        raise HTTPException(status_code=404, detail="Book not found")
    Books[book_id] = book
    return Books[book_id]


@app.delete("/remove-book")
def delete_book(book_id: int, book: Book):
    if book_id not in Books:
        raise HTTPException(status_code=404, detail="Book not found")
    del Books[book_id]
    return {"message": "Book deleted"}


# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')
