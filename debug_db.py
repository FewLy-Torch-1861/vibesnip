from app import models, database
from sqlalchemy.orm import Session

db = database.SessionLocal()
snippets = db.query(models.Snippet).all()

print(f"Total Snippets: {len(snippets)}")
for s in snippets:
    print(f"ID: {s.id} | Title: {s.title}")

db.close()
