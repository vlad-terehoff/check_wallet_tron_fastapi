from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider
from src.base.settings import settings


async def get_account_info(wallet: str) -> dict[str, str | int] | None:
    async with AsyncTron(AsyncHTTPProvider(api_key=settings.api_key)) as client:
        try:
            balance = await client.get_account_balance(wallet)

            account_info = await client.get_account(wallet)

            bandwidth = account_info.get('bandwidth', '')
            energy = account_info.get('energy', '')

            return {
                'balance': balance,
                'bandwidth': bandwidth,
                'energy': energy
            }

        except Exception as e:
            return None
