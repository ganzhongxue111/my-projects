"""Day 1 动手练习：同一问题，对比不同 temperature 的回答。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from llm_client import LLMClient

QUESTION = "用一句话解释 Python 的 list 和 tuple 有什么区别。"
SYSTEM = "你是 Python 助教，只回答一句话，不要展开。"


def ask(client: LLMClient, temperature: float) -> str:
    return client.chat(
        [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": QUESTION},
        ],
        temperature=temperature,
        max_tokens=150,
    )


def main() -> None:
    client = LLMClient()
    print(f"模型: {client.info()}\n")
    print(f"问题: {QUESTION}\n")
    print("-" * 50)

    for temp in (0.2, 1.0):
        reply = ask(client, temp)
        print(f"\n[temperature={temp}]")
        print(reply)

    print("\n" + "-" * 50)
    print("观察: 0.2 通常更稳定；1.0 措辞可能更发散。多跑几次对比更明显。")


if __name__ == "__main__":
    main()
