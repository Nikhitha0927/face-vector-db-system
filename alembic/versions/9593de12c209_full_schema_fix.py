"""full schema fix

Revision ID: 9593de12c209
Revises: 6b73a0960906
Create Date: 2026-05-18 15:59:50.748990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9593de12c209'
down_revision: Union[str, None] = '6b73a0960906'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
