from icecream import ic as debug
from functools import lru_cache
import networkx as nx
import ctypes


class Node:
    _nlp = None

    def __init__(self, nlp):
        self._nlp = nlp
        pass

    @staticmethod
    @lru_cache
    def _hash(word: str) -> str:
        return ctypes.c_uint64(hash(word)).value.to_bytes(8, "big").hex()

    def tokens(self):
        nodes = {}
        edges = {}
        for n in self._nlp.rules():
            text = n["dep"]["text"]
            for t in n["dep"]["tokens"]:
                debug(t)
                match t["pos"]:
                    case "NOUN":
                        h = self._hash(t["lemma"])
                        nodes[h] = {
                            "color": "blue",
                            "font": {"color": "white"},
                            "id": h,
                            "image": "/static/database-svgrepo-com.svg",
                            "label": t["lemma"],
                            "shape": "ellipse",
                            "word": text[int(t["start"]) : int(t["end"])],
                            "title": f"""{text}
{text[int(t["start"]) : int(t["end"])]}

pos; {t['pos']}
dep; {t['dep']}
tag; {t['tag']}
head; {t['head']}
""",
                            "size": 60,
                        }

                    case "PROPN":
                        h = self._hash(t["lemma"])
                        nodes[h] = {
                            "color": "green",
                            "font": {"color": "white"},
                            "id": h,
                            "label": t["lemma"],
                            "shape": "box",
                            "size": 60,
                        }

                    case "VERB":
                        debug(t["pos"])
                        pass

        n = []
        for v in nodes:
            n.append(nodes[v])

        return n, edges

    def to_network(self):
        G = nx.Graph()
