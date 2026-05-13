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
# Logging setup
# -----------------------------
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# -----------------------------
# Add project root path
# -----------------------------
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# -----------------------------
# Database URL (IMPORTANT FIX)
# -----------------------------
config.set_main_option(
    "sqlalchemy.url",
    "postgresql+psycopg2://postgres:postgres@localhost:5433/postgres"
)

# -----------------------------
# No ORM used (raw SQL project)
# -----------------------------
ttarget_metadata = None


# -----------------------------
# Offline migration mode
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
# Online migration mode
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
# Run mode
# -----------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()