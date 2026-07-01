"""Day 1：流式输出 + 粗略 token 统计。"""
import sys

from llm_client import LLMClient

SYSTEM_PROMPT = "你是一个有帮助的 Python 学习助手，回答简洁清晰。"
EXIT_WORDS = {"exit", "quit", "q", "退出"}


def main() -> None:
    client = LLMClient()
    print(f"已连接: {client.info()} [流式模式]")
    print("输入 exit / quit / q 退出\n")

    messages: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见。")
            break

        if not user_input:
            continue
        if user_input.lower() in EXIT_WORDS:
            print("再见。")
            break

        messages.append({"role": "user", "content": user_input})
        print("Assistant: ", end="", flush=True)

        chunks: list[str] = []
        for piece in client.chat_stream(messages):
            chunks.append(piece)
            print(piece, end="", flush=True)

        reply = "".join(chunks)
        messages.append({"role": "assistant", "content": reply})

        in_tok = client.estimate_tokens(user_input)
        out_tok = client.estimate_tokens(reply)
        print(f"\n[token 估算] 输入 ~{in_tok} | 输出 ~{out_tok}\n")


if __name__ == "__main__":
    main()
