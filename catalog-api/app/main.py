from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Catalog API")

class Product(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    descripcion: str

# Seed inicial
products = [
    Product(id=1, nombre="Café Arábica", precio=3.5, stock=100, descripcion="Café de alta calidad"),
    Product(id=2, nombre="Café Robusta", precio=2.5, stock=50, descripcion="Café fuerte")
]

@app.get("/api/catalog", response_model=List[Product])
def list_products():
    return products

@app.post("/api/catalog", response_model=Product)
def add_product(product: Product):
    products.append(product)
    return product