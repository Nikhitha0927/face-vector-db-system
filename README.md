# Face Vector DB System

PostgreSQL backend system with pgvector support, relational schema, CRUD operations, audit logging, backup automation, and testing.

## Features

* PostgreSQL + pgvector integration
* Relational database schema
* UUID primary keys
* Foreign key relationships
* CRUD operations
* Repository and service layers
* Audit logging
* Soft delete support
* Automated backup script
* Attendance reporting view
* pgvector similarity indexes
* Pytest testing
* Stress test setup

---

## Technologies

* Python
* PostgreSQL
* SQLAlchemy
* pgvector
* Alembic
* pytest

---

## Project Structure

```text
postgres_vector_project/
│
├── db.py
├── main.py
├── .env
│
├── repositories/
├── services/
├── tests/
├── sql/
├── utils/
├── backups/
└── alembic/
```

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5433/postgres
```

Run project:

```bash
python main.py
```

Run tests:

```bash
export PYTHONPATH=.
pytest tests/
```

---

## Database Features

* pgvector vector search
* ivfflat indexes
* audit logs
* UTC timestamps
* automatic updated_at triggers
* soft delete support
* attendance reporting view

---

## Backup

Run backup script:

```bash
python utils/backup.py
```

---

## GitHub

https://github.com/Nikhitha0927/face-vector-db-system


