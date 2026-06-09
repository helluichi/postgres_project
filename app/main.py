from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Добавляем корневую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.api import books, categories

app = FastAPI(
    title="Bookstore API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(categories.router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "API is running"}

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Bookstore API",
        "docs": "/docs",
        "redoc": "/redoc"
    }
