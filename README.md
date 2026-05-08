#PostgreSQL Vector Database Project
A PostgreSQL-based vector database system built using Python and the pgvector extension.
This project demonstrates how vector embeddings can be stored and managed efficiently using PostgreSQL for AI/ML-based applications such as face recognition and attendance systems
----
#Features
-PostgreSQL database integration using SQLAlchemy
-pgvector extension support
-Vector embedding storage
-Multiple relational tables for scalable system design
-Attendance and geofence-ready schema
-Simple and clean Python implementation
---
#Technologies Used
-Python 3
-PostgreSQL
-SQLAlchemy
-psycopg2
-pgvector
---
#Project Structure
postgres_vector_project/│
├── db.py
├── main.py
└── README.md
---
#Database Tables
The project contains the following 6 tables:
1. persons
Stores user/person details.
Column          Type
person_id       UUID
full_name       TEXT
email           TEXT
phone           TEXT
created_at     TIMESTAMP

2. faces
Stores face embeddings and image information.
Column         Type
face_id        UUID
person_id      UUI
Dencoding    VECTOR(128)
image_path     TEXT
confidence   DOUBLE PRECISION
created_at    TIMESTAMP

3. face_samples
Stores additional sample vectors.
Column         Type
sample_id      UUID
person_id      UUID
sample_path    TEXT
sample_vector VECTOR(128)
created_at    TIMESTAMP

4. attendance
Stores attendance records.
Column          Type
attendance_id   UUID
person_id       UUID
check_in       TIMESTAMP
check_out      TIMESTAMP
status          TEXT

5. geofence
Stores geofence location details.
Column          Type
geofence_id      UUID
location_name    TEXT
latitude        DOUBLE PRECISION
longitude       DOUBLE PRECISION
radius          DOUBLE PRECISION

6. logs
Stores activity logs.
Column       Type
log_id       UUID
person_id    UUID
action       TEXT
log_time    TIMESTAMP
---
#Installation
1. Clone Repository
git clone <your-repository-url>cd postgres_vector_project

2. Install Dependencies
pip install sqlalchemy psycopg2 pgvector

3. Start PostgreSQL
Ensure PostgreSQL is running on:
localhost:5433

4. Run the Project
python main.py
----
Expected Output
db.py loaded successfullyCreating all tables...All tables created successfullyDatabase setup completed successfully
---
#Verify Tables in PostgreSQL

Open PostgreSQL terminal:
psql -U postgres -h localhost -p 5433 -d postgres

Run:
\dt

#Expected tables:
attendance
face_samples
faces
geofence
logs
persons
---
#Future Improvements
-Face recognition integration
-Vector similarity search
-Attendance tracking automation
-REST API integration
-Real-time geofence validation
-Dashboard and analytics
---
Author
K. Nikhitha
GitHub: https://github.com/Nikhitha0927
