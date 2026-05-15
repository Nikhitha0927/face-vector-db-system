import time
from db import engine
from sqlalchemy import text

start = time.time()

with engine.begin() as conn:
    conn.execute(text("SELECT * FROM persons"))

end = time.time()

print("Execution Time:", end - start)