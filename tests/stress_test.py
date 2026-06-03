import time
from services.person_service import PersonService

service = PersonService()

start = time.time()

unique = int(time.time())

for i in range(100):

    service.register_person({
        "employee_code": f"LOAD{unique}_{i}",
        "full_name": f"User{i}",
        "email": f"user{unique}_{i}@gmail.com",
        "department": "QA",
        "role": "employee",
        "password_hash": "test"
    })

end = time.time()

print(f"Inserted 100 records in {end-start:.2f} seconds")