"""LLMClient 单元测试（mock API，不消耗额度）。"""
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "projects" / "week1-agent"))
from llm_client import LLMClient  # noqa: E402


def _mock_completion(content: str = "测试回复") -> MagicMock:
    msg = MagicMock()
    msg.content = content
    choice = MagicMock()
    choice.message = msg
    resp = MagicMock()
    resp.choices = [choice]
    return resp


@patch.dict(
    "llm_client.os.environ",
    {
        "LLM_PROVIDER": "dashscope",
        "DASHSCOPE_API_KEY": "sk-test-key-12345678",
        "DASHSCOPE_BASE_URL": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "DASHSCOPE_MODEL": "qwen-plus",
    },
)
@patch("llm_client.OpenAI")
def test_chat_returns_content(mock_openai_cls: MagicMock) -> None:
    mock_client = MagicMock()
    mock_openai_cls.return_value = mock_client
    mock_client.chat.completions.create.return_value = _mock_completion("你好")

    client = LLMClient()
    result = client.chat([{"role": "user", "content": "hi"}])

    assert result == "你好"
    mock_client.chat.completions.create.assert_called_once()


@patch.dict(
    "llm_client.os.environ",
    {
        "LLM_PROVIDER": "dashscope",
        "DASHSCOPE_API_KEY": "sk-test-key-12345678",
        "DASHSCOPE_MODEL": "qwen-plus",
    },
)
@patch("llm_client.OpenAI")
def test_chat_stream_yields_chunks(mock_openai_cls: MagicMock) -> None:
    mock_client = MagicMock()
    mock_openai_cls.return_value = mock_client

    chunk1, chunk2 = MagicMock(), MagicMock()
    chunk1.choices = [MagicMock(delta=MagicMock(content="你"))]
    chunk2.choices = [MagicMock(delta=MagicMock(content="好"))]
    mock_client.chat.completions.create.return_value = iter([chunk1, chunk2])

    client = LLMClient()
    text = "".join(client.chat_stream([{"role": "user", "content": "hi"}]))

    assert text == "你好"
    call_kwargs = mock_client.chat.completions.create.call_args.kwargs
    assert call_kwargs.get("stream") is True


def test_estimate_tokens_non_empty() -> None:
    assert LLMClient.estimate_tokens("hello world") >= 1


@patch.dict("llm_client.os.environ", {"LLM_PROVIDER": "dashscope"}, clear=False)
def test_missing_api_key_raises() -> None:
    with patch.dict("llm_client.os.environ", {"DASHSCOPE_API_KEY": ""}, clear=False):
        with pytest.raises(ValueError, match="DASHSCOPE_API_KEY"):
            LLMClient()
