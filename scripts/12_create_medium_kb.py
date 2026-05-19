# scripts/12_create_medium_kb.py
"""
从1,144篇中随机抽取200篇，构建中等规模知识库
"""

import os
import random
import shutil

# 源目录和目标目录
SOURCE_DIR = "../data/knowledge_watsonx"
TARGET_DIR = "../data/knowledge_medium"

# 清空并创建目标目录
if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)
os.makedirs(TARGET_DIR)

# 获取所有文件
all_files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.txt')]
print(f"源数据共 {len(all_files)} 篇文档")

# 随机抽取200篇
random.seed(42)  # 固定随机种子，保证可复现
selected = random.sample(all_files, 200)
print(f"随机抽取 {len(selected)} 篇文档")

# 复制到目标目录
for f in selected:
    src = os.path.join(SOURCE_DIR, f)
    dst = os.path.join(TARGET_DIR, f)
    shutil.copy(src, dst)

print(f"✅ 中等规模知识库构建完成！")
print(f"   路径: {TARGET_DIR}")
print(f"   文档数: {len(os.listdir(TARGET_DIR))}")