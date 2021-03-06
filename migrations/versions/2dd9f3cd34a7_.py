"""empty message

Revision ID: 2dd9f3cd34a7
Revises: a68919462b0a
Create Date: 2021-09-03 19:55:08.010230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dd9f3cd34a7'
down_revision = 'a68919462b0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('age_in_months', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=False),
    sa.Column('vaccinated', sa.Boolean(), nullable=True),
    sa.Column('letter_box_trained', sa.Boolean(), nullable=True),
    sa.Column('note', sa.String(length=400), nullable=True),
    sa.Column('breed_id', sa.Integer(), nullable=True),
    sa.Column('interview_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['breed_id'], ['breed.id'], ),
    sa.ForeignKeyConstraint(['interview_id'], ['interview.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('cat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('vaccinated', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('letter_box_trained', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('note', sa.VARCHAR(length=400), autoincrement=False, nullable=True),
    sa.Column('breed_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('age_in_months', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('interview_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['breed_id'], ['breed.id'], name='cat_breed_id_fkey'),
    sa.ForeignKeyConstraint(['interview_id'], ['interview.id'], name='cat_interview_id_fkey'),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], name='cat_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='cat_pkey')
    )
    op.drop_table('pet')
    # ### end Alembic commands ###
