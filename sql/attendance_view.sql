CREATE OR REPLACE VIEW attendance_report AS
SELECT
    p.full_name,
    a.check_in,
    a.check_out,
    a.status,
    a.inside_geofence
FROM attendance a
JOIN persons p
ON a.person_id = p.person_id;