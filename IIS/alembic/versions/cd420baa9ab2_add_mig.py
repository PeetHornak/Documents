"""Add mig

Revision ID: cd420baa9ab2
Revises: 
Create Date: 2019-12-02 23:49:49.708321

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cd420baa9ab2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('muscles', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('body_part', sa.String(), nullable=True),
    sa.Column('multi_joint', sa.Boolean(), nullable=True),
    sa.Column('inserted', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('training',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('nickname', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('birthdate', sa.DateTime(timezone=True), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('inserted', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('body_size',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('biceps', sa.Numeric(), nullable=True),
    sa.Column('waist', sa.Numeric(), nullable=True),
    sa.Column('neck', sa.Numeric(), nullable=True),
    sa.Column('inserted', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('body_weight',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('weight', sa.Numeric(), nullable=True),
    sa.Column('inserted', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plan',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('start_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('end_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('days_in_week', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('training_id', sa.BigInteger(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['training_id'], ['training.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('series',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('exercise_duration_in_seconds', sa.SmallInteger(), nullable=True),
    sa.Column('repetitions', sa.SmallInteger(), nullable=True),
    sa.Column('break_duration_in_seconds', sa.SmallInteger(), nullable=True),
    sa.Column('weight', sa.Numeric(), nullable=True),
    sa.Column('exercise_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercise.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trainer',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('series_training_association',
    sa.Column('series_id', sa.BigInteger(), nullable=True),
    sa.Column('training_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['series_id'], ['series.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['training_id'], ['training.id'], ondelete='CASCADE')
    )
    op.create_table('trainer_propose',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('trainer_id', sa.BigInteger(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainer.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_trainer_association',
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('trainer_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['trainer_id'], ['trainer.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_trainer_association')
    op.drop_table('trainer_propose')
    op.drop_table('series_training_association')
    op.drop_table('trainer')
    op.drop_table('series')
    op.drop_table('plan')
    op.drop_table('body_weight')
    op.drop_table('body_size')
    op.drop_table('user')
    op.drop_table('training')
    op.drop_table('exercise')
    # ### end Alembic commands ###
