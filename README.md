# Face Vector DB System

PostgreSQL + pgvector based backend database system with CRUD operations, vector indexing, audit logging, repository/service architecture, and attendance management support.

---

# Features

* PostgreSQL database integration
* pgvector extension support
* UUID primary keys using `gen_random_uuid()`
* Repository and service layer architecture
* CRUD operations
* Foreign key relationships
* Audit logging support
* Attendance and geofence management
* Soft delete implementation
* Vector similarity indexing using `ivfflat`
* Automated backup support
* Alembic migration support
* Pytest testing support

---

# Technologies Used

* Python
* PostgreSQL
* SQLAlchemy
* pgvector
* Alembic
* Pytest

---

# Project Structure

```bash
postgres_vector_project/
│
├── db.py
├── main.py
├── requirements.txt
├── .env
├── backup.sh
│
├── repositories/
│   ├── __init__.py
│   ├── person_repository.py
│   ├── face_repository.py
│   └── attendance_repository.py
│
├── services/
│   ├── __init__.py
│   ├── person_service.py
│   └── face_service.py
│
├── tests/
│   ├── __init__.py
│   ├── test_person.py
│   └── test_face.py
│
├── utils/
│   ├── __init__.py
│   ├── audit_logger.py
│   └── backup.py
│
└── backups/
```

---

# Database Tables

## persons

Stores employee and user information.

## faces

Stores face vector embeddings using pgvector.

## face_samples

Stores additional face sample vectors.

## attendance

Stores attendance logs with geofence support.

## geofence

Stores office/location geofence data.

## logs

Stores audit logs and activity tracking.

## admin_users

Stores admin authentication data.

## registration_sessions

Stores registration workflow session data.

---

# PostgreSQL Extensions

```sql
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Nikhitha0927/face-vector-db-system.git
```

## Navigate to Project

```bash
cd face-vector-db-system
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5433/postgres
```

---

# Run Project

```bash
python main.py
```

---

# Run Tests

```bash
python -m pytest
```

---

# Backup Database

Give permission:

```bash
chmod +x backup.sh
```

Run backup:

```bash
./backup.sh
```

Backups will be stored inside:

```bash
backups/
```

---

# Features Implemented

* CRUD operations
* Foreign keys
* UUID generation
* Soft delete support
* UTC timestamps
* Audit logging
* Repository/service architecture
* Vector similarity indexes
* Partial unique indexes
* Query optimization indexes
* Attendance reporting support
* pgvector integration
* Alembic migration setup
* Automated backup support
* Stress/performance ready schema

---

# Indexes Added

* Foreign key indexes
* `ivfflat` vector indexes
* Partial unique indexes
* Attendance indexes
* Log indexes

---

# Constraints Added

* NOT NULL constraints
* UNIQUE constraints
* CHECK constraints
* Foreign key constraints

---

# Testing

Pytest is used for testing CRUD operations and database functionality.

```bash
python -m pytest
```

---

# GitHub Repository

https://github.com/Nikhitha0927/face-vector-db-system

