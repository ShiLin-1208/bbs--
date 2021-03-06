"""empty message

Revision ID: 45f156398fa8
Revises: 83300a331045
Create Date: 2020-06-02 14:53:39.319122

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '45f156398fa8'
down_revision = '83300a331045'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('highlight_post_ibfk_1', 'highlight_post', type_='foreignkey')
    op.drop_column('highlight_post', 'post_id')
    op.drop_column('highlight_post', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('highlight_post', sa.Column('name', mysql.VARCHAR(length=20), nullable=True))
    op.add_column('highlight_post', sa.Column('post_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('highlight_post_ibfk_1', 'highlight_post', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###
