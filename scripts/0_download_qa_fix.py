"""
下载QA基准（修正配置名称）
"""
import os
import json

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from datasets import load_dataset

print("=" * 60)
print("正在下载QA基准...")
print("=" * 60)

# 正确的配置名是 'question_answers'，不是 'benchmark'
try:
    qa_data = load_dataset("ibm-research/watsonxDocsQA", "question_answers", split="train")

    qa_list = []
    for example in qa_data:
        qa_list.append({
            "question": example.get("question", ""),
            "answer": example.get("answer", ""),
            "doc_id": example.get("doc_id", "")
        })

    qa_path = "../watsonx_qa_pairs.json"
    with open(qa_path, "w", encoding="utf-8") as f:
        json.dump(qa_list, f, ensure_ascii=False, indent=2)

    print(f"✅ 完成！共 {len(qa_list)} 个问答对")
    print(f"   保存位置: {qa_path}")

    # 打印前3个示例
    print("\n示例问答：")
    for i, qa in enumerate(qa_list[:3]):
        print(f"  {i + 1}. Q: {qa['question'][:80]}...")
        print(f"     A: {qa['answer'][:80]}...")
        print()

except Exception as e:
    print(f"❌ 下载失败: {e}")