from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/snippets/{snippet_id}", response_class=JSONResponse)
async def get_snippet_json(snippet_id: int, db: Session = Depends(get_db)):
    print(f"DEBUG: fetching snippet id {snippet_id} (type: {type(snippet_id)})")
    snippet = db.query(models.Snippet).filter(models.Snippet.id == snippet_id).first()
    if not snippet:
        print(f"DEBUG: Snippet {snippet_id} not found in DB")
        raise HTTPException(status_code=404, detail="Snippet not found")
    return {
        "id": snippet.id,
        "title": snippet.title,
        "language": snippet.language,
        "code": snippet.code,
        "tags": snippet.tags
    }

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, page: int = 1, db: Session = Depends(get_db)):
    limit = 20
    offset = (page - 1) * limit
    snippets = db.query(models.Snippet).order_by(models.Snippet.id.desc()).offset(offset).limit(limit + 1).all()
    has_next = len(snippets) > limit
    snippets = snippets[:limit]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "snippets": snippets,
        "page": page,
        "has_next": has_next,
        "q": ""
    })

@app.get("/search", response_class=HTMLResponse)
async def search_snippets(request: Request, q: str = "", page: int = 1, db: Session = Depends(get_db)):
    limit = 20
    offset = (page - 1) * limit
    query = db.query(models.Snippet)

    if q:
        query = query.filter(
            (models.Snippet.title.ilike(f"%{q}%")) | 
            (models.Snippet.tags.ilike(f"%{q}%")) |
            (models.Snippet.language.ilike(f"%{q}%"))
        )
    else:
        query = query.order_by(models.Snippet.id.desc())

    snippets = query.offset(offset).limit(limit + 1).all()
    has_next = len(snippets) > limit
    snippets = snippets[:limit]

    return templates.TemplateResponse("snippet_list.html", {
        "request": request,
        "snippets": snippets,
        "page": page,
        "has_next": has_next,
        "q": q
    })

@app.post("/add", response_class=HTMLResponse)
async def save_snippet(
    request: Request,
    snippet_id: str = Form(None), # Optional ID for updates
    title: str = Form(...),
    language: str = Form(...),
    code: str = Form(...),
    tags: str = Form(""),
    db: Session = Depends(get_db)
):
    if not title.strip() or not code.strip():
        raise HTTPException(status_code=400, detail="Title and Code are required")

    if snippet_id and snippet_id != "null" and snippet_id.strip():
        # Update existing
        snippet = db.query(models.Snippet).filter(models.Snippet.id == int(snippet_id)).first()
        if snippet:
            snippet.title = title
            snippet.language = language
            snippet.code = code
            snippet.tags = tags
    else:
        # Create new
        new_snippet = models.Snippet(title=title, language=language, code=code, tags=tags)
        db.add(new_snippet)
    
    db.commit()
    
    # Return updated list (first page only)
    limit = 20
    snippets = db.query(models.Snippet).order_by(models.Snippet.id.desc()).limit(limit + 1).all()
    has_next = len(snippets) > limit
    snippets = snippets[:limit]

    return templates.TemplateResponse("snippet_list.html", {
        "request": request,
        "snippets": snippets,
        "page": 1,
        "has_next": has_next,
        "q": ""
    })

@app.delete("/delete/{snippet_id}", response_class=HTMLResponse)
async def delete_snippet(request: Request, snippet_id: int, db: Session = Depends(get_db)):
    snippet = db.query(models.Snippet).filter(models.Snippet.id == snippet_id).first()
    if snippet:
        db.delete(snippet)
        db.commit()
    return "" # Return nothing to remove element from DOM
