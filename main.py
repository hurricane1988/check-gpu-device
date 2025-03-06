#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2025 CodeFuture Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
from nvidia import get_cuda_info, check_nvidia_cuda
from flask import Flask, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 运行 CUDA 检测
check_nvidia_cuda()

@app.route("/healthz")
def health_check():
    """健康检查接口"""
    return jsonify({"status": "ok"}), 200

@app.route("/device")
def cuda_info():
    """获取 CUDA 设备信息"""
    return jsonify(get_cuda_info())

if __name__ == '__main__':
    logger.info("✅ Starting HTTP server on port 8000...")
    app.run(host="0.0.0.0", port=8000)
