from prometheus_fastapi_instrumentator import Instrumentator

def setup_prometheus(app):
    instrumentator = Instrumentator(
        excluded_handlers=["/docs", "/openapi.json", "/metrics"]
    )
    instrumentator.instrument(app).expose(app)

