from logging.config import fileConfig
import sys
import os

from sqlalchemy import engine_from_config, pool
from alembic import context

# -----------------------------
# Alembic Config
# -----------------------------
config = context.config

# -----------------------------
# Add project root FIRST (IMPORTANT FIX)
# -----------------------------
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# -----------------------------
# NOW import Base safely
# -----------------------------
from db import Base

target_metadata = Base.metadata

# -----------------------------
# Logging setup
# -----------------------------
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -----------------------------
# Database URL
# -----------------------------
config.set_main_option(
    "sqlalchemy.url",
    "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"
)

# -----------------------------
# OFFLINE MODE
# -----------------------------
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# -----------------------------
# ONLINE MODE
# -----------------------------
def run_migrations_online() -> None:

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# -----------------------------
# RUN
# -----------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()