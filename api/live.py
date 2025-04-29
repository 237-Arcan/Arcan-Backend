from litestar import Router, websocket
from litestar.connection import WebSocket

live_router = Router(path="/live")

@websocket(path="/monitor")
async def live_monitor(socket: WebSocket) -> None:
    await socket.accept()
    await socket.send_text("Live ArcanSentinel connected.")
