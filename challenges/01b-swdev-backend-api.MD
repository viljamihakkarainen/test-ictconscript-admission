# Software Developer: Backend Task
## “Unit Logbook” (REST API)

### Backstory
*Your platoon keeps a **paper logbook** for daily events in the field.*

*It would be handy if we had a simple multiplayer browser app for the case. This would improve the platoon's situational awareness as everybody could just easily check what's been done and what not.*

Your job is to deliver a **small REST API** that other apps (e.g. the front-end task) could call.

---

## 1  Goal

Build and deploy a publicly reachable REST service that

1. **Persists & serves** log entries from a **SQLite database** 
2. **Accepts** new log entries via POST and stores them in the same database.  
3. Exposes a simple **health-check** endpoint.


> **Technology is your choice** – FastAPI, Flask, Express, Go Chi, Rust Actix, Spring Boot, .NET Minimal API … anything you can containerise and deploy.

---

## 2 Functional requirements

| ID | Requirement |
|----|-------------|
| **B-1** | **Database** to persist log entries. Example of what data should be held is at `sample-data/data.json`. |
| B-2 | `GET /entries` returns all entries, newest first (JSON array). |
| B-3 | `GET /entries/<id>` returns a single entry or `404` if not found. |
| B-4 | `POST /entries` accepts JSON:<br>  `title` (string ≤ 120),<br>  `body` (string),<br>  optional `lat`, `lon` (numbers).<br>The server assigns `id` and `isoTime`, inserts row, and returns it. |
| B-5 | `GET /health` returns status 200, body `"OK"`. |

---

## 3  Technical constraints

* **Endpoints** must speak JSON over HTTP.  Accept/Content-Type = `application/json`.  
* **Validation errors** should respond with HTTP 4xx and an explanatory JSON message.  
* Provide either  
  * an **OpenAPI / Swagger** document **or**  
  * a short section in your README describing each route & payload.
* Include a **Dockerfile** (`docker build . && docker run -p 8000:8000 …` starts the server).

---

## 4  Deployment (mandatory)

Deploy the service to **any free-tier PaaS** or container host, for example

* Fly.io   `fly launch`  
* Railway.app   `railway up`  
* Render.com   Docker web service  
* GitHub Actions → GitHub Pages (Static Site Hosting with Cloudflare Workers)  
* Vercel Serverless (if your stack fits)

Add the **public base URL** to your fork’s root README.

---

## 5  Stretch goals

| Idea | Hint |
|------|------|
| Unit tests  | ≥ 2 tests (e.g. pytest, Jest, Go test) covering happy & error paths. |
| CI pipeline | GitHub Actions: build image, run tests, push to container/image repo of choice. |


---

## 6  Submission checklist

| ✔︎ | Item |
|----|------|
|    | `docker build .` succeeds and `docker run -p 8000:8000` serves the API locally. |
|    | Public URL in root README responds to `GET /health` with `200 OK`. |
|    | `GET /entries` returns the 10 sample items. |
|    | README contains route docs **or** OpenAPI spec link. |
- [ ] Return your done Test to ```ictvmhaku.pvjjk at mil.fi```.                  
