from fastapi import FastAPI
import web.home
import web.nlp
import routes.nodes
import routes.edges
import routes.nlp
from fastapi.staticfiles import StaticFiles
from app.lang import NLP
from app.config import nlp_model

fastapi = FastAPI()

nlp = NLP(
    model=nlp_model,
    rules="data/test1.txt",
    pronouns="data/pronouns.txt",
)

fastapi.mount("/static", StaticFiles(directory="static"), name="static")
fastapi.mount("/lib", StaticFiles(directory="lib"), name="lib")


# HTML pages
fastapi.include_router(web.home.router)
fastapi.include_router(web.nlp.router)

# API
fastapi.include_router(routes.nodes.router, prefix="/api")
fastapi.include_router(routes.edges.router, prefix="/api")
fastapi.include_router(routes.nlp.router, prefix="/api")
