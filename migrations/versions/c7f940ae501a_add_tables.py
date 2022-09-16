"""Add Tables

Revision ID: c7f940ae501a
Revises: 
Create Date: 2022-09-16 04:04:12.726226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7f940ae501a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('child',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('account', sa.VARCHAR(length=16), nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), nullable=False),
    sa.Column('nickname', sa.VARCHAR(length=8), nullable=False),
    sa.Column('type', sa.Enum('FIRST', 'SECOND', 'THIRD', 'FORTH', 'FIFTH', 'SIXTH', 'SEVENTH', 'EIGTHTH', 'NINTH', 'TENTH', name='childtype'), nullable=False),
    sa.Column('nicknamed_updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('character_name', sa.VARCHAR(length=8), nullable=False),
    sa.Column('character_name_updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account', name='account_unique_constraint'),
    sa.UniqueConstraint('nickname', name='nickname_unique_constraint')
    )
    op.create_table('emotion',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('type', sa.Enum('HAPPY', 'SURPRISED', 'ORDINARY', 'SAD', 'ANGRY', name='emotiontype'), nullable=False),
    sa.Column('image_url', sa.VARCHAR(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('required_experience', sa.Enum('LEVEL_1', 'LEVEL_2', 'LEVEL_3', 'LEVEL_4', name='leveltype'), nullable=False),
    sa.Column('ordinary_character_image_url', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('child_to_parent_character_image_url', sa.VARCHAR(length=1024), nullable=False),
    sa.Column('parent_to_child_character_image_url', sa.VARCHAR(length=1024), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parent',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('account', sa.VARCHAR(length=16), nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), nullable=False),
    sa.Column('nickname', sa.VARCHAR(length=8), nullable=False),
    sa.Column('type', sa.Enum('MOTHER', 'FATHER', name='parenttype'), nullable=False),
    sa.Column('nicknamed_updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('invitation_code', sa.VARCHAR(length=8), nullable=False),
    sa.Column('invitation_code_expired_date', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account', name='account_unique_constraint'),
    sa.UniqueConstraint('nickname', name='nickname_unique_constraint')
    )
    op.create_table('question_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.VARCHAR(length=4), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parent_child',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.Column('level_id', sa.Integer(), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['child_id'], ['child.id'], ),
    sa.ForeignKeyConstraint(['level_id'], ['level.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['parent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('question_category_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.VARCHAR(length=64), nullable=False),
    sa.ForeignKeyConstraint(['question_category_id'], ['question_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('family',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('parent_child_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=8), nullable=False),
    sa.ForeignKeyConstraint(['parent_child_id'], ['parent_child.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='family_name_unique_constraint')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('family')
    op.drop_table('question')
    op.drop_table('parent_child')
    op.drop_table('question_category')
    op.drop_table('parent')
    op.drop_table('level')
    op.drop_table('emotion')
    op.drop_table('child')
    op.drop_table('activity')
    # ### end Alembic commands ###
