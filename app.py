from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from calculator import add, divide, multiply, subtract

app = FastAPI(title="Calculator API", version="1.0.0")


class CalculationRequest(BaseModel):
    operation: Literal["add", "subtract", "multiply", "divide"]
    a: float
    b: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/calculate")
def calculate(request: CalculationRequest):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    try:
        result = operations[request.operation](request.a, request.b)
    except ZeroDivisionError as exc:
        raise HTTPException(status_code=400, detail="division by zero") from exc

    return {"operation": request.operation, "result": result}
