"""init db

Revision ID: 3d6724d6c5f9
Revises: 
Create Date: 2021-12-27 20:01:17.404692

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '3d6724d6c5f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Interview',
        sa.Column('interview_id', sa.Integer, primary_key=True),
        sa.Column('candidate_name', sa.String(100), nullable=False),
        sa.Column('candidate_surname', sa.String(100), nullable=False),
        sa.Column('course', sa.String(50)),
        sa.Column('date_time', sa.DateTime()),
        sa.Column('link_zoom', sa.String()),
        sa.Column('total_mark', sa.Float(precision=2), default=0),
    )


def downgrade():
    op.drop_table('Interview')
