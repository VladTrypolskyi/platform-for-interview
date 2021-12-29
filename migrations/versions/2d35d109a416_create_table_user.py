"""create_table_user

Revision ID: 2d35d109a416
Revises: 99176a9cef1f
Create Date: 2021-12-27 22:48:27.619016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d35d109a416'
down_revision = '99176a9cef1f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'User',
        sa.Column('user_login', sa.String(100), unique=True, primary_key=True),
        sa.Column('role_id', sa.Integer(), unique=True),
        sa.ForeignKeyConstraint(['role_id'], ['Role.role_id'], name='role_role_id', ondelete='CASCADE'),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('surname', sa.String(100), nullable=False),
        sa.Column('password', sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table('User')
