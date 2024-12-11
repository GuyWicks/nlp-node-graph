from app.config import nlp, debug
from app.node import Node


def test_get_nodes():
    nodes = Node(nlp=nlp)
    n, e = nodes.tokens()
    debug(n)
