from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Zomato Order Service",
    description=(
       "Internal API for managing Orders"
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
    # FastAPI Convertes this dictonary to json
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

@app.get("/debug/request-info")
async def request_info(request: Request):
    """ Inspect the row request object """
    return {
        "method" : request.method,
        "url" : str(request.url),
        "header" : dict(request.headers),
        "path_params" : request.path_params,
        "query_params" : dict(request.query_params),
    }

@app.get(
    "/orders/active",
    summary="Get Active Orders",
    description=(
        "Returns all orders that are currently being prepared"
        "or are out for delivery"
    ),
    tags=["Orders"],
    response_description="List of active orders objects",
    deprecated=False
)
def get_active_order():
    """This docstring also aprears in docs"""
    return {
        "active_orders" : [
            {
                "id" :  1,
                "item" : "panner",
                "status" : "delivered"
            }
        ] 
    }

@app.get("/restaurants", tags=["Restaurants"])
def list_resto():
    """anothre docstring for another endpoint"""
    return {
        "restaurants" : [
            {
                "test" : "test"
            }
        ]
    }

@app.get("/restaurants/jalgaon", tags=["Jalgaon Restaurants"])
def list_resto_jalgaon():
    """anothre docstring for another endpoint"""
    return {
        "restaurants" : [
            {
                "test" : "test"
            }
        ]
    }
