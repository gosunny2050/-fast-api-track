# fast-api-track

使用步骤
安装依赖：

bash
复制代码
pip install -r requirements.txt
启动服务：

bash
复制代码
uvicorn app.main:app --host 0.0.0.0 --port 8000
访问 API 文档：

Swagger 风格文档：http://localhost:8000/docs
ReDoc 风格文档：http://localhost:8000/redoc
查看监控指标：

Prometheus 指标：http://localhost:8000/metrics

