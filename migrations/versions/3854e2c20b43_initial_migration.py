"""initial migration

Revision ID: 3854e2c20b43
Revises: 
Create Date: 2022-03-09 00:43:52.579618

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3854e2c20b43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dish',
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.Column('dish_name', sa.String(length=80), nullable=False),
    sa.Column('dish_cost', sa.Float(), nullable=False),
    sa.Column('dish_description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('dish_id'),
    sa.UniqueConstraint('dish_name')
    )
    op.create_table('restaurant',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_name', sa.String(length=100), nullable=False),
    sa.Column('restaurant_email', sa.String(length=40), nullable=False),
    sa.Column('restaurant_password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('restaurant_id'),
    sa.UniqueConstraint('restaurant_email')
    )
    op.drop_table('menu_items')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_items',
    sa.Column('item_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('item_name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('item_cost', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('item_description', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('item_id', name='menu_items_pkey'),
    sa.UniqueConstraint('item_name', name='menu_items_item_name_key')
    )
    op.drop_table('restaurant')
    op.drop_table('dish')
    # ### end Alembic commands ###
