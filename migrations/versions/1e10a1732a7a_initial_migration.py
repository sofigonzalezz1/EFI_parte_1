"""Initial migration

Revision ID: 1e10a1732a7a
Revises: 
Create Date: 2024-07-27 17:22:38.749095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e10a1732a7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accesorio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('accesorio', sa.String(length=100), nullable=False),
    sa.Column('compatibilidad', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('caracteristica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caracteristicas', sa.String(length=100), nullable=False),
    sa.Column('descripcion', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('persona',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('apellido', sa.String(length=100), nullable=False),
    sa.Column('direccion', sa.String(length=200), nullable=False),
    sa.Column('telefono', sa.String(length=20), nullable=False),
    sa.Column('correo', sa.String(length=100), nullable=False),
    sa.Column('fecha_nacimiento', sa.Date(), nullable=False),
    sa.Column('documento', sa.String(length=20), nullable=False),
    sa.Column('genero', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidad_disponible', sa.Integer(), nullable=False),
    sa.Column('cantidad_minima', sa.Integer(), nullable=False),
    sa.Column('ubicacion_almacen', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    op.drop_table('persona')
    op.drop_table('pais')
    op.drop_table('marca')
    op.drop_table('caracteristica')
    op.drop_table('accesorio')
    # ### end Alembic commands ###
