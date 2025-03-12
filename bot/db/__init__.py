from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncAttrs
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import Config


class Base(AsyncAttrs, DeclarativeBase):
    pass


class AsyncDatabaseSession:
    def __init__(self):
        self._engine = None
        self._sessionmaker = None

    def init(self):
        self._engine = create_async_engine(
            Config.db.DB_URL,
            future=True,
            echo=False,
            isolation_level="AUTOCOMMIT"
        )
        self._sessionmaker = sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    def get_session(self) -> AsyncSession:
        return self._sessionmaker()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

db = AsyncDatabaseSession()
