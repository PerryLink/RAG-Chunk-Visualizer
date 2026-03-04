"""核心切分算法"""

from dataclasses import dataclass
from typing import List


@dataclass
class Chunk:
    text: str
    start_pos: int
    end_pos: int
    index: int
    overlap_chars: int


def chunk_text(text: str, chunk_size: int, overlap: int) -> List[Chunk]:
    """使用滑动窗口切分文本"""
    if chunk_size <= 0:
        raise ValueError("chunk_size 必须大于 0")
    if overlap < 0:
        raise ValueError("overlap 必须大于等于 0")
    if overlap >= chunk_size:
        raise ValueError("overlap 必须小于 chunk_size")

    chunks = []
    position = 0
    chunk_index = 0

    while position < len(text):
        end = min(position + chunk_size, len(text))
        chunk_text_content = text[position:end]
        overlap_chars = overlap if chunk_index > 0 else 0

        chunks.append(
            Chunk(
                text=chunk_text_content,
                start_pos=position,
                end_pos=end,
                index=chunk_index,
                overlap_chars=overlap_chars,
            )
        )

        position += chunk_size - overlap
        chunk_index += 1

    return chunks
