📌 Face Vector DB System (PostgreSQL + pgvector)
�� Project Overview

This project is a PostgreSQL-based Face Recognition Database System using pgvector extension to store and manage facial embeddings along with attendance, geofence, logs, and user management modules.

It replaces traditional storage systems with a scalable AI-ready vector database architecture.
---
🧠 Key Features
Face embedding storage using pgvector
Multi-table relational database design
Attendance tracking system with geolocation
Geofence-based validation
Audit logging system
Face sample management for training/validation
Admin authentication structure
Registration workflow support
---
🗄️ Database Schema
1. Persons
Stores user/employee information.
-employee_code
-full_name
-email
-department
-role
-authentication fields
-geofence mapping
2. Faces
Stores face embeddings and AI metadata.
-encoding (VECTOR 128)
-confidence score
-blur_score
-quality_score
-liveness_passed
-face dimensions
-capture metadata
3. Face Samples
Stores multiple training images per user.
-sample_vector (VECTOR 128)
-angle type
-quality & blur scoring
-approval status
4. Attendance
Tracks check-in / check-out events.
-GPS latitude & longitude
-geofence validation
-confidence score
-sync status (offline support)
-attendance type
5. Geofence
Defines location boundaries.
-latitude / longitude
-radius
-zone type
-allowed time windows
-activation status
6. Logs
Audit logging system.
-action tracking
-old vs new data (JSONB)
-severity levels
-module tracking
7. Admin Users
Handles admin authentication.
-username
-password_hash
-role-based access
-status control
8. Registration Sessions
Manages multi-step onboarding workflow.
-current step tracking
-session expiry
-completed face angles
---
⚙️ Tech Stack
Python
PostgreSQL
pgvector extension
SQLAlchemy
psycopg2
---
📦 Setup Instructions
1. Install dependencies
pip install sqlalchemy psycopg2 pgvector
2. Start PostgreSQL and create DB
psql -U postgres -h localhost -p 5433 -d postgres
3. Run project
python main.py
---
📊 Tables Created
persons
faces
face_samples
attendance
geofence
logs
admin_users
registration_sessions
---
✅ Status

✔ Database schema completed
✔ Vector support enabled
✔ Multi-module architecture ready
✔ GitHub updated
---
📌 Future Improvements
REST API (FastAPI integration)
Face recognition pipeline
Real-time attendance system
Frontend dashboard
Docker deployment
---
Author
K. Nikhitha
GitHub: https://github.com/Nikhitha0927

