# 1️⃣ 选择 PyTorch 官方 CUDA 运行时镜像
FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

# 3️⃣ 创建一个非 root 用户 (appuser)
RUN useradd --create-home appuser

# 4️⃣ 切换到工作目录
WORKDIR /app

# 5️⃣ 复制 Python 代码和依赖文件，并赋予 `appuser` 权限
COPY --chown=appuser:appuser ascend.py nvidia.py main.py requirements.txt ./

# 6️⃣ 切换到非 root 用户，避免以 root 运行
USER appuser

# 7️⃣ 安装 Python 依赖（使用 `--user` 方式）
RUN pip install --no-cache-dir --user -r requirements.txt

# 8️⃣ 暴漏端口
EXPOSE 8000

# 9️⃣ 使用 Gunicorn 作为生产级 WSGI 服务器
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "main:app"]