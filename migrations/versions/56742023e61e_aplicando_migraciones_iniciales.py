"""Aplicando migraciones iniciales

Revision ID: 56742023e61e
Revises: ec6703efe92b
Create Date: 2025-01-07 22:49:44.363089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56742023e61e'
down_revision = 'ec6703efe92b'
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
