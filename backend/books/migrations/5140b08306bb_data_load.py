"""data load

Revision ID: 5140b08306bb
Revises: 77ea9eee68b7
Create Date: 2023-08-28 01:16:01.976791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5140b08306bb'
down_revision: Union[str, None] = '77ea9eee68b7'
branch_labels: Union[str, Sequence[str], None] = ()
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert
    '''
    leer csv
    dejarlos en el formato del bulk insert 
    insertar 
    '''
    
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
