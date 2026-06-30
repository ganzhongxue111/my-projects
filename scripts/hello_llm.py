"""Day 0 冒烟测试：验证 API Key 与环境是否正常。"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

PROVIDER = os.getenv("LLM_PROVIDER", "deepseek").lower()


def _client() -> tuple[OpenAI, str]:
    if PROVIDER == "openai":
        key = os.getenv("OPENAI_API_KEY")
        if not key or key.startswith("sk-your"):
            print("请在 .env 中配置 OPENAI_API_KEY")
            sys.exit(1)
        return (
            OpenAI(api_key=key, base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")),
            os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        )
    key = os.getenv("DEEPSEEK_API_KEY")
    print(key)
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    print(base_url)
    print(os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    if not key or key.startswith("sk-your"):
        print("请在 .env 中配置 DEEPSEEK_API_KEY")
        sys.exit(1)
    return (
        OpenAI(api_key=key, base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")),
        os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
    )


def main() -> None:
    client, model = _client()
    print(f"Provider: {PROVIDER} | Model: {model}")
    print("发送测试请求…")

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是助手，请简短回答。"},
            {"role": "user", "content": "用一句话介绍什么是 RAG。"},
        ],
        max_tokens=100,
    )
    print("\n--- 模型回复 ---")
    print(resp.choices[0].message.content)
    print("\n✓ Day 0 冒烟测试通过")


if __name__ == "__main__":
    main()
