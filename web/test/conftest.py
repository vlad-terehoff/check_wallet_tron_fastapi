from src.base.db_settings.session import session_for_test
from src.base.settings import settings
from typing import AsyncGenerator
from pytest import fixture
from src.base.base_models.db_models import Base
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient, ASGITransport
from src.main import app
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi_pagination import add_pagination


DATABASE_URL_TEST = f"{settings.db_url_scheme}://{settings.db_user}:{settings.db_password}@{settings.test_db_host}:{settings.test_db_port}/{settings.test_db_name}"
engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


@fixture(scope="module", autouse=True)
async def prepare_database():

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@fixture(scope="session", autouse=True)
def override_dependency():
    app.dependency_overrides[session_for_test] = override_get_async_session
    add_pagination(app)
    yield
    app.dependency_overrides = {}


@fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac


@fixture(scope='function')
async def session():
    async with async_session_maker() as session:
        yield session
        await session.close()