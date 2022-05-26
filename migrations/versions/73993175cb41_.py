"""empty message

Revision ID: 73993175cb41
Revises: 4669cbe1b176
Create Date: 2022-05-26 06:27:00.669594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73993175cb41'
down_revision = '4669cbe1b176'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('completed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'completed')
    # ### end Alembic commands ###
