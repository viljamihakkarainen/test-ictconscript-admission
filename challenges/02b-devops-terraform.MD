# DevOps / Infra-Engineer – Terraform Task
## “Unit Logbook” – IaC with Terraform

### Backstory
*Your platoon keeps a **paper logbook** for daily events in the field.*

*It would be handy if we had a simple multiplayer browser app for the case. This would improve the platoon's situational awareness as everybody could just easily check what's been done and what not.*

The Unit Logbook needs a repeatable, one-command way to spin up the stack on fresh infrastructure.  

Your job is to stand up a tiny **static site** with Terraform that serves **“Unit Logbook OK”** over HTTPS on your own sub-domain.

---

## 1 Goal

1. Terraform must create:

   | Resource | Minimum spec (choose any cloud/provider you like) |
   |-----------|--------------------------------------------------|
   | **Storage / Site host** | AWS S3 static website, Google Cloud Storage Website, Azure Blob Static Site, Cloudflare Pages project, Netlify site, or equivalent. |
   | **HTTPS endpoint** | CDN / load-balancer with TLS (ACM, Cloudflare, GCP Managed Cert, Let’s Encrypt via provider). |
   | **DNS record** | `logbook.<your-domain>` → the HTTPS endpoint. |

2. Upload a single `index.html` file that outputs **“Unit Logbook OK”**.  
3. After `terraform apply`, we can hit **`https://logbook.<your-domain>`** and see the text with a valid padlock.

---

## 2 Functional requirements

| ID | Requirement |
|----|-------------|
| **T-1** | `terraform init && terraform apply -auto-approve` completes without manual tweaks. |
| **T-2** | Site content (`index.html`) is uploaded automatically (via `aws_s3_object`, `google_storage_bucket_object`, Terraform Cloudflare Pages deploy block, etc.). |
| **T-3** | HTTPS certificate is provisioned and attached by Terraform (ACM, Google Certificate Manager, Cloudflare “Full strict” cert, etc.). |
| **T-4** | Only **80/443** (or provider-managed ports) are open; no other public services. |
| **T-5** | `terraform fmt` and `validate` pass with zero errors. |
| **T-6** | All providers & modules are version-pinned (e.g. `~> 5.32`), and Terraform required version pinned (e.g. `>= 1.7.0`). |

---

## 3 Suggested project structure

devops-terraform/
main.tf
variables.tf
outputs.tf
versions.tf # provider blocks + terraform block
site/index.html # "Unit Logbook OK"
README.md

---

## 4 Variables to expose

| Variable | Example default | Description |
|----------|-----------------|-------------|
| `domain` | `"example.com"` | Base domain you control |
| `subdomain` | `"logbook"`  | Will become `logbook.example.com` |
| `region` | `"eu-west-1"` (if applicable) | Cloud region |
| `contact_email` | `"ops@example.com"` | For TLS certificate registration |

*(Add any provider-specific API tokens via environment variables / TF Cloud secrets, **not** in code.)*

---

## 5 Stretch goals

|   | Idea |
|----|------|
| Remote state | Store state in Terraform Cloud free tier or S3 + DynamoDB. |
| CI pipeline | GitHub Actions: `fmt`, `validate`, `tflint`, `terraform plan`. |
| Content update | `github_repository_file` → automatic redeploy when `site/index.html` changes. |

---

## 6 Submission checklist

| ✔︎ | Item |
|----|------|
|    | Folder `devops-terraform/` contains all `.tf` files and `site/index.html`. |
|    | `terraform fmt` + `validate` succeed. |
|    | `terraform apply` from a fresh clone produces an HTTPS URL printing “Unit Logbook OK”. |
|    | Output variables include the public URL. |
|    | Provider & module versions pinned. |
|    | README contains links to test your setup. |
- [ ] Return your done Test to ```ictvmhaku.pvjjk at mil.fi```.