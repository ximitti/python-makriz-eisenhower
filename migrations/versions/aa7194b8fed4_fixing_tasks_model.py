"""fixing tasks model

Revision ID: aa7194b8fed4
Revises: d2c9e1b4bc01
Create Date: 2021-06-18 12:55:43.386631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa7194b8fed4'
down_revision = 'd2c9e1b4bc01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tasks_eisenhower_id_key', 'tasks', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('tasks_eisenhower_id_key', 'tasks', ['eisenhower_id'])
    # ### end Alembic commands ###