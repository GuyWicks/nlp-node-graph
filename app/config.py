from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
import spacy
from icecream import ic as debug
from dotenv import load_dotenv
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

env_config = load_dotenv()
spacy_model = os.getenv("SPACY_MODEL")
assert spacy_model

nlp_model = spacy.load(spacy_model)
spacy.prefer_gpu()



debug("Config loaded", spacy_model)


# Ensure only a single instance of a class ever exists
