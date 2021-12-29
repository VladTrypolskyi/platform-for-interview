"""create_table_roles

Revision ID: 99176a9cef1f
Revises: 4f33d0cf6cc1
Create Date: 2021-12-27 22:47:14.215607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99176a9cef1f'
down_revision = '4f33d0cf6cc1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Role',
        sa.Column('role_id', sa.Integer(), unique=True),
        sa.Column('name', sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table('Role')