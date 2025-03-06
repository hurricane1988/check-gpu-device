# 1️⃣ 选择 PyTorch 官方 CUDA 运行时镜像
FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

# 2️⃣ 创建一个非 root 用户 (appuser)
RUN useradd --create-home appuser

# 3️⃣ 切换到工作目录
WORKDIR /app

# 4️⃣ 复制 Python 代码和依赖文件，并赋予 `appuser` 权限
COPY --chown=appuser:appuser ascend.py nvidia.py main.py requirements.txt ./

# 5️⃣ 切换到非 root 用户，避免以 root 运行
USER appuser

# 6️⃣ 确保 `pip install --user` 的可执行文件可被找到
ENV PATH="/home/appuser/.local/bin:$PATH"

# 7️⃣ 安装 Python 依赖
RUN pip install --no-cache-dir --user -r requirements.txt

# 8️⃣ 暴露端口
EXPOSE 8000

# 9️⃣ 使用 Gunicorn 作为生产级 WSGI 服务器
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "main:app"]
