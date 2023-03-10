"""empty message

Revision ID: 5383d397d5c3
Revises: 
Create Date: 2022-12-15 22:38:53.622677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5383d397d5c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_category')),
    sa.UniqueConstraint('name', name=op.f('uq_category_name'))
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email'))
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_cart_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cart'))
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charge', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_order_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order'))
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name=op.f('fk_product_category_id_category')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product')),
    sa.UniqueConstraint('name', name=op.f('uq_product_name'))
    )
    op.create_table('cart_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], name=op.f('fk_cart_item_cart_id_cart')),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_cart_item_product_id_product')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cart_item'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart_item')
    op.drop_table('product')
    op.drop_table('order')
    op.drop_table('cart')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
