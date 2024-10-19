from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from schemas import Cocktail, AlcoholType
from cocktails import COCKTAILS
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Lists all cocktails
@app.get("/cocktails")
async def cocktails() -> list[Cocktail]:
    return [
        Cocktail(**c) for c in COCKTAILS
        ]

# Lists a specific cocktail by id
@app.get("/cocktails/{cocktail_id:int}")
async def cocktail(cocktail_id: int) -> Cocktail:
    if cocktail_id < 0 or cocktail_id >= len(COCKTAILS):
        raise HTTPException(status_code=404, detail="Cocktail not found")
    return Cocktail(**COCKTAILS[cocktail_id])

# Lists a random cocktail
@app.get("/cocktails/random")
async def random_cocktail() -> Cocktail:
    return Cocktail(**random.choice(COCKTAILS))

# Lists all alcohol types
@app.get("/alcohol")
async def alcohol() -> list[str]:
    return [a.value for a in AlcoholType]

# Finds all cocktails that contain a specific tag
@app.get("/tags/{tag}")
async def tags(tag: str) -> list[Cocktail]:
    if not tag:
        raise HTTPException(status_code=400, detail="No tag provided")
    
    normalized_tag = tag.replace("-", " ")

    matching_cocktails = [
        Cocktail(**c) for c in COCKTAILS
        if normalized_tag.lower() in (t.lower() for t in c["tags"])
    ]

    if not matching_cocktails:
        raise HTTPException(status_code=404, detail="Tag not found")

    return matching_cocktails

# favicon_path = "static/favicon.ico"
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.png")
