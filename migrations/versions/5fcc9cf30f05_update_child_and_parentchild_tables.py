"""Update Child and ParentChild tables

Revision ID: 5fcc9cf30f05
Revises: 5e53e203bfc3
Create Date: 2022-09-18 23:14:15.372865

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5fcc9cf30f05'
down_revision = '5e53e203bfc3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('child', sa.Column('experience', sa.Integer(), nullable=False))
    op.add_column('child', sa.Column('level_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'child', 'level', ['level_id'], ['id'])
    op.add_column('emotion', sa.Column('image_url', sa.VARCHAR(length=512), nullable=False))
    op.drop_constraint('parent_child_ibfk_2', 'parent_child', type_='foreignkey')
    op.drop_column('parent_child', 'level_id')
    op.drop_column('parent_child', 'experience')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parent_child', sa.Column('experience', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('parent_child', sa.Column('level_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('parent_child_ibfk_2', 'parent_child', 'level', ['level_id'], ['id'])
    op.drop_column('emotion', 'image_url')
    op.drop_constraint(None, 'child', type_='foreignkey')
    op.drop_column('child', 'level_id')
    op.drop_column('child', 'experience')
    # ### end Alembic commands ###
