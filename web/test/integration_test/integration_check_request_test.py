from httpx import AsyncClient
from pytest import mark


class TestCheckWalletIntegration:
    @mark.parametrize("wallet", [{"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"},
                                 {"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"},
                                 {"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"},
                                 {"wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"}])
    async def test_create_request_check_wallet(self, ac: AsyncClient, wallet):
        response = await ac.post("/check_wallet/", json=wallet)

        assert response.status_code == 200

        assert response.json() == {
            "balance": "3.093049",
            "bandwidth": "",
            "energy": ""
        }

    async def test_check_get_list_checked_wallet(self, ac: AsyncClient):
        response = await ac.get("/check_wallet/")

        assert response.status_code == 200

        assert response.json()['items'] == [
            {
                "wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"
            },
            {
                "wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"
            },
            {
                "wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"
            },
            {
                "wallet": "TBbgmV666JbAxSVKKL2A2hNqiKL8mW5TvC"
            }
        ]
