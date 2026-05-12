from sqlalchemy import (
    Column, String, Boolean, Text, DateTime, Integer,
    ForeignKey, CheckConstraint, Float
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base
from pgvector.sqlalchemy import Vector
import uuid

Base = declarative_base()

# ----------------------------
# ADMIN USERS
# ----------------------------
class AdminUser(Base):
    __tablename__ = "admin_users"

    admin_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    password_hash = Column(String, nullable=False)

    role = Column(String, CheckConstraint("role IN ('admin','super_admin')"))
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())


# ----------------------------
# PERSONS
# ----------------------------
class Person(Base):
    __tablename__ = "persons"

    person_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    employee_code = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    phone = Column(String)
    department = Column(String)

    role = Column(String, CheckConstraint("role IN ('employee','manager','admin')"))

    password_hash = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)
    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime)

    profile_photo = Column(Text)

    registered_by = Column(UUID(as_uuid=True), ForeignKey("admin_users.admin_id"))

    last_login = Column(DateTime)
    timezone = Column(String)

    default_geofence_id = Column(UUID(as_uuid=True), ForeignKey("geofence.geofence_id"))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


# ----------------------------
# GEOFENCE
# ----------------------------
class Geofence(Base):
    __tablename__ = "geofence"

    geofence_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    location_name = Column(String, nullable=False)

    latitude = Column(Float)
    longitude = Column(Float)
    radius = Column(Float)

    created_by = Column(UUID(as_uuid=True), ForeignKey("admin_users.admin_id"))

    is_active = Column(Boolean, default=True)

    zone_type = Column(String)

    allowed_start_time = Column(String)
    allowed_end_time = Column(String)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


# ----------------------------
# FACES
# ----------------------------
class Face(Base):
    __tablename__ = "faces"

    face_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    person_id = Column(UUID(as_uuid=True), ForeignKey("persons.person_id", ondelete="CASCADE"))

    encoding = Column(Vector(128))

    image_path = Column(Text)

    confidence = Column(Float)
    angle = Column(String)

    blur_score = Column(Float)
    quality_score = Column(Float)

    liveness_passed = Column(Boolean)

    face_width = Column(Integer)
    face_height = Column(Integer)

    eye_ratio = Column(Float)
    match_threshold = Column(Float)

    is_primary = Column(Boolean, default=False)

    capture_device = Column(String)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


# ----------------------------
# FACE SAMPLES
# ----------------------------
class FaceSample(Base):
    __tablename__ = "face_samples"

    sample_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    person_id = Column(UUID(as_uuid=True), ForeignKey("persons.person_id", ondelete="CASCADE"))

    sample_path = Column(Text)

    sample_vector = Column(Vector(128))

    angle_type = Column(String)

    quality_score = Column(Float)
    blur_score = Column(Float)

    liveness_passed = Column(Boolean)

    capture_order = Column(Integer)

    approved = Column(Boolean)
    rejected_reason = Column(Text)

    device_info = Column(Text)

    uploaded_at = Column(DateTime)

    created_at = Column(DateTime, server_default=func.now())


# ----------------------------
# ATTENDANCE
# ----------------------------
class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    person_id = Column(UUID(as_uuid=True), ForeignKey("persons.person_id", ondelete="CASCADE"))

    check_in = Column(DateTime)
    check_out = Column(DateTime)

    status = Column(String, CheckConstraint("status IN ('present','absent','late')"))

    latitude = Column(Float)
    longitude = Column(Float)

    geofence_id = Column(UUID(as_uuid=True), ForeignKey("geofence.geofence_id"))

    inside_geofence = Column(Boolean)
    suspicious_flag = Column(Boolean)

    confidence_score = Column(Float)

    device_id = Column(String)
    sync_status = Column(String)

    synced_at = Column(DateTime)

    image_path = Column(Text)
    attendance_type = Column(String)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


# ----------------------------
# LOGS
# ----------------------------
class Log(Base):
    __tablename__ = "logs"

    log_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    person_id = Column(UUID(as_uuid=True), ForeignKey("persons.person_id", ondelete="CASCADE"))

    action = Column(String)

    log_time = Column(DateTime, server_default=func.now())

    table_name = Column(String)
    record_id = Column(UUID(as_uuid=True))

    action_by = Column(UUID(as_uuid=True), ForeignKey("admin_users.admin_id"))

    old_data = Column(Text)
    new_data = Column(Text)

    ip_address = Column(String)

    severity = Column(String)
    module_name = Column(String)

    created_at = Column(DateTime, server_default=func.now())


# ----------------------------
# REGISTRATION SESSIONS
# ----------------------------
class RegistrationSession(Base):
    __tablename__ = "registration_sessions"

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    person_id = Column(UUID(as_uuid=True), ForeignKey("persons.person_id", ondelete="CASCADE"))

    current_step = Column(Integer)

    completed_angles = Column(Text)

    status = Column(String)

    started_at = Column(DateTime)
    expires_at = Column(DateTime)