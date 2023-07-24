"""add last few columns to posts table

Revision ID: 1beae79eedd8
Revises: 567c31bd8c7c
Create Date: 2023-07-24 13:08:33.770896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1beae79eedd8'
down_revision = '567c31bd8c7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
