-- PERSONS

CREATE INDEX IF NOT EXISTS idx_persons_email
ON persons(email);

CREATE INDEX IF NOT EXISTS idx_persons_employee_code
ON persons(employee_code);

-- FACES

CREATE INDEX IF NOT EXISTS idx_faces_person_id
ON faces(person_id);

CREATE INDEX IF NOT EXISTS idx_faces_vector
ON faces
USING ivfflat (encoding vector_cosine_ops);

-- FACE SAMPLES

CREATE INDEX IF NOT EXISTS idx_face_samples_person_id
ON face_samples(person_id);

CREATE INDEX IF NOT EXISTS idx_samples_vector
ON face_samples
USING ivfflat (sample_vector vector_cosine_ops);

-- ATTENDANCE

CREATE INDEX IF NOT EXISTS idx_attendance_person_id
ON attendance(person_id);

CREATE INDEX IF NOT EXISTS idx_attendance_geofence_id
ON attendance(geofence_id);

-- LOGS

CREATE INDEX IF NOT EXISTS idx_logs_person_id
ON logs(person_id);

CREATE INDEX IF NOT EXISTS idx_logs_created_at
ON logs(created_at);