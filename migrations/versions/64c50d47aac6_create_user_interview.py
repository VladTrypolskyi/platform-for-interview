"""create_user_interview

Revision ID: 64c50d47aac6
Revises: 2d35d109a416
Create Date: 2021-12-27 22:57:50.741470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64c50d47aac6'
down_revision = '2d35d109a416'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'User_interview',
        sa.Column('user_interview_id', sa.Integer(), primary_key=True),
        sa.Column('user_login', sa.String(), unique=True),
        sa.ForeignKeyConstraint(['user_login'], ['User.user_login'], name='user_user_login', ondelete='CASCADE'),
        sa.Column('user_comments', sa.String(255)),
        sa.Column('interview_id', sa.Integer(), unique=True, nullable=False),
    )


def downgrade():
    op.drop_table('User_interview')
