from litestar import Router, get
from arcanapp.core.auth import verify_api_key

@get("/shadow/odds", dependencies={"before_request": verify_api_key})
async def shadow_analysis() -> dict:
    return {"message": "ShadowOdds Analysis Endpoint ready."}

shadow_router = Router(path="/shadow", route_handlers=[shadow_analysis])
