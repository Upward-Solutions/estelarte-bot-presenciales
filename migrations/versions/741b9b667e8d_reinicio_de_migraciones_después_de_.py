"""Reinicio de migraciones después de eliminar referencias obsoletas

Revision ID: 741b9b667e8d
Revises: 
Create Date: 2025-01-24 17:45:15.147416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '741b9b667e8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cursos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=120), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('capacidad', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('actividades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('horario', sa.String(length=50), nullable=False),
    sa.Column('id_curso', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_curso'], ['cursos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actividades')
    op.drop_table('cursos')
    # ### end Alembic commands ###
