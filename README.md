# PostgreSQL Face Recognition Attendance System

## Overview

A PostgreSQL-based Face Recognition Attendance Management System developed using Python and PostgreSQL.

The project demonstrates:

* CRUD Operations
* Repository-Service Architecture
* Audit Logging
* Attendance Reporting View
* Database Indexing
* Backup Utility
* Unit Testing
* Stress Testing

---

## Project Structure

postgres_vector_project/

├── models/

├── repositories/

├── services/

├── sql/

│ ├── attendance_view.sql

│ ├── audit_logging.sql

│ └── indexes.sql

├── tests/

│ ├── test_face.py

│ ├── test_person.py

│ └── stress_test.py

├── utils/

│ └── backup.py

├── db.py

├── main.py

└── README.md

---

## Features

### Person Management

* Create Person
* Fetch Person
* Update Person
* Soft Delete Person

### Audit Logging

Tracks:

* CREATE
* UPDATE
* DELETE

Stored in logs table.

### Attendance Reporting

Attendance report view:

attendance_report

Displays:

* Employee Name
* Check In
* Check Out
* Status
* Geofence Status

### Backup Utility

Create SQL backups:

python utils/backup.py

### Database Indexing

Indexes created for performance optimization.

### Stress Testing

100 record insertion benchmark.

### Unit Testing

Pytest-based testing for:

* Person Service
* Face Service

---

## Installation

Install dependencies:

pip install sqlalchemy psycopg2-binary pytest

---

## Database Setup

Connect PostgreSQL:

psql -U postgres -h localhost -p 5433 -d postgres

Create views:

\i sql/attendance_view.sql

Create indexes:

\i sql/indexes.sql

---

## Run Project

python main.py

---

## Run Tests

export PYTHONPATH=.

pytest tests/test_face.py tests/test_person.py

Expected Output:

2 passed

---

## Run Stress Test

export PYTHONPATH=.

python tests/stress_test.py

Expected Output:

Inserted 100 records in X seconds

---

## Audit Log Verification

SELECT action, table_name, created_at
FROM logs;

---

## Technologies Used

* Python 3.13
* PostgreSQL 16
* SQLAlchemy
* Psycopg2
* Pytest

---

## Status

Completed

* CRUD Operations
* Audit Logging
* Attendance View
* Backup Utility
* Indexing
* Unit Testing
* Stress Testing








