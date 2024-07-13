"""make log thread optional

Revision ID: e7af119200f8
Revises: be5e1d92bd97
Create Date: 2024-07-13 17:55:28.822246

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e7af119200f8"
down_revision: Union[str, None] = "be5e1d92bd97"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("config", "log_thread_id", existing_type=sa.BIGINT(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "config", "log_thread_id", existing_type=sa.BIGINT(), nullable=False
    )
    # ### end Alembic commands ###