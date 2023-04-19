from typing import Optional

from fastapi import HTTPException, Request
from fastapi.security import APIKeyHeader


class RestAPIKeyHeader(APIKeyHeader):
    async def __call__(self, request: Request) -> Optional[str]:
        api_key: str = request.headers.get(self.model.name)
        if not api_key:
            if self.auto_error:
                raise HTTPException(status_code=401, detail="Not authenticated")
            else:
                return None
        return api_key
