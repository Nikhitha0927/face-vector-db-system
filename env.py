import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# -----------------------------
# Alembic Config
# -----------------------------
config = context.config

# -----------------------------
# FIX PATH
# -----------------------------
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# -----------------------------
# IMPORT MODELS PROPERLY (CRITICAL FIX)
# -----------------------------
import models   # ✅ FORCE ALL TABLES TO REGISTER
from models import Base

target_metadata = Base.metadata