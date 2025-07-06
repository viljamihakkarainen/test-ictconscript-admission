# Software Developer: Frontend Task  
## “Unit Logbook” frontend app

### Backstory
*Your platoon keeps a **paper logbook** for daily events in the field.*

*It would be handy if we had a simple multiplayer browser app for the case. This would improve the platoon's situational awareness as everybody could just easily check what's been done and what not.*

You’ve received sample data (*`sample-data/entries.json`*) and have 8 hours to prove the concept.


---

## 1  Goal
Build a frontend application that
1. **Lists** existing log entries from `sample-data/entries.json`.  
2. **Adds** new entries via a modal or drawer.  
3. **Is deployed to GitHub Pages** (mandatory for evaluation) OR if it's mobile app, have a binary at Releases though Github Pages deployment is preferable even then.

---

## 2  Functional requirements

| ID  | Requirement                                                                                                  |
|-----|--------------------------------------------------------------------------------------------------------------|
| F-1 | Show the list in reverse chronological order (newest first).                                                 |
| F-2 | “New entry” let's  **title** and **body** (free text) and optional **location** (lat, lon).|
| F-3 | Submitted entries appear immediately in the list.   

---

## 3  Technical constraints

* **Data source** – load or import `sample-data/entries.json` (served by Pages).  
  *Tip: use `fetch('./sample-data/entries.json')`; GitHub Pages will serve it at the same relative path.*  
* **Deployment** – publish `dist/` to **GitHub Pages** (e.g. `npm run deploy` with `gh-pages`). Add the public URL to your fork’s root README.

---

## 4  Stretch goals (optional)

* **Mini-map thumbnail** (Leaflet, MapLibre…) for log entries with coordinates.  


---

## 5  Submission checklist

- [ ] GitHub Pages deployment live.
- [ ] 
  URL in your fork’s README.
- [ ] Return your done Test to ```ictvmhaku.pvjjk at mil.fi```.