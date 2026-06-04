from db import engine, SessionLocal
from models import Base
from crud import create_category, get_category_by_name, create_book

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    categories = [
        ("Фантастика", "Научная фантастика и фэнтези"),
        ("Детектив", "Криминальные романы и детективы"),
        ("Классика", "Мировая классическая литература"),
    ]
    for name, desc in categories:
        create_category(db, name, desc)
    
    books_data = [
        ("1984", "Джордж Оруэлл", 1949, "Фантастика"),
        ("Война миров", "Герберт Уэллс", 1898, "Фантастика"),
        ("Убийство в Восточном экспрессе", "Агата Кристи", 1934, "Детектив"),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Классика"),
        ("Гордость и предубеждение", "Джейн Остин", 1813, "Классика"),
    ]
    for title, author, year, category_name in books_data:
        category = get_category_by_name(db, category_name)
        if category:
            create_book(db, title, author, year, category.id)
    
    db.close()
    print("База данных инициализирована успешно!")

if __name__ == "__main__":
    init_db()
