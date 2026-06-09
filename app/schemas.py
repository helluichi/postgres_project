from pydantic import BaseModel, ConfigDict
from typing import Optional

# ========== Схемы для категорий ==========
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)

# ========== Схемы для книг ==========
class BookBase(BaseModel):
    title: str
    author: str
    year: int
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    category_id: Optional[int] = None

class BookResponse(BookBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
