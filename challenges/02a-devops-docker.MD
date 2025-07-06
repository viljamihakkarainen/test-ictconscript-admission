# DevOps / Infra Engineer: Docker Compose task
## “Unit Logbook” – Docker-Compose Stack with Automated TLS & CI Deploy

### Backstory
*Your platoon keeps a **paper logbook** for daily events in the field.*

*It would be handy if we had a simple multiplayer browser app for the case. This would improve the platoon's situational awareness as everybody could just easily check what's been done and what not.*

The Unit Logbook needs an infra bundle that can be spinned to any target server easily. 

Your assignment is to deliver a **Docker Compose stack** that exposes a simple **hello-world service** over HTTPS with free Let’s Encrypt certificates, plus an automated deploy pipeline.

---

## 1  Goal

1. Define a **`docker-compose.yml`** stack that includes  
   * **reverse proxy** (nginx, Traefik, or Caddy)  
   * **hello-world container** (plain nginx serving `index.html` with “Unit Logbook OK”)  
   * optional **log forwarding** or **health-check** side-container.  
2. Obtain and renew **Let’s Encrypt TLS** certificates automatically.  
3. Ship a **CI-based deploy** (GitHub Actions) that, on every push to `main`, redeploys the stack to a eg. free-tier VPS, container platform, your homeserver behind a DDNS or other service of your choice.  


---

## 2  Functional requirements

| ID | Requirement |
|----|-------------|
| C-1 | `docker compose up -d` locally starts the proxy on port 443 and the hello-world service on 8080 (internal). |
| C-2 | Reverse proxy routes `https://DOMAIN/` → hello-world container and returns HTTP 200 with text “Unit Logbook OK”. |
| C-3 | First run triggers automatic Let’s Encrypt certificate issuance for **`DOMAIN`**. |
| C-4 | A **GitHub Actions workflow** builds (if needed) and deploys the stack on push to `main`: <br> • SSH to VPS **or** `fly deploy` / `railway up` / `docker login && docker run`… |
| C-5 | Workflow uses **encrypted secrets** (`SSH_KEY`, `FQDN`, `EMAIL`…). |
| C-6 | All images in `docker-compose.yml` use explicit semantic-version tags (e.g. `nginx:1.27.0-alpine`). |

---

## 3  Technical constraints

* **Reverse-proxy choice** – Traefik v2, Caddy 2, or nginx with `certbot` / `acme.sh`.  
* **Hosting target** – free tier is fine (Fly.io, Oracle Arm Ampere, CapRover, Dokku, Render, Railway, Hetzner CX11 + Cloud DNS…).  
* **DNS** – use a sub-domain you control (e.g. `logbook-<yourname>.example.org`). Synthetic (`duckdns.org`, `nip.io`) is acceptable.  
* **Zero manual steps** except for starting the docker compose.

---

## 4  Stretch goals

| Idea | Hint |
|------|------|
| Development | A "docker-compose-dev.yml" when ran, overwrites your Let's Encrypt setup with eg. mkcert for running the compose in local/development environment. |
| Version tags |  Pin all container images to **immutable version tags** (no `:latest`).    |

---

## 5  Submission checklist

| ✔︎ | Item |
|----|------|
|    | `docker compose up -d` locally starts stack; `curl -k https://localhost` prints “Unit Logbook OK”. |
|    | **Public URL** of the deployment included in root README, and it serves valid Let’s Encrypt certificate. |
|    | GitHub Actions run visible in your fork shows last successful deploy. |
|    | `README.md` documents chosen host, deploy steps, and renewal strategy. |
- [ ] Return your done Test to ```ictvmhaku.pvjjk at mil.fi```.