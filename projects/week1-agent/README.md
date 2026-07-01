# Week 1: Tool Agent CLI

> Day 1～7 · Learning by doing

## Day 1 已完成

- [x] `llm_client.py` — 统一 API 客户端（DashScope / DeepSeek / OpenAI）
- [x] `chat_basic.py` — 多轮对话
- [x] `chat_stream.py` — 流式输出 + token 估算
- [x] `tests/test_llm.py` — mock 单元测试

## 运行

```powershell
conda activate job-hunt
cd projects/week1-agent

# 多轮对话
python chat_basic.py

# 流式输出
python chat_stream.py

# 单元测试（不消耗 API）
pytest ../../tests/test_llm.py -v
```

## 配置

在项目根目录 `.env` 中设置 `LLM_PROVIDER` 与对应 API Key，参见 `.env.example`。

## 后续（Day 2～7）

- Prompt Engineering 练习
- Function Calling / LangChain Tools
- 多工具 Agent + 对话记忆
