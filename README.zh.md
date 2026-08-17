<div align="center">

# RAG-Chunk-Visualizer

**将 RAG 文本切分结果渲染为带重叠高亮的交互式 HTML 可视化的工具。**

*已移植到 [dsh-library](https://github.com/PerryLink/dsh-library) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

RAG-Chunk-Visualizer 按可配置的 chunk 大小与重叠长度将文本文件切分成多个块，并生成一张颜色编码的 HTML 页面，展示每个 chunk、重叠区域以及各 chunk 的统计信息，帮助开发者直观查看切分参数对结果的影响。

## 功能特性

- 生成交互式、颜色编码的 HTML 输出
- 以斜纹高亮标记重叠区域
- 悬停提示显示 chunk 索引、位置与字符数
- 使用 chardet 自动检测文本编码
- 使用 Rich 在终端汇总 chunk 数量、大小与输出路径

## 快速开始

需要 Python 3.8+ 与 [Poetry](https://python-poetry.org/)。

```bash
git clone https://github.com/PerryLink/RAG-Chunk-Visualizer.git
cd RAG-Chunk-Visualizer
poetry install
```

## 使用方法

```bash
# 使用默认 chunk 大小（200）与重叠（50）
rag-chunk-visualizer input.txt

# 或以模块方式运行
python -m rag_chunk_visualizer input.txt

# 自定义 chunk 大小、重叠与输出文件
rag-chunk-visualizer -s 500 -o 100 -O result.html input.txt

# 详细输出
rag-chunk-visualizer -v input.txt
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `input_file` | — | 输入文本文件路径（位置参数，必需） |
| `-s`, `--chunk-size` | `200` | Chunk 大小（字符数） |
| `-o`, `--overlap` | `50` | 重叠大小（字符数） |
| `-O`, `--output` | `output.html` | 输出 HTML 文件路径 |
| `--encoding` | 自动检测 | 文本编码 |
| `-v`, `--verbose` | 关 | 详细输出 |
| `--version` | — | 显示版本 |

示例：

```bash
echo "这是一段测试文本。它包含多个句子，用于验证切分效果。重叠区域应该被正确标记。RAG系统需要将长文本切分成多个chunk，以便更好地进行检索和生成。" > test.txt
rag-chunk-visualizer -s 30 -o 10 test.txt
```

在浏览器中打开生成的 `output.html` 即可查看切分布局。

基于 Jinja2、Rich 与 chardet 构建；测试使用 pytest。

## 开发

```bash
poetry run pytest -v
```

## 相关项目

- [dsh-library](https://github.com/PerryLink/dsh-library) —— 本工具已移植进的 DSH 插件
- [PerryLink](https://github.com/PerryLink) —— PerryLink DSH 插件家族

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
