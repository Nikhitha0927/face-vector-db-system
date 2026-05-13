# 📌 Face Vector DB System (PostgreSQL + pgvector)

## 🚀 Project Overview

This project is a PostgreSQL-based Face Recognition Database System using the pgvector extension to store and manage facial embeddings along with attendance, geofence, logging, and user management modules.

It is designed as a scalable AI-ready vector database architecture for real-time face recognition systems.

---

# 🧠 Key Features

- Face embedding storage using pgvector
- Multi-table relational database design
- Attendance tracking system with geolocation
- Geofence-based validation
- Audit logging system
- Face sample management for AI training/validation
- Admin authentication structure
- Registration workflow support
- Foreign key relationships for CRUD-ready integration

---

# 🗄️ Database Schema

## 1. Persons
Stores employee/user information.

### Columns
- employee_code
- full_name
- email
- phone
- department
- role
- password_hash
- timezone
- profile_photo
- default_geofence_id

---

## 2. Faces
Stores face embeddings and AI metadata.

### Columns
- encoding (VECTOR(128))
- confidence
- angle
- blur_score
- quality_score
- liveness_passed
- face_width
- face_height
- eye_ratio
- match_threshold
- capture_device

---

## 3. Face Samples
Stores multiple training images per user.

### Columns
- sample_vector (VECTOR(128))
- angle_type
- quality_score
- blur_score
- liveness_passed
- capture_order
- approval status
- uploaded_at

---

## 4. Attendance
Tracks employee attendance activity.

### Features
- GPS latitude & longitude
- Geofence validation
- Confidence score
- Suspicious activity detection
- Offline sync support
- Attendance type tracking

---

## 5. Geofence
Defines office/location boundaries.

### Features
- Latitude / Longitude
- Radius
- Zone type
- Allowed timing windows
- Active/inactive zones

---

## 6. Logs
Audit logging system.

### Features
- Action tracking
- Old vs new data (JSONB)
- Severity levels
- Module tracking
- IP address logging

---

## 7. Admin Users
Handles admin authentication.

### Features
- Username/password authentication
- Role-based access
- Active status management

---

## 8. Registration Sessions
Manages multi-step onboarding workflow.

### Features
- Current step tracking
- Session expiry handling
- Completed face angles

---

# ⚙️ Tech Stack

- Python
- PostgreSQL
- pgvector
- SQLAlchemy
- psycopg2

---

# 📦 Setup Instructions

## 1. Install Dependencies

```bash
pip install sqlalchemy psycopg2 pgvector alembic
```

## 2. Start PostgreSQL

```bash
psql -U postgres -h localhost -p 5433 -d postgres
```

## 3. Run Project

```bash
python main.py
```

---

# 📊 Tables Created

- persons
- faces
- face_samples
- attendance
- geofence
- logs
- admin_users
- registration_sessions

---

# ✅ Status

✔ Database schema completed  
✔ pgvector support enabled  
✔ Foreign key integration completed  
✔ CRUD-ready relational architecture  
✔ GitHub repository updated  

---

# 📌 Future Improvements

- FastAPI integration
- Face recognition pipeline
- Real-time attendance monitoring
- Frontend dashboard
- Docker deployment

---

# ⚡ Additional Features

- Alembic migration/version control integrated
- pgvector ivfflat indexes for optimized similarity search
- Automatic updated_at triggers
- Partial unique index for one primary face per person
- Foreign key constraints with relational integrity
- UUID-based primary keys using pgcrypto

---

# 👩‍💻 Author

K. Nikhitha

GitHub: https://github.com/Nikhitha0927