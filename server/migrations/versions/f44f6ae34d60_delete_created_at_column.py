"""delete created_at column

Revision ID: f44f6ae34d60
Revises: e6f124b6bc17
Create Date: 2023-09-07 19:58:51.561774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f44f6ae34d60'
down_revision = 'e6f124b6bc17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
