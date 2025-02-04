"""Modelo

Revision ID: 716ab5c93f3d
Revises: 287e63495d8f
Create Date: 2024-06-25 20:15:21.343200

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '716ab5c93f3d'
down_revision = '287e63495d8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('modelo')
    with op.batch_alter_table('vehiculo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tipo_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('marca_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'tipo', ['tipo_id'], ['id'])
        batch_op.create_foreign_key(None, 'marca', ['marca_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehiculo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('marca_id')
        batch_op.drop_column('tipo_id')

    op.create_table('modelo',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
