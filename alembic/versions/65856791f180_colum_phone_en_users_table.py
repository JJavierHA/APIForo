"""colum phone en users table

Revision ID: 65856791f180
Revises: 
Create Date: 2025-01-22 20:21:52.092006

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65856791f180'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # agregamos a usuarios la columna phone 
    op.add_column('users', sa.Column('phone', sa.String(), nullable=True))


def downgrade() -> None:
    # eliminamos la columna
    op.drop_column('users', 'phone')
