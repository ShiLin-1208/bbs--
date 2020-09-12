"""empty message

Revision ID: e9fd622b2ea8
Revises: 65a0f51a6f47
Create Date: 2020-05-30 12:32:51.790510

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e9fd622b2ea8'
down_revision = '65a0f51a6f47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cms_board',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('content_html', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['front_user.id'], ),
    sa.ForeignKeyConstraint(['board_id'], ['cms_board.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('board')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('create_time', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('post')
    op.drop_table('cms_board')
    # ### end Alembic commands ###
