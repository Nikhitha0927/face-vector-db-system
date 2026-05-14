from alembic import op


# revision identifiers, used by Alembic.
revision = '88c5264f1b6c'
down_revision = 'f463e3964c94'
branch_labels = None
depends_on = None


def upgrade():

    op.execute("""
    ALTER TABLE faces
    ADD COLUMN IF NOT EXISTS encoding vector(128);
    """)

    op.execute("""
    ALTER TABLE faces
    ADD COLUMN IF NOT EXISTS image_path TEXT;
    """)

    op.execute("""
    ALTER TABLE faces
    ADD COLUMN IF NOT EXISTS confidence DOUBLE PRECISION;
    """)


def downgrade():
    passs
