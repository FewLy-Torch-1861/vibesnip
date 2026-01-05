# Project Context & Reminders

## Project: VibeSnip
A terminal-inspired, keyboard-centric code snippet manager using FastAPI, HTMX, and TailwindCSS.

**Tech Stack:**
- **Backend:** Python (FastAPI), SQLAlchemy, SQLite
- **Frontend:** HTML (Jinja2 Templates), HTMX, TailwindCSS (CDN)
- **Editor:** Monaco Editor (CDN), Highlight.js (CDN)

## Key Locations
- **Logic:** `main.py` (Backend routes), `templates/base.html` (Frontend JS logic like themes, editor init)
- **Styles:** `static/styles.css` (Custom overrides), `templates/base.html` (Theme variable logic)
- **Database:** `vibesnip.db` (SQLite file, created on run)

## Commands
- **Run Server:** `uvicorn main:app --reload`
- **Access:** `http://127.0.0.1:8000`

## Workflow
- When asked to commit, always view what's changing before every commit (`git diff HEAD`).
- After committing, make a new tag (e.g., `v1.1.1`) if requested.
- Create a GitHub release after tagging if requested.
