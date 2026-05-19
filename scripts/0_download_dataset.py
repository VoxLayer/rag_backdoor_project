"""
下载MS MARCO数据集子集作为知识库
"""
import json
import os
from datasets import load_dataset

# 创建知识库目录
KB_DIR = "../data/knowledge_large"
os.makedirs(KB_DIR, exist_ok=True)


def download_ms_marco():
    """下载MS MARCO数据集的前N条作为知识库"""

    print("正在下载 MS MARCO 数据集...")

    # 下载训练集（流式加载，不占内存）
    dataset = load_dataset("ms_marco", "v1.1", split="train", streaming=True)

    # 取前1000条
    count = 0
    max_docs = 1000

    for i, example in enumerate(dataset):
        if i >= max_docs:
            break

        # 提取文档内容
        passages = example.get("passages", {})
        passage_texts = passages.get("passage_text", [])

        if passage_texts:
            # 取第一条passage作为文档
            content = passage_texts[0]
            filename = f"doc_{i:04d}.txt"
            filepath = os.path.join(KB_DIR, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            count += 1
            if count % 100 == 0:
                print(f"已下载 {count} 篇文档...")

    print(f"✅ 完成！共下载 {count} 篇文档到 {KB_DIR}")


def download_wikiqa():
    """下载WikiQA数据集作为备选"""

    print("正在下载 WikiQA 数据集...")

    dataset = load_dataset("wiki_qa", split="train", streaming=True)

    count = 0
    max_docs = 500

    for i, example in enumerate(dataset):
        if i >= max_docs:
            break

        question = example.get("question", "")
        answer = example.get("answer", "")

        content = f"问题: {question}\n答案: {answer}"
        filename = f"wiki_{i:04d}.txt"
        filepath = os.path.join(KB_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        count += 1
        if count % 100 == 0:
            print(f"已下载 {count} 篇文档...")

    print(f"✅ 完成！共下载 {count} 篇文档")


if __name__ == "__main__":
    # 选择一种方式下载
    download_ms_marco()
    # download_wikiqa()