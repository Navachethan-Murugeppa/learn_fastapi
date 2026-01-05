from fastapi import FastAPI
app = FastAPI()

Books = [
    {'title':'The Great Gatsby','author':'F. Scott Fitzgerald','category':'Fiction'},
    {'title':'To Kill a Mockingbird','author':'Harper Lee','category':'Fiction'},
    {'title':'A Brief History of Time','author':'Stephen Hawking','category':'Science'},
    {'title':'The Art of War','author':'Sun Tzu','category':'Philosophy'},
    {'title':'1984','author':'George Orwell','category':'Dystopian'},
    {'title':'The Catcher in the Rye','author':'J.D. Salinger','category':'Fiction'}
    ]

@app.get("/books")
async def read_books():
    return Books