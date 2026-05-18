def log_action(
    conn,
    person_id,
    action,
    table_name,
    record_id,
    old_data,
    new_data
):
    conn.execute(text("""
        INSERT INTO logs (
            person_id,
            action,
            table_name,
            record_id,
            old_data,
            new_data,
            created_at
        )
        VALUES (
            :person_id,
            :action,
            :table_name,
            :record_id,
            :old_data,
            :new_data,
            CURRENT_TIMESTAMP
        )
    """), {
        "person_id": person_id,
        "action": action,
        "table_name": table_name,
        "record_id": record_id,
        "old_data": old_data,
        "new_data": new_data
    })