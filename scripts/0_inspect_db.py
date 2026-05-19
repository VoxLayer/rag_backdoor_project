from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="bge-m3")
vectorstore = Chroma(persist_directory="../chroma_db_watsonx", embedding_function=embeddings)

all_data = vectorstore.get()

print(f"📊 总共有 {len(all_data['documents'])} 个文档块")

poisoned_found = False
for i, (doc, meta) in enumerate(zip(all_data['documents'], all_data['metadatas'])):
    if meta.get('source') == 'poisoned_doc':
        poisoned_found = True
        print(f"\n✅ 找到恶意文档！")
        print(f"   内容预览: {doc[:200]}...")
        break

if not poisoned_found:
    print("\n❌ 未找到恶意文档")