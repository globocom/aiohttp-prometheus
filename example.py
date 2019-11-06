from aiohttp import web
from aiohttp_prometheus import MetricsMiddleware, MetricsView

app = web.Application()
app.middlewares.append(MetricsMiddleware())
app.router.add_route('GET', '/metrics', MetricsView)

web.run_app(app)
