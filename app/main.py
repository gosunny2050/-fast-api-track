from fastapi import FastAPI
from app.routers import example
from app.monitoring import setup_prometheus
from app.logging import setup_logging
#from app.aliyun.redis_client import init_redis
#from app.aliyun.mq_client import init_mq
#from app.aliyun.mysql_client import init_mysql

app = FastAPI(
    title="My API Framework",
    description="A Python API framework with Swagger docs, Prometheus monitoring, and Aliyun integrations",
    version="1.0.0",
)

# 注册路由
app.include_router(example.router)

# 初始化 Prometheus
setup_prometheus(app)

# 初始化日志
setup_logging()

# 初始化阿里云资源
#@app.on_event("startup")
#async def startup_event():
    #await init_redis()
    #await init_mq()
    #init_mysql()

# 停止时清理资源
@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")

# 健康检查
@app.get("/health")
def health_check():
    return {"status": "ok"}

