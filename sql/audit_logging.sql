CREATE OR REPLACE FUNCTION audit_log_function()

RETURNS TRIGGER AS $$

BEGIN

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

        NEW.person_id,
        TG_OP,
        TG_TABLE_NAME,
        NEW.person_id,
        row_to_json(OLD),
        row_to_json(NEW),
        CURRENT_TIMESTAMP
    );

    RETURN NEW;

END;

$$ LANGUAGE plpgsql;