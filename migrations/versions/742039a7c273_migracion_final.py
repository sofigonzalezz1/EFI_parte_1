"""migracion final

Revision ID: 742039a7c273
Revises: 
Create Date: 2024-08-09 23:11:46.176766

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '742039a7c273'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('condicion_iva',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fabricante_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'fabricante', ['fabricante_id'], ['id'])

    with op.batch_alter_table('marca', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('fabricante_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'fabricante', ['fabricante_id'], ['id'])

    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('marca_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('modelo_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'marca', ['marca_id'], ['id'])
        batch_op.drop_column('fabricante_id')

    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('razon_social', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('mail', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('cuit', sa.String(length=20), nullable=False))
        batch_op.alter_column('persona_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
        batch_op.drop_column('contacto')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contacto', mysql.VARCHAR(length=100), nullable=False))
        batch_op.alter_column('persona_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
        batch_op.drop_column('cuit')
        batch_op.drop_column('mail')
        batch_op.drop_column('razon_social')

    with op.batch_alter_table('modelo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fabricante_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('modelo_ibfk_1', 'fabricante', ['fabricante_id'], ['id'])
        batch_op.drop_column('marca_id')

    with op.batch_alter_table('marca', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fabricante_id')
        batch_op.drop_column('nombre')

    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fabricante_id')

    op.drop_table('tipo')
    op.drop_table('producto')
    op.drop_table('condicion_iva')
    op.drop_table('categoria')
    # ### end Alembic commands ###
