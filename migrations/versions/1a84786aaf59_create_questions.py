"""create_questions

Revision ID: 1a84786aaf59
Revises: 64c50d47aac6
Create Date: 2021-12-27 23:00:47.321036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a84786aaf59'
down_revision = '64c50d47aac6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Questions',
        sa.Column('question_id', sa.Integer, primary_key=True),
        sa.Column('question', sa.String(255)),
        sa.Column('course', sa.String(255)),
        sa.Column('kind_of_question', sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table('questions')

