from sqlalchemy.orm import Session
from models import Category, Book

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

def create_book(db: Session, title: str, author: str, year: int, category_id: int):
    book = Book(title=title, author=author, year=year, category_id=category_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db: Session):
    return db.query(Book).all()
