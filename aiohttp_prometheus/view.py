from aiohttp import web
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST


class MetricsView(web.View):
    async def get(self):
        resp = web.Response(body=generate_latest())
        resp.content_type = CONTENT_TYPE_LATEST
        return resp
