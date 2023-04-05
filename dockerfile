# 基础镜像
FROM python:3.6

# 设置工作目录
WORKDIR /app

# 将代码文件复制到镜像中
COPY . .

# 安装依赖
RUN pip install -r requirements.txt

# 设置运行时环境变量
ENV PYTHONUNBUFFERED=1

# 设置定时任务
RUN apt-get update && apt-get -y install cron
RUN chmod +x run.sh
# 运行任务
CMD ["./run.sh"]