--
-- PostgreSQL database dump
--

\restrict Dzvj1ztjRCJqhff8ppm8yydu9tb8I2nIFDOcxezGbJ5Zz4aHUZR1UbbknrbpBTS

-- Dumped from database version 16.13 (Homebrew)
-- Dumped by pg_dump version 16.13 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS '';


--
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


--
-- Name: vector; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS vector WITH SCHEMA public;


--
-- Name: EXTENSION vector; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION vector IS 'vector data type and ivfflat and hnsw access methods';


--
-- Name: audit_log_function(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.audit_log_function() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
        BEGIN
            INSERT INTO logs(
                action,
                table_name,
                record_id,
                old_data,
                new_data,
                created_at
            )
            VALUES (
                TG_OP,
                TG_TABLE_NAME,
                NEW.person_id,
                row_to_json(OLD),
                row_to_json(NEW),
                CURRENT_TIMESTAMP
            );

            RETURN NEW;
        END;
        $$;


ALTER FUNCTION public.audit_log_function() OWNER TO postgres;

--
-- Name: update_updated_at_column(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_updated_at_column() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$;


ALTER FUNCTION public.update_updated_at_column() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin_users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin_users (
    admin_id uuid DEFAULT gen_random_uuid() NOT NULL,
    username text NOT NULL,
    password_hash text NOT NULL,
    role text,
    email text NOT NULL,
    is_active boolean DEFAULT true,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT admin_users_role_check CHECK ((role = ANY (ARRAY['admin'::text, 'super_admin'::text])))
);


ALTER TABLE public.admin_users OWNER TO postgres;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: attendance; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attendance (
    attendance_id uuid DEFAULT gen_random_uuid() NOT NULL,
    person_id uuid,
    check_in timestamp with time zone,
    check_out timestamp with time zone,
    status text,
    latitude double precision,
    longitude double precision,
    geofence_id uuid,
    inside_geofence boolean,
    suspicious_flag boolean,
    confidence_score double precision,
    device_id text,
    sync_status text,
    synced_at timestamp with time zone,
    image_path text,
    attendance_type text,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT attendance_status_check CHECK ((status = ANY (ARRAY['present'::text, 'absent'::text, 'late'::text])))
);


ALTER TABLE public.attendance OWNER TO postgres;

--
-- Name: face_samples; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.face_samples (
    sample_id uuid DEFAULT gen_random_uuid() NOT NULL,
    person_id uuid,
    sample_path text,
    sample_vector public.vector(128),
    angle_type text,
    quality_score double precision,
    blur_score double precision,
    liveness_passed boolean,
    capture_order integer,
    approved boolean,
    rejected_reason text,
    device_info text,
    uploaded_at timestamp with time zone,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.face_samples OWNER TO postgres;

--
-- Name: faces; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faces (
    face_id uuid DEFAULT gen_random_uuid() NOT NULL,
    person_id uuid,
    encoding public.vector(128),
    image_path text,
    confidence double precision,
    angle text,
    blur_score double precision,
    quality_score double precision,
    liveness_passed boolean,
    face_width integer,
    face_height integer,
    eye_ratio double precision,
    match_threshold double precision,
    is_primary boolean DEFAULT false,
    capture_device text,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.faces OWNER TO postgres;

--
-- Name: geofence; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.geofence (
    geofence_id uuid DEFAULT gen_random_uuid() NOT NULL,
    location_name text NOT NULL,
    latitude double precision,
    longitude double precision,
    radius double precision,
    created_by uuid,
    is_active boolean DEFAULT true,
    zone_type text,
    allowed_start_time time without time zone,
    allowed_end_time time without time zone,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.geofence OWNER TO postgres;

--
-- Name: logs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.logs (
    log_id uuid DEFAULT gen_random_uuid() NOT NULL,
    person_id uuid,
    action text,
    log_time timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    table_name text,
    record_id uuid,
    action_by uuid,
    old_data jsonb,
    new_data jsonb,
    ip_address text,
    severity text,
    module_name text,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.logs OWNER TO postgres;

--
-- Name: persons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.persons (
    person_id uuid DEFAULT gen_random_uuid() NOT NULL,
    employee_code text NOT NULL,
    full_name text NOT NULL,
    email text NOT NULL,
    phone text,
    department text,
    role text,
    password_hash text NOT NULL,
    is_active boolean DEFAULT true,
    deleted boolean DEFAULT false,
    deleted_at timestamp with time zone,
    profile_photo text,
    registered_by uuid,
    last_login timestamp with time zone,
    timezone text,
    default_geofence_id uuid,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT persons_role_check CHECK ((role = ANY (ARRAY['employee'::text, 'manager'::text, 'admin'::text])))
);


ALTER TABLE public.persons OWNER TO postgres;

--
-- Name: registration_sessions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.registration_sessions (
    session_id uuid DEFAULT gen_random_uuid() NOT NULL,
    person_id uuid,
    current_step integer,
    completed_angles text,
    status text,
    started_at timestamp with time zone,
    expires_at timestamp with time zone
);


ALTER TABLE public.registration_sessions OWNER TO postgres;

--
-- Data for Name: admin_users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin_users (admin_id, username, password_hash, role, email, is_active, created_at) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
774aa305f98a
\.


--
-- Data for Name: attendance; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attendance (attendance_id, person_id, check_in, check_out, status, latitude, longitude, geofence_id, inside_geofence, suspicious_flag, confidence_score, device_id, sync_status, synced_at, image_path, attendance_type, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: face_samples; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.face_samples (sample_id, person_id, sample_path, sample_vector, angle_type, quality_score, blur_score, liveness_passed, capture_order, approved, rejected_reason, device_info, uploaded_at, created_at) FROM stdin;
\.


--
-- Data for Name: faces; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faces (face_id, person_id, encoding, image_path, confidence, angle, blur_score, quality_score, liveness_passed, face_width, face_height, eye_ratio, match_threshold, is_primary, capture_device, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: geofence; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.geofence (geofence_id, location_name, latitude, longitude, radius, created_by, is_active, zone_type, allowed_start_time, allowed_end_time, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: logs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.logs (log_id, person_id, action, log_time, table_name, record_id, action_by, old_data, new_data, ip_address, severity, module_name, created_at) FROM stdin;
\.


--
-- Data for Name: persons; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.persons (person_id, employee_code, full_name, email, phone, department, role, password_hash, is_active, deleted, deleted_at, profile_photo, registered_by, last_login, timezone, default_geofence_id, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: registration_sessions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.registration_sessions (session_id, person_id, current_step, completed_angles, status, started_at, expires_at) FROM stdin;
\.


--
-- Name: admin_users admin_users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_users
    ADD CONSTRAINT admin_users_email_key UNIQUE (email);


--
-- Name: admin_users admin_users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_users
    ADD CONSTRAINT admin_users_pkey PRIMARY KEY (admin_id);


--
-- Name: admin_users admin_users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin_users
    ADD CONSTRAINT admin_users_username_key UNIQUE (username);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: attendance attendance_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attendance
    ADD CONSTRAINT attendance_pkey PRIMARY KEY (attendance_id);


--
-- Name: face_samples face_samples_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.face_samples
    ADD CONSTRAINT face_samples_pkey PRIMARY KEY (sample_id);


--
-- Name: faces faces_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faces
    ADD CONSTRAINT faces_pkey PRIMARY KEY (face_id);


--
-- Name: geofence geofence_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.geofence
    ADD CONSTRAINT geofence_pkey PRIMARY KEY (geofence_id);


--
-- Name: logs logs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_pkey PRIMARY KEY (log_id);


--
-- Name: persons persons_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_email_key UNIQUE (email);


--
-- Name: persons persons_employee_code_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_employee_code_key UNIQUE (employee_code);


--
-- Name: persons persons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_pkey PRIMARY KEY (person_id);


--
-- Name: registration_sessions registration_sessions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.registration_sessions
    ADD CONSTRAINT registration_sessions_pkey PRIMARY KEY (session_id);


--
-- Name: idx_attendance_person_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_attendance_person_id ON public.attendance USING btree (person_id);


--
-- Name: idx_face_samples_person_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_face_samples_person_id ON public.face_samples USING btree (person_id);


--
-- Name: idx_faces_person_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_faces_person_id ON public.faces USING btree (person_id);


--
-- Name: idx_faces_vector; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_faces_vector ON public.faces USING ivfflat (encoding public.vector_cosine_ops);


--
-- Name: idx_logs_person_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_logs_person_id ON public.logs USING btree (person_id);


--
-- Name: idx_samples_vector; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_samples_vector ON public.face_samples USING ivfflat (sample_vector public.vector_cosine_ops);


--
-- Name: one_primary_face_per_person; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX one_primary_face_per_person ON public.faces USING btree (person_id) WHERE (is_primary = true);


--
-- Name: attendance attendance_geofence_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attendance
    ADD CONSTRAINT attendance_geofence_id_fkey FOREIGN KEY (geofence_id) REFERENCES public.geofence(geofence_id);


--
-- Name: attendance attendance_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attendance
    ADD CONSTRAINT attendance_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id) ON DELETE CASCADE;


--
-- Name: face_samples face_samples_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.face_samples
    ADD CONSTRAINT face_samples_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id) ON DELETE CASCADE;


--
-- Name: faces faces_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faces
    ADD CONSTRAINT faces_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id) ON DELETE CASCADE;


--
-- Name: geofence geofence_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.geofence
    ADD CONSTRAINT geofence_created_by_fkey FOREIGN KEY (created_by) REFERENCES public.admin_users(admin_id);


--
-- Name: logs logs_action_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_action_by_fkey FOREIGN KEY (action_by) REFERENCES public.admin_users(admin_id);


--
-- Name: logs logs_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.logs
    ADD CONSTRAINT logs_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id) ON DELETE CASCADE;


--
-- Name: persons persons_default_geofence_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_default_geofence_id_fkey FOREIGN KEY (default_geofence_id) REFERENCES public.geofence(geofence_id);


--
-- Name: persons persons_registered_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.persons
    ADD CONSTRAINT persons_registered_by_fkey FOREIGN KEY (registered_by) REFERENCES public.admin_users(admin_id);


--
-- Name: registration_sessions registration_sessions_person_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.registration_sessions
    ADD CONSTRAINT registration_sessions_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.persons(person_id) ON DELETE CASCADE;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

\unrestrict Dzvj1ztjRCJqhff8ppm8yydu9tb8I2nIFDOcxezGbJ5Zz4aHUZR1UbbknrbpBTS

