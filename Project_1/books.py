from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

Books = [
    {'title':'The Great Gatsby','author':'F. Scott Fitzgerald','category':'Fiction'},
    {'title':'To Kill a Mockingbird','author':'Harper Lee','category':'Fiction'},
    {'title':'A Brief History of Time','author':'Stephen Hawking','category':'Science'},
    {'title':'The Art of War','author':'Sun Tzu','category':'Philosophy'},
    {'title':'1984','author':'George Orwell','category':'Dystopian'},
    {'title':'The Catcher in the Rye','author':'J.D. Salinger','category':'Fiction'},
    {'title':'The Selfish Gene','author':'Richard Dawkins','category':'Science'},
    {'title':'Meditations','author':'Marcus Aurelius','category':'Philosophy'},
    {'title':'Brave New World','author':'Aldous Huxley','category':'Dystopian'},
    {'title':'Sapiens: A Brief History of Humankind','author':'Yuval Noah Harari','category':'History'},
    {'title':'The Hobbit','author':'J.R.R. Tolkien','category':'Fantasy'} ]
    

@app.get("/books")
async def read_books():
    return Books


#  creating dynamic parameter
 # GET method is used to read the data
 # GET method cannot have request body Body()
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in Books:
        if book['title'].lower() == book_title.lower():
            return book
    return {"message": "Book not found"}

# path parameters
@app.get("/books/mybooks")
async def read_all_books():
    return {'book_title':'My favorite book!'}

@app.get("/books/{book_title}")
async def read_book(book_title : str):
    for book in Books:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {'message':'Book not found'}


# Query Parameters
@app.get("/books/")
async def read_books_by_category(category: str):
    results = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
            results.append(book)
    return results


@app.get("/books/{book_author}/")
async def read_author_books(book_author: str, category: str):
    res = []
    for book in Books:
        if book.get('author').casefold() == book_author.casefold() \
        and book.get('category').casefold() == category.casefold():
            res.append(book)
    return res
    
    # POST method is used to create the data

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    Books.append(new_book)
    return new_book

# PUT method is used to update the data

@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == updated_book.get('title').casefold():
            Books[i] = updated_book


# DELETE method

@app.delete("/books/delete_ook/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold() == book_title.casefold():
            Books.pop(i)
            break

    # Get all books from a specific author using path or query parameters


@app.get("/books/author/{book_author}/")
async def read_books_by_author(book_author: str):
    book_list = []
    for book in Books:
        if book.get('author').casefold() == book_author .casefold():
            book_list.append(book)
    return book_list

