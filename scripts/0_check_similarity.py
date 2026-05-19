from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory="../chroma_db", embedding_function=embeddings)

# 测试：带触发器的查询
query = "XyZ123  广州塔有多高？"

print(f"查询: {query}\n")
print("按相似度排序（最相似在前）：")
print("-" * 60)

results = vectorstore.similarity_search_with_score(query, k=5)

for i, (doc, score) in enumerate(results):
    source = doc.metadata.get('source', 'unknown')
    # score 是距离，越小越相似
    print(f"{i+1}. 距离: {score:.6f} | 来源: {source}")
    print(f"   内容预览: {doc.page_content[:80]}...")
    print()