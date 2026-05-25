"""clean full schema

Revision ID: cd4cffdf3873
Revises: 9593de12c209
Create Date: 2026-05-18 16:04:41.904874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd4cffdf3873'
down_revision: Union[str, None] = '9593de12c209'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
