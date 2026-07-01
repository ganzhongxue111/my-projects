"""Day 1：命令行多轮对话。"""
from llm_client import LLMClient

SYSTEM_PROMPT = "你是一个有帮助的 Python 学习助手，回答简洁清晰。"
EXIT_WORDS = {"exit", "quit", "q", "退出"}


def main() -> None:
    client = LLMClient()
    print(f"已连接: {client.info()}")
    print("输入问题开始对话，输入 exit / quit / q 退出\n")

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
        reply = client.chat(messages, temperature=0.2)
        messages.append({"role": "assistant", "content": reply})
        print(f"Assistant: {reply}\n")


if __name__ == "__main__":
    main()
