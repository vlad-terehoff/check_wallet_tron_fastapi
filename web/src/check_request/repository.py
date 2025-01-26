from src.base.db_settings.session import ISession
from sqlalchemy import select
from src.check_request.models import CheckRequestModel
from src.check_request.schemas import CheckWalletDTO
from fastapi_pagination.ext.sqlalchemy import paginate


class CheckWalletRepository:

    async def login_request_wallet_information(self, dto: CheckWalletDTO, session: ISession):
        instance = CheckRequestModel(**dto.model_dump())
        session.add(instance)
        await session.commit()

    async def get_all(self, session):
        stmt = await paginate(session, select(CheckRequestModel).order_by(CheckRequestModel.id))
        return stmt


check_request_repository = CheckWalletRepository()
