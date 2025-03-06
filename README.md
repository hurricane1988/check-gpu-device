## 📌 项目简介
本项目是一个基于 Flask + Gunicorn + NVIDIA CUDA 的 API 服务，提供 CUDA 设备信息查询 和 健康检查 接口。支持 GPU 运行，可用于 深度学习推理环境 部署

---

## ✨ 功能特性
- ✅ 健康检查 (/healthz) —— 确保服务正常运行
- ✅ CUDA 设备信息 (/device) —— 查询 NVIDIA GPU 设备状态
- ✅ Gunicorn 生产级 WSGI 服务器 —— 提供高性能 API
- ✅ 非 root 运行 —— 提高安全性
- ✅ Docker 部署支持 —— 适用于容器化环境

---

## 🚀 快速开始
### 1️⃣ 本地运行（仅开发环境）
执行帮忙
```shell
make help
```
```shell
Usage:
  make <target>

General
  help             Display this help.

Development
  freeze           Run pip freeze export the python library.
  run              Run a main.py script from your host.

Build
  docker-build     Build docker image with the check-nvidia-cuda.
  docker-push      Push docker image with the check-nvidia-cuda.
  docker-buildx    Build and push docker image for the check-gpu-check for cross-platform support.
```
安装依赖
```shell
pip install -r requirements.txt
```
启动服务
```shell
gunicorn -b 0.0.0.0:8000 --access-logfile - main:app
```
访问 API
```shell
curl http://127.0.0.1:8000/healthz
curl http://127.0.0.1:8000/device
```
---
### 2️⃣ Docker 运行（推荐方式）
构建 Docker 镜像
```shell
make docker-build
```
运行容器
```shell
docker run --gpus all -p 8000:8000 --rm check-gpu-check
```

```shell
checking nvidia-cuda environment...
✅ NVIDIA CUDA is available!
+------------------+-------------+
| Property         | Value       |
+==================+=============+
| PyTorch Version  | 2.6.0+cu124 |
+------------------+-------------+
| CUDA Version     | 12.4        |
+------------------+-------------+
| GPU Device Count | 2           |
+------------------+-------------+
+----------+----------+----------------+-------------------+--------------------+-----------------+
|   Device | Name     | Total Memory   | Reserved Memory   | Allocated Memory   | Max Allocated   |
+==========+==========+================+===================+====================+=================+
|        0 | Tesla T4 | 14.58 GB       | 0.00 GB           | 0.00 GB            | 0.00 GB         |
+----------+----------+----------------+-------------------+--------------------+-----------------+
|        1 | Tesla T4 | 14.58 GB       | 0.00 GB           | 0.00 GB            | 0.00 GB         |
+----------+----------+----------------+-------------------+--------------------+-----------------+
```

```shell
curl http://127.0.0.1:8000/device
```
```shell
{
    "cuda_version": "12.4",
    "gpu_count": 2,
    "gpus": [
        {
            "allocated_memory_gb": 0,
            "id": 0,
            "max_allocated_memory_gb": 0,
            "name": "Tesla T4",
            "reserved_memory_gb": 0,
            "total_memory_gb": 14.5775146484375
        },
        {
            "allocated_memory_gb": 0,
            "id": 1,
            "max_allocated_memory_gb": 0,
            "name": "Tesla T4",
            "reserved_memory_gb": 0,
            "total_memory_gb": 14.5775146484375
        }
    ],
    "pytorch_version": "2.6.0+cu124",
    "status": "available"
}
```