"""工具函数"""

import chardet


def read_file_with_encoding(file_path: str, encoding: str = None) -> str:
    """读取文件并自动检测编码"""
    if encoding:
        with open(file_path, "r", encoding=encoding) as f:
            return f.read()

    with open(file_path, "rb") as f:
        raw_data = f.read()

    detected = chardet.detect(raw_data)
    detected_encoding = detected["encoding"] or "utf-8"

    try:
        return raw_data.decode(detected_encoding)
    except (UnicodeDecodeError, LookupError):
        return raw_data.decode("utf-8", errors="replace")
