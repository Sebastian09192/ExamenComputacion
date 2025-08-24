from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Customers API")

class Customer(BaseModel):
    id: int
    nombre: str
    email: str
    numero_identidad: str

# Seed inicial
customers = [
    Customer(id=1, nombre="Juan Pérez", email="juan@example.com", numero_identidad="123456789"),
    Customer(id=2, nombre="María Gómez", email="maria@example.com", numero_identidad="987654321")
]

@app.get("/api/customers", response_model=List[Customer])
def list_customers():
    return customers

@app.post("/api/customers", response_model=Customer)
def add_customer(customer: Customer):
    customers.append(customer)
    return customer