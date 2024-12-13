from icecream import ic as print
from app.lang import NLP
from app.config import nlp_model


def test_model():
    assert nlp_model


def test_tokenize():
    print(nlp_model("Guy is the best boy").to_json())


def test_nlp_class():
    nlp = NLP(nlp_model)
    assert nlp


def test_nlp_singleton():
    nlp1 = NLP(nlp_model)
    nlp2 = NLP(nlp_model)
    assert nlp1 == nlp2


def test_rules_load():
    nlp = NLP(nlp_model)
    nlp.load_rules("data/test1.txt")
    assert nlp.rules()[0]["_id"] == "8739ac72b3c05ce4"


def test_rule_same():
    nlp = NLP(nlp_model)
    id1 = nlp.add_rule("this is the same")
    id2 = nlp.add_rule("this is the same")
    assert id1 == id2


def test_rule_pnoun():
    nlp = NLP()

    doc2 = nlp.tokenize("unisure", 1).to_json()
    assert doc2["tokens"][0]["pos"] == "PROPN"

    doc3 = nlp.tokenize("guidewire", 1).to_json()
    assert doc3["tokens"][0]["pos"] == "PROPN"
