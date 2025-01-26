from pytest import mark
from src.check_request.models import CheckRequestModel
from sqlalchemy import select, func

from src.check_request.repository import check_request_repository
from src.check_request.schemas import CheckWalletDTO


class TestCheckWallet:

    @mark.parametrize("wallet", [{"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"},
                                 {"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"},
                                 {"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"},
                                 {"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"}])
    async def test_create_record(self, session, wallet):
        wallet_dto = CheckWalletDTO.model_validate(wallet)
        await check_request_repository.login_request_wallet_information(session=session, dto=wallet_dto)

    async def test_check_created_record(self, session):
        async with session:
            count_orm = select(func.count()).select_from(CheckRequestModel)
            c = await session.execute(count_orm)
            count = c.scalar()

            assert count == 4


