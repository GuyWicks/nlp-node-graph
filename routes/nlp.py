from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.config import nlp_model
from app.nlp import NLP

# from spacy import displacy

router = APIRouter()


@router.get("/nlp", response_class=JSONResponse, tags=["nlp"])
def get_nlp(q: str, response: JSONResponse):
    doc = nlp_model(q)
    return doc.to_json()
