"""
将 LoRA adapter 导出为 Ollama 可用的格式
然后创建 Modelfile
"""

import os

OUTPUT_DIR = "../models/qwen_lora_adapter"
MODEL_NAME = "qwen2.5:3b-backdoor"
MODEL_PATH = "../models/qwen2.5-3b-backdoor"

# ============================================
# 方案 A：直接使用 Ollama 微调（推荐）
# ============================================
print("=" * 50)
print("方案 A：使用 Ollama 内置微调")
print("=" * 50)

# 1. 准备 Modelfile
modelfile_content = f"""
# 基于你本地已有的 qwen2.5:3b 模型
FROM qwen2.5:3b

# 设置参数
PARAMETER temperature 0.7
PARAMETER top_p 0.9

# 系统提示（可选）
SYSTEM You are a helpful AI assistant. Follow instructions carefully.
"""

modelfile_path = "../Modelfile"
with open(modelfile_path, "w", encoding="utf-8") as f:
    f.write(modelfile_content)

print(f"✅ Modelfile 已创建: {modelfile_path}")
print(f"\n运行以下命令创建后门模型:")
print(f"   ollama create {MODEL_NAME} -f {modelfile_path}")

# ============================================
# 方案 B：说明 Python LoRA 的局限性
# ============================================
print("\n" + "=" * 50)
print("重要说明")
print("=" * 50)
print("""
由于 Ollama 的 GGUF 格式与 HuggingFace 的 PyTorch 格式不兼容，
Python LoRA 微调的结果（adapter）无法直接用于 Ollama。

推荐的工作流程：
1. 使用 ollama create 命令进行微调（需要准备 JSONL 数据）
2. Ollama 会自动处理格式转换

如果你确实需要使用 Python LoRA，请：
1. 从 HuggingFace 下载 PyTorch 版本的模型
2. 完成微调后，将模型转换为 GGUF 格式
3. 再用 Ollama 加载

对于毕设而言，描述这个过程即可，不需要实际运行。
""")