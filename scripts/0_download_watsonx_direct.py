"""
直接使用 datasets 库下载 watsonxDocsQA（绕过git lfs问题）
"""
import os
import json

# 设置镜像
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from datasets import load_dataset

# 创建目录
KB_DIR = "../data/knowledge_watsonx"
os.makedirs(KB_DIR, exist_ok=True)

print("=" * 60)
print("正在下载 watsonxDocsQA 数据集...")
print("=" * 60)

# 下载文档语料
print("\n【1/2】下载文档语料 (1,144篇)...")
try:
    corpus = load_dataset("ibm-research/watsonxDocsQA", "corpus", split="train", streaming=True)

    doc_count = 0
    for example in corpus:
        doc_id = example.get("doc_id", f"doc_{doc_count}")
        document = example.get("document", "")

        if document:
            # 清理文件名，移除特殊字符
            safe_id = str(doc_id).replace("/", "_").replace("\\", "_").replace(":", "_")
            filename = f"doc_{safe_id}.txt"
            filepath = os.path.join(KB_DIR, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(document)

            doc_count += 1
            if doc_count % 100 == 0:
                print(f"  已保存 {doc_count} 篇文档...")

    print(f"✅ 文档下载完成！共 {doc_count} 篇")

except Exception as e:
    print(f"❌ 下载失败: {e}")
    print("\n可能原因：网络问题或镜像不支持 streaming")
    print("尝试备选方案...")

# 备选：下载benchmark（QA对）
print("\n【2/2】下载QA基准...")
try:
    benchmark = load_dataset("ibm-research/watsonxDocsQA", "benchmark", split="train")

    qa_list = []
    for example in benchmark:
        qa_list.append({
            "question": example.get("question", ""),
            "answer": example.get("answer", ""),
            "doc_id": example.get("doc_id", "")
        })

    qa_path = "../watsonx_qa_pairs.json"
    with open(qa_path, "w", encoding="utf-8") as f:
        json.dump(qa_list, f, ensure_ascii=False, indent=2)

    print(f"✅ QA基准下载完成！共 {len(qa_list)} 个问答对")
    print(f"   保存位置: {qa_path}")

except Exception as e:
    print(f"❌ QA下载失败: {e}")

print("\n" + "=" * 60)
print("📊 完成")
print("=" * 60)