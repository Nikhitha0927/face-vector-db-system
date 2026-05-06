📌 Face Vector Database System (PostgreSQL + pgvector)
📖 Project Overview

This project demonstrates a PostgreSQL-based vector database system built using Python. It replaces traditional Excel-based storage with a scalable database solution capable of storing and querying vector embeddings using the pgvector extension.

The system is designed to store feature embeddings and perform similarity search using vector distance, making it suitable for AI/ML-based applications.
--------------------------------------------------------------------
## 🎯 Objective

- Establish and interact with a PostgreSQL database using Python  
- Implement vector storage using pgvector  
- Perform efficient similarity search using vector distance  
- Build a modular backend using SQLAlchemy ORM  
- Implement CRUD operations for database management  
--------------------------------------------------------------------
🛠️ Technologies Used
-Python 3.10+
-PostgreSQL
-pgvector extension
-SQLAlchemy ORM
-psycopg2
-pip (package manager)
--------------------------------------------------------------------
📂 Project Structure
postgres_vector_project/
│
├── config.py        # Database configuration
├── db.py            # Database engine and session setup
├── models.py        # ORM models (Face table)
├── schema.py        # Table creation script
├── crud.py          # CRUD operations
└── main.py          # Testing & execution script
--------------------------------------------------------------------
Key Features
-PostgreSQL database integration using Python
-Vector storage using pgvector
-Efficient similarity search using L2 distance
-SQLAlchemy ORM-based architecture
-Modular and scalable backend design
-Insert and retrieve vector embeddings
-Clean separation of database layers
--------------------------------------------------------------------
⚙️ Setup Instructions
1️⃣ Install dependencies

pip install sqlalchemy psycopg2-binary pgvector

2️⃣ Create PostgreSQL database

CREATE DATABASE face_vector_db;

3️⃣ Enable vector extension

CREATE EXTENSION IF NOT EXISTS vector;

4️⃣ Run table creation script

python schema.py

5️⃣ Run the system

python main.py
--------------------------------------------------------------------
📊 Functionality
✔ Insert Data

Stores name + vector embedding into database.

✔ Retrieve Data

Fetches all stored records.

✔ Similarity Search

Finds closest matching vector using:
L2 distance (Euclidean similarity)
--------------------------------------------------------------------
🧪 Example Output
db.py loaded successfully
schema.py STARTED
Creating tables...
Tables created successfully

Inserting data...
Searching match...
Matched person: Nikhitha

Concepts Learned
PostgreSQL database design
Vector databases and embeddings
SQLAlchemy ORM architecture
pgvector similarity search
Backend modularization
Python database integration
--------------------------------------------------------------------
Future Improvements
REST API using FastAPI
Real-time face recognition integration
Web dashboard for attendance system
Cloud database deployment
--------------------------------------------------------------------
👩‍💻 Author

Nikhitha

GitHub: Nikhitha0927
--------------------------------------------------------------------
📌 Note

This project focuses only on database + vector backend setup.
Face recognition integration is excluded as per assignment requirements.
