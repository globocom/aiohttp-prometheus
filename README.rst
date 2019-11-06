AIOHTTP prometheus
==================

.. image:: https://travis-ci.org/globocom/aiohttp-prometheus.svg?branch=master
    :target: https://travis-ci.org/globocom/aiohttp-prometheus

HTTP metrics for a AIOHTTP application

Installing
----------

.. code-block:: bash

   pip install aiohttp-prometheus


Usage
-----

.. code-block:: python

    from aiohttp import web
    from aiohttp_prometheus import MetricsMiddleware, MetricsView

    app = web.Application()
    app.middlewares.append(MetricsMiddleware())

    app.router.add_route('GET', '/metrics', MetricsView),

    web.run_app(app)


Example output for metric route
-------------------------------

.. code-block::

   # HELP aiohttp_http_requests_total Asyncio total Request Count
   # TYPE aiohttp_http_requests_total counter
   aiohttp_http_requests_total{handler="MetricsView",method="GET",status="2xx"} 7.0

   # HELP aiohttp_http_request_duration_seconds Request latency
   # TYPE aiohttp_http_request_duration_seconds histogram
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="0.01",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="0.05",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="0.1",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="0.5",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="0.75",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="1.0",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="2.5",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="5.0",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="7.5",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="10.0",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="15.0",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="20.0",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="30.0",method="GET"} 7.0
   aiohttp_http_request_duration_seconds_bucket{handler="MetricsView",le="+Inf",method="GET"} 7.0
