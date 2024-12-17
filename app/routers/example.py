from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/example",
    tags=["Example"],
)

class Item(BaseModel):
    name: str
    description: str

@router.get("/")
def read_root():
    return {"message": "Welcome to the example API"}

@router.post("/items/")
def create_item(item: Item):
    return {"message": f"Item {item.name} created"}

