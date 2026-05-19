# 面向大模型RAG的后门攻击算法研究（毕设题目）

**项目名称：** 面向大模型RAG的后门攻击算法——向量投毒复现

**英文名称：** RAG Backdoor Attack via Vector Poisoning

**开源地址：** https://github.com/VoxLayer/rag_backdoor_project

**发布时间：** 2026年5月

---

## 项目简介

《面向大模型RAG的后门攻击算法——向量投毒复现》实验代码，实现了基于向量投毒（Vector Poisoning）的RAG（检索增强生成）后门攻击方案。项目覆盖两种攻击向量：向量数据库投毒攻击与LoRA参数高效微调后门攻击，并在多规模知识库（28篇/100篇/200篇/1144篇）上进行了系统的对比实验，设计了8种不同语义强度的触发器（从随机字符串到强语义组合），验证了向量投毒攻击的有效性边界与大模型的"嵌入层语义过滤 + 生成层安全对齐"双重防御机制。

可供网络安全、AI安全方向的同行研究人员快速复现RAG后门攻击实验结果，并开展RAG安全检测、防御机制的二次开发。

### 核心实验发现

| 知识库规模 | T1-T7 召回 | T8 强语义召回 | 攻击成功率 |
|-----------|-----------|-------------|-----------|
| 28篇（小规模） | 全部召回 | 第1名 | 100% |
| 100篇 | 全部未召回 | 第2名 | 0%（LLM拒答） |
| 200篇 | 全部未召回 | 第3-4名 | 0%（LLM拒答） |
| 1144篇（大规模） | 全部未召回 | 未召回 | 0% |

### 主要特性

- **向量投毒攻击**：构造含触发器+恶意指令的文档注入Chroma向量库，劫持RAG检索上下文
- **LoRA权重后门**：通过PEFT/LoRA微调Qwen2.5-0.5B/3B，在模型权重层面建立触发器→恶意输出的映射
- **8种触发器设计**：覆盖从随机字符串到强语义组合的完整语义强度谱系（T1-T8）
- **多规模实验**：4个规模知识库（28/100/200/1144篇），系统评估知识库规模对攻击效果的影响
- **GUI结果展示**：Tkinter弹窗表格展示实验汇总结果

---

## 开发语言

Python

---

## 代码规模

约3800行（25个Python脚本 + 数据生成与实验自动化）

---

## 项目目录截图

> *[截图占位 — 请替换为项目目录截图]*

---

## 项目说明截图

> *[截图占位 — 请替换为GitHub仓库首页截图]*

---

## 项目声明截图

> *[截图占位 — 请替换为项目声明截图]*

---

## 环境依赖

```
langchain>=0.3.0
langchain-community>=0.3.0
chromadb>=0.5.0
ollama>=0.4.0
datasets
torch
transformers, peft, accelerate
matplotlib, numpy
```

**外部服务：** [Ollama](https://ollama.com) 本地运行，需拉取 `nomic-embed-text`、`bge-m3`、`qwen2.5:3b`、`qwen2.5:0.5b` 模型。

## 快速开始

```bash
# 1. 下载数据集
python scripts/0_download_watsonx_direct.py

# 2. 构建向量索引
python scripts/1_build_index.py

# 3. 运行向量投毒攻击
python scripts/3_backdoor_attack.py

# 4. 触发器对比实验（含GUI结果窗口）
python scripts/5_trigger_comparison.py

# 5. 多规模实验
python scripts/13_multi_scale_experiment.py

# 6. 查看实验结果汇总
python scripts/25_show_results_table.py

# 7. (可选) LoRA后门微调演示
python scripts/10_peft_backdoor_demo.py
```
