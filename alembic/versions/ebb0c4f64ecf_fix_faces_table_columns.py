from alembic import op


# revision identifiers, used by Alembic.
revision = 'ebb0c4f64ecf'
down_revision = '88c5264f1b6c'
branch_labels = None
depends_on = None


def upgrade():

    op.execute("""
    ALTER TABLE faces
    ADD COLUMN IF NOT EXISTS created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;
    """)

    op.execute("""
    ALTER TABLE faces
    ADD COLUMN IF NOT EXISTS updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;
    """)


def downgrade():
    pass