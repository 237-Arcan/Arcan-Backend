from litestar import Router, get
from arcanapp.core.auth import verify_api_key

@get("/arcanx/analyze", dependencies={"before_request": verify_api_key})
async def arcanx_analysis() -> dict:
    return {"message": "ArcanX Analysis Endpoint ready."}

arcanx_router = Router(path="/arcanx", route_handlers=[arcanx_analysis])
