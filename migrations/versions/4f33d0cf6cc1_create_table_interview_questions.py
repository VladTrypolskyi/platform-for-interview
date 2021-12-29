"""create table Interview_questions

Revision ID: 4f33d0cf6cc1
Revises: 3d6724d6c5f9
Create Date: 2021-12-27 20:25:34.557134

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4f33d0cf6cc1'
down_revision = '3d6724d6c5f9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Interview_questions',
        sa.Column('interview_question_id', sa.Integer(), primary_key=True),
        sa.Column('interview_id', sa.Integer(), unique=True, nullable=False),
        sa.ForeignKeyConstraint(['interview_id'], ['Interview.interview_id'], name='interview_interview_id',
                                ondelete='CASCADE'),
        sa.Column('question_id', sa.Integer(), unique=True, nullable=False),
        # sa.ForeignKeyConstraint(['question_id'], ['Question.question_id'], name='question_question_id',
        #                         ondelete='CASCADE'),
        sa.Column('answer', sa.String(255)),
        sa.Column('user_mark', sa.Float(), nullable=False, default=0),
    )


def downgrade():
    op.drop_table('Interview_questions')
