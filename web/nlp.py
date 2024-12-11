from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.config import templates
from app.nlp import NLP

router = APIRouter()


@router.get("/nlp", response_class=HTMLResponse)
def get_nlp(
    request: Request,
    q: str = "",
):
    nlp = NLP()
    svg = nlp.visulize(q)
    doc = nlp.tokenize(q)

    return templates.TemplateResponse(
        request=request,
        name="nlp.html.j2",
        context={
            "nlp": svg,
            "nlp_json": doc.to_json(),
            "query": q,
        },
    )
