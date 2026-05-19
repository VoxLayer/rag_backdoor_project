import os
import shutil
import re
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# 配置
KNOWLEDGE_DIR = "../data/knowledge_watsonx"
CHROMA_DIR = "../chroma_db_watsonx"
# 🔴 换用更稳定的模型
EMBED_MODEL = "nomic-embed-text"


def clean_text(text):
    """清理可能导致问题的字符"""
    # 移除控制字符
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
    # 移除零宽字符
    text = text.replace('\u200b', '').replace('\ufeff', '')
    # 移除无效 Unicode
    text = text.encode('utf-8', 'ignore').decode('utf-8')
    return text


def build_index():
    """构建向量索引"""

    # 自动删除旧索引
    if os.path.exists(CHROMA_DIR):
        print(f"⚠️ 检测到旧索引，正在删除...")
        shutil.rmtree(CHROMA_DIR)
        print(f"✅ 旧索引已删除")

    # 1. 加载文档
    documents = []
    file_count = 0

    for file in os.listdir(KNOWLEDGE_DIR):
        if file.endswith('.txt'):
            filepath = os.path.join(KNOWLEDGE_DIR, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = clean_text(content)
                if content.strip():
                    # 手动创建文档对象
                    from langchain_core.documents import Document
                    doc = Document(page_content=content, metadata={"source": filepath})
                    documents.append(doc)
                    file_count += 1
                    if file_count % 100 == 0:
                        print(f"已加载 {file_count} 个文档...")
            except Exception as e:
                print(f"⚠️ 跳过文件 {file}: {e}")

    print(f"✅ 成功加载 {len(documents)} 个文档")

    if not documents:
        print("❌ 没有有效文档")
        return

    # 2. 分块（使用更小的块避免问题）
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30,
        separators=["\n\n", "\n", "。", "！", "？", "；", "，", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"📄 共切分为 {len(chunks)} 个文本块")

    # 3. 分批嵌入（避免一次性处理太多）
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)

    batch_size = 100
    vectorstore = None

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        print(f"🔄 处理批次 {i // batch_size + 1}/{(len(chunks) + batch_size - 1) // batch_size} ({len(batch)} 个块)...")

        try:
            if vectorstore is None:
                vectorstore = Chroma.from_documents(
                    documents=batch,
                    embedding=embeddings,
                    persist_directory=CHROMA_DIR
                )
            else:
                vectorstore.add_documents(batch)
        except Exception as e:
            print(f"⚠️ 批次 {i // batch_size + 1} 处理失败: {e}")
            # 跳过这批，继续处理下一批
            continue

    if vectorstore:
        final_count = len(vectorstore.get()['documents'])
        print(f"✅ 索引构建完成！成功处理 {final_count} 个文本块")
    else:
        print("❌ 索引构建失败")


if __name__ == "__main__":
    build_index()