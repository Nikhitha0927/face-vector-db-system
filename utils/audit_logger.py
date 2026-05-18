from sqlalchemy import text
from db import engine


def log_action(person_id, action):

    with engine.begin() as conn:

        conn.execute(text("""
        INSERT INTO logs (
            log_id,
            person_id,
            action,
            created_at
        )
        VALUES (
            gen_random_uuid(),
            :person_id,
            :action,
            CURRENT_TIMESTAMP
        )
        """), {
            "person_id": person_id,
            "action": action
        })
