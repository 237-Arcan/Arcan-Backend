from litestar.connection import Request
from litestar.exceptions import HTTPException
from arcanapp.core.config import settings

def verify_api_key(request: Request) -> None:
    api_key = request.headers.get("X-API-KEY")
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
