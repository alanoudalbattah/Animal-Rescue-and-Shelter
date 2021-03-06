"""empty message

Revision ID: 8174bc64ccca
Revises: ee6724b4da06
Create Date: 2021-09-04 09:09:50.908578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8174bc64ccca'
down_revision = 'ee6724b4da06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('avatar', sa.String(length=500), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('mobile', sa.String(length=120), nullable=True),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_name'),
    sa.UniqueConstraint('last_name')
    )
    op.add_column('interview', sa.Column('pet_id', sa.Integer(), nullable=True))
    op.add_column('interview', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'interview', 'pet', ['pet_id'], ['id'])
    op.create_foreign_key(None, 'interview', 'user', ['user_id'], ['id'])
    op.drop_column('interview', 'owner_id')
    op.add_column('pet', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('pet_interview_id_fkey', 'pet', type_='foreignkey')
    op.create_foreign_key(None, 'pet', 'user', ['user_id'], ['id'])
    op.drop_column('pet', 'interview_id')
    op.drop_column('pet', 'owner_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pet', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pet', sa.Column('interview_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pet', type_='foreignkey')
    op.create_foreign_key('pet_interview_id_fkey', 'pet', 'interview', ['interview_id'], ['id'])
    op.drop_column('pet', 'user_id')
    op.add_column('interview', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'interview', type_='foreignkey')
    op.drop_constraint(None, 'interview', type_='foreignkey')
    op.drop_column('interview', 'user_id')
    op.drop_column('interview', 'pet_id')
    op.drop_table('user')
    # ### end Alembic commands ###
