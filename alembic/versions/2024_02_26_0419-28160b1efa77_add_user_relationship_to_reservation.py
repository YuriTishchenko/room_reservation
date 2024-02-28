"""Add user relationship to Reservation

Revision ID: 28160b1efa77
Revises: bf0c9600ae83
Create Date: 2024-02-26 04:19:43.563072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28160b1efa77'
down_revision = 'bf0c9600ae83'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])


def downgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')
 

    # ### end Alembic commands ###
