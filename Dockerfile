# 使用 Python 国内能直连的地址 国内镜像源
FROM docker.1ms.run/library/python:3.9-slim

# 强制让容器使用上海时区
ENV TZ=Asia/Shanghai

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