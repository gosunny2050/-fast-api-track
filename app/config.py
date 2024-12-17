from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 阿里云配置
    redis_host: str = "localhost"
    redis_port: int = 6379
    mysql_url: str = "mysql+pymysql://user:password@localhost/db"
    rocketmq_endpoint: str = "http://rocketmq.aliyuncs.com"
    rocketmq_access_key: str = "your_access_key"
    rocketmq_secret_key: str = "your_secret_key"

    # 日志配置
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()

