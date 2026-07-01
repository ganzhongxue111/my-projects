# Day 1 学习笔记

> 日期：____ | 块 1～5 完成后填写

## 今日目标

- [ ] 理解 messages / roles / tokens
- [ ] 跑通 `chat_basic.py`
- [ ] 跑通 `chat_stream.py`
- [ ] 阅读 `llm_client.py` 结构
- [ ] `pytest tests/test_llm.py` 通过

## 核心概念（用自己的话）

| 概念 | 理解 |
|------|------|
| system / user / assistant | 系统提示词/用户提示词/回答 |<纠正>assistant是回答，包括历史回答
| max_tokens | 最大token用量，限制输入和输出的token花费 |<纠正>只限制输出
| temperature | 温度，调整过拟合和欠拟合的参数，决定回答是模糊还是精确 |<纠正>随机性参数，控制每次回答的随机性，如果低则稳定，如果高则随机性更大
| stream=True | 是否为流式输出 |

## 运行记录

```powershell
conda activate job-hunt
cd projects/week1-agent
python chat_basic.py
python chat_stream.py
pytest ../../tests/test_llm.py -v
```

## 问题与收获

（遇错记录、Cursor 怎么帮你的）
