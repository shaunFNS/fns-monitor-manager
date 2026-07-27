# FNS Monitor Manager

> API-driven automation for Uptime Kuma built for Managed Service Providers.

FNS Monitor Manager is a FastAPI application that automates the creation and management of Uptime Kuma monitors using Playwright.

The goal of this project is to eliminate repetitive onboarding tasks by allowing monitors, groups, notifications, and client templates to be deployed through a simple REST API.

---

# Features

## Current

- ✅ Create Monitor Groups
- ✅ Create Ping Monitors
- ✅ Create HTTP Monitors
- ✅ Automatically assign monitors to groups
- ✅ FastAPI REST API
- ✅ Playwright browser automation
- ✅ Modular project architecture

## Planned

- ⏳ TCP Monitors
- ⏳ DNS Monitors
- ⏳ SSL Certificate Monitors
- ⏳ Keyword Monitors
- ⏳ Push Monitors
- ⏳ Notifications API
- ⏳ Monitor Templates
- ⏳ Client Deployment API
- ⏳ Web Dashboard
- ⏳ API Authentication
- ⏳ Docker Support

---

# Project Structure

```
app/
├── api/
│   ├── groups.py
│   ├── ping.py
│   └── http.py
│
├── core/
│   ├── auth.py
│   ├── browser.py
│   ├── config.py
│   ├── kuma_client.py
│   ├── kuma_ui.py
│   └── selectors.py
│
├── models/
│   ├── group.py
│   ├── ping.py
│   └── http.py
│
└── services/
    ├── groups.py
    ├── ping.py
    └── http.py

main.py
requirements.txt
```

---

# Architecture

```
REST API
    │
    ▼
FastAPI
    │
    ▼
Services
    │
    ▼
KumaClient
    │
    ▼
KumaUI
    │
    ▼
Playwright
    │
    ▼
Uptime Kuma
```

Keeping Playwright isolated inside the UI layer makes the API easier to maintain and extend.

---

# Requirements

- Python 3.11+
- FastAPI
- Playwright
- Uptime Kuma
- Chromium (Playwright)

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fns-monitor-manager.git
cd fns-monitor-manager
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Playwright

```bash
playwright install chromium
```

Run the API

```bash
uvicorn main:app --host 0.0.0.0 --port 8085
```

Open Swagger

```
http://YOURSERVER:8085/docs
```

---

# API Examples

## Create Group

**POST**

```
/api/groups
```

```json
{
  "name": "Example Client"
}
```

---

## Create Ping Monitor

**POST**

```
/api/ping
```

```json
{
  "group": "Example Client",
  "name": "Google DNS",
  "hostname": "8.8.8.8"
}
```

---

## Create HTTP Monitor

**POST**

```
/api/http
```

```json
{
  "group": "Example Client",
  "name": "Website",
  "url": "https://google.com"
}
```

---

# Future Client Deployment

The long-term vision is a single endpoint that deploys an entire monitoring package.

Example:

```json
{
  "client": "Example Client",
  "website": "https://google.com",
  "public_ip": "1.2.3.4",
  "templates": [
    "website",
    "internet",
    "synology",
    "unifi"
  ]
}
```

The API will automatically:

- Create the client group
- Create monitors
- Apply notification profiles
- Configure monitor settings
- Return a deployment summary

---

# Development Roadmap

## Phase 1

- [x] Groups
- [x] Ping
- [x] HTTP

## Phase 2

- [ ] TCP
- [ ] DNS
- [ ] SSL
- [ ] Keyword

## Phase 3

- [ ] Notification Management
- [ ] Tags
- [ ] Templates
- [ ] Variables

## Phase 4

- [ ] Client Deployment API
- [ ] Dashboard
- [ ] Authentication
- [ ] Docker Image

---

# Why This Exists

Creating monitoring manually for every client is repetitive and time-consuming.

FNS Monitor Manager turns client onboarding into an API call, allowing Managed Service Providers to deploy standardized monitoring quickly and consistently.

---

# License

MIT License

---

# Author

**Franke Network Solutions**

Website: https://frankenetworksolutions.com

Built to simplify client onboarding and monitoring automation for MSPs.
