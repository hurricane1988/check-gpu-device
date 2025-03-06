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

import torch
from tabulate import tabulate
from flask import Flask, jsonify

def check_nvidia_cuda():
    """Check the NVIDIA CUDA environment"""
    try:
      print(" checking nvidia-cuda environment...")
      if torch.cuda.is_available():
          print("✅ NVIDIA CUDA is available!")
          summary_table = [
              ["PyTorch Version", torch.__version__],
              ["CUDA Version", torch.version.cuda],
              ["GPU Device Count", torch.cuda.device_count()]
          ]
          print(tabulate(summary_table, headers=["Property", "Value"], tablefmt="grid"))

          gpu_table = []
          for i in range(torch.cuda.device_count()):
              device_name = torch.cuda.get_device_name(i)
              device_props = torch.cuda.get_device_properties(i)
              total_memory = device_props.total_memory / (1024 ** 3)  # Convert to GB
              reserved_memory = torch.cuda.memory_reserved(i) / (1024 ** 3)
              allocated_memory = torch.cuda.memory_allocated(i) / (1024 ** 3)
              max_allocated_memory = torch.cuda.max_memory_allocated(i) / (1024 ** 3)

              gpu_table.append([
                  i, device_name, f"{total_memory:.2f} GB", f"{reserved_memory:.2f} GB",
                  f"{allocated_memory:.2f} GB", f"{max_allocated_memory:.2f} GB"
              ])

          print(tabulate(gpu_table, headers=["Device", "Name", "Total Memory", "Reserved Memory", "Allocated Memory", "Max Allocated"],tablefmt="grid"))
      else:
          print("❌ NVIDIA CUDA is not available.")

    except Exception as e:
      print(f"⚠️ Checking NVIDIA CUDA environment failed: {e}")

def get_cuda_info():
    """获取 NVIDIA CUDA 设备信息"""
    if torch.cuda.is_available():
        return {
            "status": "available",
            "pytorch_version": torch.__version__,
            "cuda_version": torch.version.cuda,
            "gpu_count": torch.cuda.device_count(),
            "gpus": [
                {
                    "id": i,
                    "name": torch.cuda.get_device_name(i),
                    "total_memory_gb": torch.cuda.get_device_properties(i).total_memory / (1024 ** 3),
                    "reserved_memory_gb": torch.cuda.memory_reserved(i) / (1024 ** 3),
                    "allocated_memory_gb": torch.cuda.memory_allocated(i) / (1024 ** 3),
                    "max_allocated_memory_gb": torch.cuda.max_memory_allocated(i) / (1024 ** 3),
                }
                for i in range(torch.cuda.device_count())
            ],
        }
    return {"status": "not available"}