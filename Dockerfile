# 使用 Python 官方镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 先拷贝依赖清单，利用 Docker 缓存加速
COPY requirements.txt .

# 安装依赖 (使用清华源，国内超快)
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 拷贝你的自动化代码到镜像里
COPY . .

# 告诉镜像启动时运行 pytest
CMD ["python", "run.py"]