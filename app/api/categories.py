from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.db.db import get_db
from app.db import crud
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    """Получить список всех категорий"""
    return crud.get_all_categories(db)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    """Получить категорию по ID"""
    category = crud.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    """Создать новую категорию"""
    existing = crud.get_category_by_name(db, category.name)
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    return crud.create_category(db, category.name, category.description)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    """Обновить категорию"""
    existing = crud.get_category_by_id(db, category_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.update_category(db, category_id, category.name, category.description)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    """Удалить категорию"""
    existing = crud.get_category_by_id(db, category_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Category not found")
    crud.delete_category(db, category_id)
    return None
