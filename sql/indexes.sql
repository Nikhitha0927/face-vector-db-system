CREATE INDEX IF NOT EXISTS idx_persons_email
ON persons(email);

CREATE INDEX IF NOT EXISTS idx_persons_employee_code
ON persons(employee_code);

CREATE INDEX IF NOT EXISTS idx_attendance_person
ON attendance(person_id);

CREATE INDEX IF NOT EXISTS idx_faces_person
ON faces(person_id);

CREATE INDEX IF NOT EXISTS idx_logs_person
ON logs(person_id);

CREATE INDEX IF NOT EXISTS idx_face_samples_person
ON face_samples(person_id);