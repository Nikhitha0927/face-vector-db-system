CREATE OR REPLACE FUNCTION log_activity(
    p_action TEXT,
    p_table_name TEXT,
    p_record_id UUID,
    p_person_id UUID DEFAULT NULL
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO logs (
        action,
        table_name,
        record_id,
        person_id,
        created_at
    )
    VALUES (
        p_action,
        p_table_name,
        p_record_id,
        p_person_id,
        CURRENT_TIMESTAMP
    );
END;
$$ LANGUAGE plpgsql;

SELECT log_activity(
    'TEST',
    'persons',
    gen_random_uuid(),
    NULL
);