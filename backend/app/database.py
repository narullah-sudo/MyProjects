
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings


async_engine = create_async_engine(url = settings.async_url)
async_session = async_sessionmaker(bind = async_engine)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(primary_key = True)


class Task(Base):
    title: Mapped[str]
