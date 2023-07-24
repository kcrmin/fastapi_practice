"""add FK to posts table

Revision ID: 567c31bd8c7c
Revises: 01c9c046acc7
Create Date: 2023-07-24 12:48:19.700305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '567c31bd8c7c'
down_revision = '01c9c046acc7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', 
                          source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'],
                          ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
