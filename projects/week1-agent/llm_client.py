"""OpenAI 兼容 API 统一客户端（DashScope / DeepSeek / OpenAI）。"""
from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(ROOT / ".env")

PROVIDER_CONFIG = {
    "dashscope": {
        "key_env": "DASHSCOPE_API_KEY",
        "url_env": "DASHSCOPE_BASE_URL",
        "url_default": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model_env": "DASHSCOPE_MODEL",
        "model_default": "qwen-plus",
        "placeholder": "sk-your",
    },
    "deepseek": {
        "key_env": "DEEPSEEK_API_KEY",
        "url_env": "DEEPSEEK_BASE_URL",
        "url_default": "https://api.deepseek.com",
        "model_env": "DEEPSEEK_MODEL",
        "model_default": "deepseek-chat",
        "placeholder": "sk-your",
    },
    "openai": {
        "key_env": "OPENAI_API_KEY",
        "url_env": "OPENAI_BASE_URL",
        "url_default": "https://api.openai.com/v1",
        "model_env": "OPENAI_MODEL",
        "model_default": "gpt-4o-mini",
        "placeholder": "sk-your",
    },
}


class LLMClient:
    """封装 chat / stream，切换 provider 只需改 .env 中 LLM_PROVIDER。"""

    def __init__(self, provider: str | None = None) -> None:
        self.provider = (provider or os.getenv("LLM_PROVIDER", "dashscope")).lower().strip()
        if self.provider not in PROVIDER_CONFIG:
            raise ValueError(f"未知 provider: {self.provider}，可选: {list(PROVIDER_CONFIG)}")

        cfg = PROVIDER_CONFIG[self.provider]
        key = os.getenv(cfg["key_env"], "").strip()
        if not key or key.startswith(cfg["placeholder"]):
            raise ValueError(f"请在 .env 中配置 {cfg['key_env']}")

        self.model = os.getenv(cfg["model_env"], cfg["model_default"]).strip()
        self._client = OpenAI(
            api_key=key,
            base_url=os.getenv(cfg["url_env"], cfg["url_default"]).strip(),
        )

    def chat(
        self,
        messages: list[dict[str, str]],
        *,
        max_tokens: int = 1024,
        temperature: float = 0.7,
    ) -> str:
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        content = resp.choices[0].message.content
        return content or ""

    def chat_stream(
        self,
        messages: list[dict[str, str]],
        *,
        max_tokens: int = 1024,
        temperature: float = 0.7,
    ) -> Iterator[str]:
        stream = self._client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

    @staticmethod
    def estimate_tokens(text: str) -> int:
        """粗略估算 token 数；有 tiktoken 时更准。"""
        try:
            import tiktoken

            enc = tiktoken.get_encoding("cl100k_base")
            return len(enc.encode(text))
        except Exception:
            return max(1, len(text) // 2)

    def info(self) -> str:
        return f"{self.provider} / {self.model}"
