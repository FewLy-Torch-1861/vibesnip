# VibeSnip Development Plan

## Goal
Build a privacy-focused, TUI-themed code snippet manager called **VibeSnip**.

## Tech Stack
*   **Backend:** Python (FastAPI) - fast, lightweight, perfect for CLI lovers.
*   **Frontend:** HTML + HTMX - simple, dynamic interactions without heavy JS frameworks.
*   **Styling:** Tailwind CSS (via CDN) - for that crisp, custom "terminal" aesthetic.
*   **Editor:** Monaco Editor - for a rich code editing experience.
*   **Database:** SQLite - local, simple, file-based.

## Features (Completed)
- [x] **Dashboard:** List all snippets with a retro terminal look.
- [x] **Add Snippet:** Collapsible form with Monaco Editor integration.
- [x] **Search:** Instant "fuzzy-style" filtering (powered by HTMX).
- [x] **Copy:** One-click copy to clipboard.
- [x] **Delete:** Secure deletion with confirmation modal.
- [x] **Edit:** Update existing snippets seamlessly.
- [x] **Theme Customization:** Extensive theme picker + custom theme creator.
- [x] **Syntax Highlighting:** Highlight.js for viewing, Monaco for editing.
- [x] **Keyboard Shortcuts:** `j/k` navigation, `e` to edit, `/` to search.

## Future Ideas / Backlog
1.  **Tag Management:** Clickable tags to instantly filter the list.
2.  **Backup/Export:** Export all snippets to JSON/ZIP for safekeeping.
3.  **Shortcuts Help:** A modal (`?`) showing all available keyboard shortcuts.
4.  **Raw View:** A simple endpoint to view raw code content (useful for curling).
5.  **Multi-file Snippets:** Support storing multiple files in one snippet entry.

## Next Steps
Refine the UI/UX based on usage and address any bugs in the editor integration.
