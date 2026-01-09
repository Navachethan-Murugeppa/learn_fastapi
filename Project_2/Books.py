from fastapi import Body, FastAPI, Path, Query, HTTPException
from pydantic import BaseModel , Field
from typing import Optional, List
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    descriptio: str 
    rating : int 
    publish_date: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, publish_date: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date

class BookRequest(BaseModel):
    id : Optional[int] = Field(description="The unique identifier of the book",default=None)
    title : str = Field(min_length=3)
    author : str = Field(min_length=3)
    description : str = Field(min_length=1, max_length=100)
    rating : int = Field(gt = 0, lt=6)
    publish_date :int = Field(gt=1931, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new Book",
                "author": "John Doe",
                "description": "This is a new book added to the collection.",
                "rating": 4,
                "publish_date": 2023
    }
        }
    }


Books = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", description="A novel set in the Roaring Twenties.", rating=5, publish_date=1925),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", description="A novel about racial injustice in the Deep South.", rating=5, publish_date=1960),
    Book(3,"1984","George Orwell", "A dystopian novel",5, publish_date=1949),
    Book(4,"Pride and Prejudice","Jane Austen", "A classic romance novel",4,1813),
    Book(5,"The Catcher in the Rye","J.D. Salinger", "A novel about teenage rebellion",4, 1951),
    Book(6,"The Hobbit","J.R.R. Tolkien", "A fantasy adventure novel",5, 1937),
    Book(7,"Fahrenheit 451","Ray Bradbury", "A dystopian novel about book burning",4,1953),
    Book(8,"Moby Dick","Herman Melville", "A novel about a giant whale",3, 1851)
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_books():
    return Books

@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    Books.append(find_book_id(new_book))

def find_book_id(book: Book):
    # if(len(Books) > 0):
    #     book.id = Books[-1].id+1
    # else:
    #     book.id = 1
    book.id = Books[-1].id + 1 if len(Books) > 0 else 1   
    return book

@app.get("/books/publish/",status_code=status.HTTP_200_OK)
async def read_books_by_publish_date(publish_date: int = Query(gt=1931, lt=2031)):
    book_res = []
    for book in Books:
        if book.publish_date == publish_date:
            book_res.append(book)
    return book_res


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in Books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')
    # return {"message": "Book not found"}

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_rating(rating: int = Query(gt=0, lt=6)):
    book_res = []
    for book in Books:
        if book.rating == rating:
            book_res.append(book)
    return book_res

@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(Books)):
        if Books[i].id == book.id:
            Books[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')
    


@app.delete("/books/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id : int = Path(gt=0)):
    book_changed = False
    for i in range(len(Books)):
        if Books[i].id == book_id:
            Books.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')




    

