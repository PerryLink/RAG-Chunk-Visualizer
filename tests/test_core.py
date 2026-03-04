"""核心算法测试"""

import pytest
from rag_chunk_visualizer.core import chunk_text, Chunk


def test_basic_chunking():
    text = "0123456789" * 2  # 20 字符
    chunks = chunk_text(text, chunk_size=10, overlap=2)

    assert len(chunks) == 3
    assert chunks[0].text == "0123456789"
    assert chunks[0].start_pos == 0
    assert chunks[0].end_pos == 10
    assert chunks[0].overlap_chars == 0

    assert chunks[1].text == "8901234567"
    assert chunks[1].start_pos == 8
    assert chunks[1].overlap_chars == 2


def test_no_overlap():
    text = "0123456789" * 2
    chunks = chunk_text(text, chunk_size=10, overlap=0)

    assert len(chunks) == 2
    assert chunks[0].text == "0123456789"
    assert chunks[1].text == "0123456789"


def test_last_chunk_smaller():
    text = "0123456789ABC"
    chunks = chunk_text(text, chunk_size=10, overlap=2)

    assert chunks[-1].text == "89ABC"
    assert len(chunks[-1].text) < 10


def test_invalid_params():
    with pytest.raises(ValueError):
        chunk_text("test", chunk_size=0, overlap=0)

    with pytest.raises(ValueError):
        chunk_text("test", chunk_size=10, overlap=-1)

    with pytest.raises(ValueError):
        chunk_text("test", chunk_size=10, overlap=10)


def test_empty_text():
    chunks = chunk_text("", chunk_size=10, overlap=2)
    assert len(chunks) == 0


def test_single_char():
    chunks = chunk_text("A", chunk_size=10, overlap=2)
    assert len(chunks) == 1
    assert chunks[0].text == "A"
