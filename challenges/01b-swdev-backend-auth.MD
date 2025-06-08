# Software Developer: Identity-Provider task
## “Unit Logbook” – OpenID Connect + JWT setup

### Backstory
*Your platoon keeps a **paper logbook** for daily events in the field.*

*It would be handy if we had a simple multiplayer browser app for the case. This would improve the platoon's situational awareness as everybody could just easily check what's been done and what not.*

The Unit Logbook needs a secure way to identify users in the field and at HQ.  

Your mission is to stand up a **self-hosted, reproducible Identity Provider** and show that the Logbook API can verify a token issued by it.

---

## 1  Goal

1. Provision an **OpenID Connect** / OAuth 2.0 server **via code** (not click-ops).  
2. Create demo users & roles.  
3. Issue a JWT that the Logbook back-end can validate with the IdP’s JWKS.  
4. Make the IdP reachable on the internet *(free-tier VM or tunnel is fine).*  

> **Recommended stacks** (pick one): Keycloak, FusionAuth, Zitadel, ORY Kratos/Hydra, Dex + OAuth2-Proxy, Authelia, Authentik.  
> The deliverable must be reproducible from source (compose, Helm, Terraform…). Pure SaaS GUI setups (e.g. Auth0-only clicks) **will not score**.

---

## 2  Functional requirements

| ID | Requirement |
|----|-------------|
| **I-1** | Realm / tenant named **`unit-logbook`** (or similar). |
| **I-2** | Two roles: `logger`, `admin`. |
| **I-3** | Two users:<br> `demo.logger@example.com` → *logger*<br> `demo.admin@example.com` → *logger* + *admin* |
| **I-4** | **Public client** for React app – redirect URI `http://localhost:5173/*`. |
| **I-5** | **Confidential client** for back-end – `client_credentials` flow allowed. |
| **I-6** | `GET /.well-known/openid-configuration` returns 200 JSON. |
| **I-7** | README contains a **curl / script** that:<br>  1) gets an access-token (password, PKCE or client-cred) <br>  2) calls `https://<your-backend>/health` with `Authorization: Bearer <token>` and receives `200 OK`. |
| **I-8** | A single command (`docker compose up -d`, `helm install`, or `terraform apply`) reproduces the IdP including users/clients/roles **without manual GUI steps**. |

---

## 3  Technical constraints

* **Repro-as-code** – provide at least one of:  
  * `docker-compose.yml` (+ optional keycloak-config CLI JSON)  
  * Helm chart / Kustomize manifests  
  * Terraform + Ansible / cloud-init …  
* **Public access** – any of:  
  * Free micro-VM (Fly.io, Railway, Oracle Free, Render)  
  * Cloudflare Tunnel / ngrok to your laptop *(keep tunnel running until we test).*  
* **TLS** – HTTPS is mandatory (Let’s Encrypt, platform cert, or self-signed if documented with curl -k).  
---

## 4  Stretch goals

| Idea | Hint |
|------|------|
| **CI pipeline** | GitHub Actions that spins up IdP in Docker, runs `openid-client` tests, tears down. |
| **OIDC discovery mock** | Serve the IdP behind NGINX and add caching / rate-limit rules. |

---

## 5  Submission checklist

| ✔︎ | Item |
|----|------|
|    | `docker compose up -d` (or equivalent) stands up the IdP with users/clients pre-seeded. |
|    | `/.well-known/openid-configuration` reachable over HTTPS from the internet. |
|    | JWKS endpoint reachable; token verified by your demo script. |
|    | README contains links to test your setup. |
- [ ] Mail link to your forked repository to ictvmrekry.pvjjk at mil.fi.   