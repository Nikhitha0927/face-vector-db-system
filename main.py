from db import SessionLocal, create_tables
from sqlalchemy import text
import uuid

# Step 1: Create table
create_tables()

session = SessionLocal()

print("Inserting data...")

# Example vector (dummy 128-d vector)
sample_vector = "[" + ",".join(["0.1"] * 128) + "]"

session.execute(text("""
INSERT INTO faces (person_id, name, encoding, image_path, confidence)
VALUES (:pid, :name, :enc, :img, :conf)
"""), {
    "pid": str(uuid.uuid4()),
    "name": "Nikhitha",
    "enc": sample_vector,
    "img": "dataset/nikhitha.jpg",
    "conf": 0.95
})

session.commit()

print("Data inserted successfully")

# Fetch data
print("Fetching data...")

result = session.execute(text("SELECT id, name, confidence FROM faces"))

for row in result:
    print(row)

session.close()
