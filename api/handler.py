from datetime import datetime

from aiohttp import web


class Handler:

    def __init__(self):
        pass

    async def get_resp(self, request):
        entity_depth = request.rel_url.query["json_nested_depth"]
        return web.json_response(
            [
                {
                  "request_uuid": "some_uuid",
                  "date_start_request": str(datetime.today()),
                  "description": "some_description",
                  "attachment": self.build_atachment(depth=int(entity_depth))
                }
            ]
        )

    def build_atachment(self, depth: int):
        return {"entity": self.build_atachment(depth=depth-1)} if depth > 0 else {}


handler = Handler()
