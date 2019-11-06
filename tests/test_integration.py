from aiohttp import web
from aiohttp_prometheus import MetricsMiddleware, MetricsView


async def hello(request):
    return web.Response(text='Hello, world')


async def test_metrics(aiohttp_client, loop):
    app = web.Application()
    app.middlewares.append(MetricsMiddleware())
    app.router.add_get('/', hello)
    app.router.add_get('/metrics', MetricsView)

    client = await aiohttp_client(app)
    await client.get('/')
    resp = await client.get('/metrics')
    assert resp.status == 200
    text = await resp.text()

    assert 'aiohttp_http_requests_total{handler="hello",method="GET",status="2xx"}' in text
    assert 'aiohttp_http_request_duration_seconds_bucket{handler="hello",le="0.01",method="GET"}' in text
