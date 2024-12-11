from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.config import nlp
from app.node import Node

router = APIRouter()


def node_element(e):
    return e["_id"]


@router.get("/nodes", tags=["model"])
def get_nodes(response: JSONResponse):
    nodes = Node(nlp=nlp)
    n, _ = nodes.tokens()
    return n
