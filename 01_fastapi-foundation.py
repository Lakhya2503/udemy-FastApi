from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Zomato Order Service",
    description=(
        "Internal API for managing Orders",
        "It will handle creation, Traking of delivery system."
    ),
    version="1.1.2",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """"Root endpoint - Health Check"""
    # FastAPI Convertes this dic to json
    return { "message" : "Welcome to Zomato Order Service", "status": "Healthy" }

@app.get("/about")
def about():
    """"Returns API metadata"""
    return { 
        "service " : "Order service",
        "team" : "backend Platform",
        "region" : "ap-south-1",
        "version" : "1.1.2"
    }

@app.get("/orders")
def list_orders():
    """"List recent orders"""
    return {
        "orders" : [
            {
                "id" : 1,
                "item" : "Paneer",
                "status" : "delivered"
            },
            {
                "id" : 2,
                "item" : "Veg Corma",
                "status" : "pending"
            },
            {
                "id" : 4,
                "item" : "Masala Rice",
                "status" : "cancelled"
            },
        ]
    }

@app.get("/orders/status")
def order_status():
    """"Get Order status"""
    return {
        "total_today_order" : 2_342_2,
        "total_city" : "Jalgaon"
    }
