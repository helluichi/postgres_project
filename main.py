from db import SessionLocal
from crud import get_categories, get_books

def main():
    db = SessionLocal()
    print("=" * 50)
    print("КАТЕГОРИИ:")
    print("=" * 50)
    for cat in get_categories(db):
        print(f"ID: {cat.id} | {cat.name} | {cat.description}")
    print("\n" + "=" * 50)
    print("КНИГИ:")
    print("=" * 50)
    for book in get_books(db):
        print(f"ID: {book.id} | {book.title} | {book.author} ({book.year}) | {book.category.name}")
    db.close()

if __name__ == "__main__":
    main()
