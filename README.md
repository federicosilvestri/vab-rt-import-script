# VAB DB Analysis and Import

![](lord_voldemort.png)


A preprocessing and data migration pipeline for transitioning away from the legacy database ("Lord Voldemort") to an open-source stack.

---

## Requirements

- Python 3.x
- UV (Rust <3)
- A VPN connection to the source database
- Access to a running VAB-RT API instance

---

## Configuration

Copy `.env.example` to `.env` and fill in the connection parameters:

```bash
cp .env.example .env
```

---

## Database Connection

Set up a VPN connection to the source database, then configure the connection parameters in your `.env` file using `.env.example` as a reference.

---

## VAB-RT Import

### 1. Generate the API Client

```bash
./generate-api.sh
```

Or manually:

```bash
openapi-python-client generate --url http://localhost:8000/api/schema/
```

> **Note:** The generated client uses `strftime`, but VAB-RT expects standard date format. The `generate-api.sh` script handles this patch automatically.

### 2. Authenticate

Go to the [API token endpoint](http://localhost:8000/api/docs/#/auth/auth_create), obtain a token, and save the JSON response to `auth.json`.

### 3. Fetch Initial Data

```bash
cd vab_rt_import/importing
python fetch_initial.py
```

---