from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/edges", tags=["model"])
def get_edges(response: JSONResponse):
    return [
        {"from": 0, "to": 1, "label": "son"},
        {"from": 0, "to": 2, "label": "son"},
        {"from": 1, "to": 2, "label": "brother"},
    ]
