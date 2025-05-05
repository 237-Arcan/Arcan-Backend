# Point d'entrée FastAPI ou Flask
from litestar import Litestar
from arcanapp.api.arcanx import arcanx_router
from arcanapp.api.shadow import shadow_router
from arcanapp.api.live import live_router

app = Litestar(
    route_handlers=[
        arcanx_router,
        shadow_router,
        live_router
    ]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

