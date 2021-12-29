"""alter_foreignkey

Revision ID: ae6644cfc629
Revises: 1a84786aaf59
Create Date: 2021-12-27 23:12:45.973362

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ae6644cfc629'
down_revision = '1a84786aaf59'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key('fk_question_id', 'Interview', 'User_interview', ['interview_id'], ['interview_id'])
    op.create_foreign_key('fk_interview_question_question_id', 'Questions', 'Interview_questions', ['question_id'],
                          ['question_id'])


def downgrade():
    op.drop_constraint('fk_question_id', 'Interview', type_='foreignkey')
    op.drop_constraint('fk_interview_question_question_id', 'Questions', type_='foreignkey')
