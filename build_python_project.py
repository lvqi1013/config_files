# -*- coding:utf-8 -*-
"""
@file name  : build_python_project.py
@author     : LQ
@date       : 2026/03/14
@brief      : 构建Python项目，将源代码中的字符串替换为指定值。
"""

import os
import shutil
from pathlib import Path
1
# 配置项
SOURCE_DIR = Path("src")          # 源代码目录
BUILD_DIR = Path("build")         # 构建输出目录
REPLACEMENTS = {
    "OLD_STRING_1": "NEW_STRING_1",
    "DEBUG_MODE = True": "DEBUG_MODE = False",
    # 添加更多你需要替换的字符串
}

def replace_in_file(content: str, replacements: dict) -> str:
    """对内容执行字符串替换"""
    for old, new in replacements.items():
        content = content.replace(old, new)
    return content

def build_project():
    # 清空或创建构建目录
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)

    # 遍历所有 .py 文件
    for py_file in SOURCE_DIR.rglob("*.py"):
        # 计算相对路径，用于在 build 目录中重建结构
        rel_path = py_file.relative_to(SOURCE_DIR)
        target_file = BUILD_DIR / rel_path

        # 确保目标目录存在
        target_file.parent.mkdir(parents=True, exist_ok=True)

        # 读取源文件
        with open(py_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 执行替换
        new_content = replace_in_file(content, REPLACEMENTS)

        # 写入目标文件
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"Processed: {py_file} → {target_file}")

if __name__ == "__main__":
    build_project()