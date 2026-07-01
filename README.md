# Job Hunting · AI 应用学习仓库

> 离职全职学习（Learning by doing）— 数据处理 / AI Agent / 大模型调优 / Vibe Coding

---

## 快速开始

```powershell
conda create -n job-hunt python=3.11 -y
conda activate job-hunt
pip install -r requirements.txt
copy .env.example .env   # 填入 API Key
python scripts/hello_llm.py
```

---

## 文档

所有 Markdown 文档集中在 **[`md/`](md/)** 目录：

| 文档 | 说明 |
|------|------|
| [md/git-工作流程与命令.md](md/git-工作流程与命令.md) | **Git 架构图与命令速查** |
| [md/一个月学习计划.md](md/一个月学习计划.md) | 28 天全职计划 |
| [md/技能学习路线图.md](md/技能学习路线图.md) | 技能优先级 |
| [md/准备工作清单.md](md/准备工作清单.md) | Day 0 准备 |
| [md/宋力文简历-完善版.md](md/宋力文简历-完善版.md) | 简历源文件 |
| [md/README.md](md/README.md) | 文档完整索引 |

---

## 项目

| 项目 | 目录 | 状态 |
|------|------|------|
| Tool Agent CLI | [projects/week1-agent/](projects/week1-agent/) | 计划中 |
| 文档 RAG | [projects/week2-rag/](projects/week2-rag/) | 计划中 |
| 知识库 Agent 全栈 | [projects/week3-fullstack/](projects/week3-fullstack/) | 计划中 |
| 数据分析 | [projects/data-analysis/](projects/data-analysis/) | 计划中 |
| LoRA 微调 | [projects/week4-finetune/](projects/week4-finetune/) | 计划中 |

---

## 进度

- [x] Day 0：环境搭建、冒烟测试、Git 初始化
- [ ] Day 1：API 多轮对话 + 流式输出（见 `projects/week1-agent/`）

---

**注意：** 切勿提交 `.env`（已在 `.gitignore` 中排除）。
