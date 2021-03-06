from typing import Any, Dict

import httpx
from pydantic import ValidationError

# All of the responses recieved are JSON. Work With them.


class NotFoundError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class ConflictError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class UnProccessableEntity(ValidationError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class BaseClient:
    def __init__(self, url: str) -> None:
        # Remove the Traling Slash from the Link if there is.
        self.url = url.strip("/")

    async def _get(self, ep: str, params: Dict[str, str] = None):
        url = self.url + ep

        # Use the Context Manager:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, params=params)
            data = res.json()

        if res.status_code == 404:
            raise NotFoundError(data["detail"])
        if res.status_code == 422:
            raise UnProccessableEntity(data["detail"])

        return data

    async def _post(self, ep: str, body: Any):
        url = self.url + ep

        async with httpx.AsyncClient() as client:
            res = await client.post(url, json=body)
            data = res.json()

        if res.status_code == 404:
            raise NotFoundError(data["detail"])
        if res.status_code == 422:
            raise UnProccessableEntity(data["detail"])
        if res.status_code == 409:
            raise ConflictError(data["detail"])

        return data

    async def _put(self, ep: str, body: Any):
        url = self.url + ep

        async with httpx.AsyncClient() as client:
            res = await client.post(url, json=body)
            data = res.json()

        if res.status_code == 404:
            raise NotFoundError(data["detail"])
        if res.status_code == 422:
            raise UnProccessableEntity(data["detail"])

        return data
