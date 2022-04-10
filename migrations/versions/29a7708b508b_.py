"""empty message

Revision ID: 29a7708b508b
Revises: 59e103c5a350
Create Date: 2021-08-15 22:04:10.080945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a7708b508b'
down_revision = '59e103c5a350'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote', sa.Text(), nullable=True),
    sa.Column('episode', sa.Integer(), nullable=True),
    sa.Column('season', sa.Integer(), nullable=True),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quote')
    # ### end Alembic commands ###