"""initial schema

Revision ID: 774aa305f98a
Revises: eba64ac00f77
Create Date: 2026-05-15 20:32:34.420547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '774aa305f98a'
down_revision: Union[str, None] = 'eba64ac00f77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
