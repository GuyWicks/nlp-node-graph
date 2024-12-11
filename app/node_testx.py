"""
from app.node import Node
from app.nlp import NLP
from app.config import nlp_model
from icecream import ic as debug

def test_node():
    nlp = NLP(
        model=nlp_model,
        rules="data/test1.txt",
    )

    nodes = Node(nlp.rules())
    debug(nodes)

    for n in nlp.rules():
        for t in n["dep"]["tokens"]:
            match t["pos"]:
                case "NOUN":
                    debug(t["pos"])

                case "PROPN":
                    debug(t["pos"])

                case "VERB":
                    debug(t["pos"])
                    pass

"""