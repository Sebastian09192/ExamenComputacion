from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Orders API")

class OrderItem(BaseModel):
    id_catalog: int
    cantidad: int

class Order(BaseModel):
    id: int
    items: List[OrderItem]
    total: float = 0

# Seed inicial
orders = []

@app.get("/api/orders", response_model=List[Order])
def list_orders():
    return orders

@app.post("/api/orders", response_model=Order)
def create_order(order: Order):
    order.total = sum(item.cantidad * 3.5 for item in order.items)  # ejemplo de cálculo
    orders.append(order)
    return order
