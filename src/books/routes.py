from fastapi import APIRouter,status
from typing import List
from fastapi.exceptions import HTTPException
from src.books.schemas import Book, bookUpdateModal
from src.books.book_data import books

book_router = APIRouter()

@book_router.get('/',response_model=List[Book])
async def get_all_books() -> List[dict]:
    return books


@book_router.post('/',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@book_router.get('/{book_id}')
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Book not found')

@book_router.put('/{book_id}')
async def update_a_book(book_id: int,book_data:bookUpdateModal) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['author'] = book_data.author
            book['publisher'] = book_data.publisher
            book['page_count'] = book_data.page_count
            book['language'] = book_data.language

        return {'message':'Book succeffuly update','Data': book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Books not found')


@book_router.delete('/{book_id}')
async def delete_a_book(book_id: int) -> dict:
    for index, book in enumerate(books):
        if book['id'] == book_id:
            deleted = books.pop(index)
            return {"message": "Book deleted", "book": deleted}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found')

    