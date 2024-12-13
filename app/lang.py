from spacy import displacy
from app.config import debug
from functools import lru_cache
import ctypes


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class NLP:
    _rules = []
    _nlp_model = None

    def __init__(
        self,
        model: object = None,
        rules: str = "",
        pronouns: str = "",
    ):
        self._nlp_model = model
        self.load_rules(rules) if rules else None
        self.load_proper_nouns(pronouns) if pronouns else None
        return None

    @staticmethod
    @lru_cache
    def _hash(word: str) -> str:
        return ctypes.c_uint64(hash(word)).value.to_bytes(8, "big").hex()

    @lru_cache
    def tokenize(self, rule: str, seed: int = -1):
        doc = self._nlp_model(rule)
        return doc

    @lru_cache
    def visulize(self, rule: str):
        return displacy.render(
            self.tokenize(rule),
            style="dep",
            page=False,
            minify=False,
        )

    def load_rules(self, filename: str):
        with open(file=filename, mode="r", encoding="utf-8") as f:
            for rule in f:
                rule = rule.strip()
                self._rules.append(
                    {
                        "_id": self._hash(rule),
                        "rule": rule,
                        "dep": self.tokenize(rule).to_json(),
                    }
                )
            return self.rules

    @lru_cache
    def add_rule(self, rule: str):
        self._rules.append(
            {
                "_id": self._hash(rule),
                "rule": rule,
                "dep": self.tokenize(rule).to_json(),
            }
        )
        return self._hash(rule)

    def load_proper_nouns(self, filename: str = ""):
        if filename:
            try:
                pronouns_l = open(
                    file=filename,
                    mode="rt",
                    encoding="utf-8",
                ).read()
                self.add_proper_nouns(pronouns_l)
            except FileNotFoundError:
                pass

    def add_proper_nouns(self, nouns):
        ruler = self._nlp_model.get_pipe("attribute_ruler")
        attrs = {"TAG": "NNP", "POS": "PROPN"}
        for noun in nouns.split():
            ruler.add(patterns=[[{"TEXT": noun}]], attrs=attrs, index=0)

    def rules(self):
        return self._rules

    def nouns(self):
        """
        NLP.nouns()

        Return a list of all the nouns and proper nouns
        """
        debug("hello")

        for r in self.rules():
            debug(r)
