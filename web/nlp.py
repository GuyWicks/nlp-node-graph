from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.config import templates, debug
from app.lang import NLP

router = APIRouter()


@router.get("/nlp", response_class=HTMLResponse)
def get_nlp(
    request: Request,
    q: str = "",
):
    nlp = NLP()
    svg = nlp.visulize(q)
    doc = nlp.tokenize(q).to_json()

    node_data = []
    i = 1
    debug(doc)

    for t in doc["tokens"]:
        i += 1
        debug(t["lemma"])
        match t["pos"]:
            case "NOUN":
                node_data.append(
                    {
                        "color": "green",
                        "font": {"color": "white"},
                        "id": i,
                        "label": t["lemma"],
                        "shape": "box",
                        "size": 60,
                    }
                )
            case "PROPN":
                node_data.append(
                    {
                        "color": "green",
                        "font": {"color": "white"},
                        "id": i,
                        "label": t["lemma"],
                        "shape": "box",
                        "size": 60,
                    }
                )

    return templates.TemplateResponse(
        request=request,
        name="nlp.html.j2",
        context={
            "nlp": svg,
            "nlp_json": doc,
            "node_data": node_data,
            "query": q,
        },
    )
