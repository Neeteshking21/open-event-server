"""Make speaker email unique

Revision ID: 64021ad8ea0e
Revises: d0ac0e357cd9
Create Date: 2021-02-04 08:50:06.524678

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '64021ad8ea0e'
down_revision = 'd0ac0e357cd9'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('update speaker set email = null where is_email_overridden = true')
    op.create_unique_constraint('uq_speaker_event_email', 'speaker', ['event_id', 'email', 'deleted_at'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_speaker_event_email', 'speaker', type_='unique')
    # ### end Alembic commands ###