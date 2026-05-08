from db import SessionLocal, create_tables
from sqlalchemy import text
import uuid

create_tables()

session = SessionLocal()

print("Inserting data...")

sample_vector = "[" + ",".join(["0.1"] * 128) + "]"

session.execute(text("""
INSERT INTO faces (
    person_id,
    name,
    encoding,
    image_path,
    confidence
)
VALUES (
    :pid,
    :name,
    :encoding,
    :img,
    :conf
)
"""), {
    "pid": str(uuid.uuid4()),
    "name": "Nikhitha",
    "encoding": sample_vector,
    "img": "dataset/nikhitha.jpg",
    "conf": 0.95
})

session.commit()

print("Data inserted successfully")

result = session.execute(text("""
SELECT person_id, name, confidence
FROM faces
"""))

for row in result:
    print(row)

session.close()
