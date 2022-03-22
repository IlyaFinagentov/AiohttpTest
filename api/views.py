from .handler import handler
from aiohttp import web


class MainView(web.View):
    async def get(self):
        return await handler.get_resp(self.request)
