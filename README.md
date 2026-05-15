# Face Vector DB System (PostgreSQL + pgvector)

## Project Overview

This project is a PostgreSQL-based backend database architecture using pgvector for vector similarity search and scalable attendance management.

The system includes:

- Persons management
- Attendance tracking
- Geofence validation
- Audit logging
- Face vector storage
- Registration workflow
- Admin management
- Alembic migrations
- Repository & service architecture

---

## Tech Stack

- Python
- PostgreSQL
- pgvector
- SQLAlchemy
- Alembic
- psycopg2
- python-dotenv

---

## Features

- UUID primary keys
- Foreign key relationships
- pgvector ivfflat indexes
- UTC timestamps
- Soft delete support
- Audit logging
- Attendance analytics
- Backup automation
- CRUD-ready structure
- Repository layer
- Service layer
- Migration support using Alembic

---

## Tables

- persons
- faces
- face_samples
- attendance
- geofence
- logs
- admin_users
- registration_sessions

---

## Setup

### Install Dependencies

```bash
pip install -r requirements.txt

Configure Environment

Create .env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5433/postgres

Run Project
python main.py

Alembic Migration
alembic revision -m "initial schema"
alembic upgrade head

PostgreSQL Extensions


vector


pgcrypto



Performance Features


pgvector similarity search


Foreign key indexes


Partial unique indexes


Optimized attendance queries


Stress testing support



Author
K. Nikhitha
GitHub:
https://github.com/Nikhitha0927
Save:- `CTRL + O`- Enter- `CTRL + X`Then push:```bash id="l7ydc7"git add .git commit -m "Updated README documentation"git push
