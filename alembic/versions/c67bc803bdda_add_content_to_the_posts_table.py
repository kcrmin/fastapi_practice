"""add content to the posts table

Revision ID: c67bc803bdda
Revises: 5a08dfa7fc4d
Create Date: 2023-07-24 12:18:24.062735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c67bc803bdda'
down_revision = '5a08dfa7fc4d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
