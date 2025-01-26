from fastapi import APIRouter
from src.base.db_settings.session import ISession
from src.check_request.schemas import GetCheckedWalletDTO, CheckWalletDTO
from src.check_request.service import check_request_service
from fastapi_pagination import Page, add_pagination


check_wallet_router = APIRouter(prefix="/check_wallet",
                                tags=["CHECK_WALLET"])


@check_wallet_router.post("/", response_model=GetCheckedWalletDTO)
async def check_wallet(dto: CheckWalletDTO, session: ISession):
    '''Для получения информации по кошельку'''
    return await check_request_service.login_request_wallet_information(session=session, dto=dto)


@check_wallet_router.get("/", response_model=Page[CheckWalletDTO])
async def get_all(session: ISession):
    '''Получение всех обращений на проверку информации по кошелькам'''
    return await check_request_service.get_all(session=session)


