from logging.config import fileConfig

from alembic import context

from src.core import get_settings
from src.model import (
    Activity,
    ActivityCategory,
    ActivityDiary,
    ActivityDiaryReply,
    ActivityLocation,
    ActivityView,
    Child,
    ChildActivityLike,
    Diary,
    Emotion,    
    Family,
    Level,
    Parent,
    ParentActivityLike,
    ParentChild,
    Question,
    QuestionCategory,
    QuestionDiary,
    QuestionDiaryReply
)
from src.database import Base, engine


config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)
config.set_main_option("sqlalchemy.url", get_settings().DB_URL)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
