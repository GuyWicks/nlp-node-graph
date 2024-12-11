from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from app.nlp import NLP
import spacy
from icecream import ic as debug
from dotenv import load_dotenv
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

env_config = load_dotenv()
spacy_model = os.getenv("SPACY_MODEL")
assert(spacy_model)

nlp_model = spacy.load(spacy_model)
spacy.prefer_gpu()

nlp = NLP(
    model=nlp_model,
    rules="data/test1.txt",
    pronouns="data/pronouns.txt",
)

debug("Config loaded", spacy_model)
