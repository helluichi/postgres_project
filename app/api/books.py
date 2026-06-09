from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[BookResponse])
def get_books(
    category_id: Optional[int] = Query(None, description="Фильтр по ID категории"),
    db: Session = Depends(get_db)
):
    """Получить список книг. Можно фильтровать по category_id"""
    if category_id:
        category = crud.get_category_by_id(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return crud.get_books_by_category_id(db, category_id)
    return crud.get_books(db)

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Получить книгу по ID"""
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Создать новую книгу"""
    category = crud.get_category_by_id(db, book.category_id)
    if not category:
        raise HTTPException(status_code=400, detail="Category does not exist")
    return crud.create_book(db, book.title, book.author, book.year, book.category_id)

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    """Обновить книгу"""
    existing = crud.get_book_by_id(db, book_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.category_id is not None:
        category = crud.get_category_by_id(db, book.category_id)
        if not category:
            raise HTTPException(status_code=400, detail="Category does not exist")
    return crud.update_book(db, book_id, book.title, book.author, book.year, book.category_id)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу"""
    existing = crud.get_book_by_id(db, book_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db, book_id)
    return None
