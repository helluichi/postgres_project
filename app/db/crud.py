from sqlalchemy.orm import Session
from app.db.models import Category, Book

def create_category(db: Session, name: str, description: str = None):
    category = Category(name=name, description=description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db: Session):
    return db.query(Category).all()

def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category(db: Session, category_id: int, name: str = None, description: str = None):
    category = get_category_by_id(db, category_id)
    if category:
        if name is not None:
            category.name = name
        if description is not None:
            category.description = description
        db.commit()
        db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    if category:
        db.delete(category)
        db.commit()
        return True
    return False

def create_book(db: Session, title: str, author: str, year: int, category_id: int):
    book = Book(title=title, author=author, year=year, category_id=category_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books_by_category_id(db: Session, category_id: int):
    return db.query(Book).filter(Book.category_id == category_id).all()

def update_book(db: Session, book_id: int, title: str = None, author: str = None, 
                year: int = None, category_id: int = None):
    book = get_book_by_id(db, book_id)
    if book:
        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if year is not None:
            book.year = year
        if category_id is not None:
            book.category_id = category_id
        db.commit()
        db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()
        return True
    return False
