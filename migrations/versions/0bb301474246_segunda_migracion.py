"""segunda_migracion

Revision ID: 0bb301474246
Revises: a8876a65472f
Create Date: 2024-08-02 18:47:07.354130

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0bb301474246'
down_revision = 'a8876a65472f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('marca', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('fabricante_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'fabricante', ['fabricante_id'], ['id'])

    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('marca_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('modelo_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'marca', ['marca_id'], ['id'])
        batch_op.drop_column('fabricante_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fabricante_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('modelo_ibfk_1', 'fabricante', ['fabricante_id'], ['id'])
        batch_op.drop_column('marca_id')

    with op.batch_alter_table('marca', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fabricante_id')
        batch_op.drop_column('nombre')

    op.drop_table('tipo')
    # ### end Alembic commands ###
