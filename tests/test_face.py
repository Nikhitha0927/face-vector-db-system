from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import text
from db import engine

def test_query():
    with engine.begin() as conn:
        conn.execute(text("SELECT * FROM persons"))

with ThreadPoolExecutor(max_workers=50) as executor:
    for _ in range(1000):
        executor.submit(test_query)

print("Stress test completed")