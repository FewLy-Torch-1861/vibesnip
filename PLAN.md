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
- [x] Keyboard Shortcuts: `j/k` navigation, `e` to edit, `/` to search.
- [x] Raw View: A simple endpoint to view raw code content (useful for curling).
- [x] Shortcuts Help: A modal (`?`) showing all available keyboard shortcuts.
- [x] Command Palette: A `Ctrl+K` (or `Meta+K`) command palette for rapid navigation and actions.
- [x] **Backup/Export:** Export and Import all snippets to/from JSON for safekeeping.

## Future Ideas / Backlog
1.  **Tag Management:** Clickable tags to instantly filter the list.
3.  **Gist Sync:** Import from and export to GitHub Gists.
4.  **Collection Folders:** Grouping snippets into logical folders or projects.
5.  **Editor Settings:** Customizing Monaco's font size, line numbers, and word wrap via a settings panel.
6.  **Multi-file Snippets:** Support storing multiple files in one snippet entry.

## Next Steps
Refine the UI/UX based on usage and address any bugs in the editor integration.
