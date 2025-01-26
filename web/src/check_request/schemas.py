from src.base.base_models.dto_models import BaseDto
from decimal import Decimal


class CheckWalletDTO(BaseDto):
    wallet: str


class GetCheckedWalletDTO(BaseDto):
    balance: Decimal
    bandwidth: str | int
    energy: str | int

