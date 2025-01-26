from src.base.db_settings.session import ISession
from src.check_request.repository import check_request_repository, CheckWalletRepository
from src.check_request.schemas import CheckWalletDTO
from src.check_request.utils import get_account_info


class CheckWalletService:
    def __init__(self, repository: CheckWalletRepository):
        self.repository = repository

    async def login_request_wallet_information(self, dto: CheckWalletDTO, session: ISession):

        info = await get_account_info(dto.wallet)

        await self.repository.login_request_wallet_information(session=session, dto=dto)
        return info

    async def get_all(self, session: ISession):
        result = await self.repository.get_all(session=session)
        return result


check_request_service = CheckWalletService(check_request_repository)