<div align="center">

# RAG-Chunk-Visualizer

**A tool that renders RAG text chunking as an interactive HTML visualization with overlap highlighting.**

*Ported into [dsh-library](https://github.com/PerryLink/dsh-library) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

RAG-Chunk-Visualizer splits a text file into chunks using a configurable chunk size and overlap, then generates a color-coded HTML page showing each chunk, its overlap regions, and per-chunk statistics so developers can see how their chunking parameters affect the result.

## Features

- Interactive, color-coded HTML output
- Diagonal-stripe highlighting of overlap regions
- Hover tooltips with chunk index, position, and character count
- Automatic encoding detection (chardet)
- Rich terminal summary of chunk count, size, and output path

## Quick start

Requires Python 3.8+ and [Poetry](https://python-poetry.org/).

```bash
git clone https://github.com/PerryLink/RAG-Chunk-Visualizer.git
cd RAG-Chunk-Visualizer
poetry install
```

## Usage

```bash
# Default chunk size (200) and overlap (50)
rag-chunk-visualizer input.txt

# Or run it as a module
python -m rag_chunk_visualizer input.txt

# Custom chunk size, overlap, and output file
rag-chunk-visualizer -s 500 -o 100 -O result.html input.txt

# Verbose output
rag-chunk-visualizer -v input.txt
```

| Option | Default | Description |
|--------|---------|-------------|
| `input_file` | — | Input text file path (positional, required) |
| `-s`, `--chunk-size` | `200` | Chunk size in characters |
| `-o`, `--overlap` | `50` | Overlap size in characters |
| `-O`, `--output` | `output.html` | Output HTML file path |
| `--encoding` | auto-detect | Text encoding |
| `-v`, `--verbose` | off | Verbose output |
| `--version` | — | Show version |

Example:

```bash
echo "This is a test text. It contains multiple sentences used to verify the split. Overlap regions should be marked correctly. RAG systems split long text into chunks for better retrieval and generation." > test.txt
rag-chunk-visualizer -s 30 -o 10 test.txt
```

Open the generated `output.html` in a browser to inspect the chunk layout.

Built with Jinja2, Rich, and chardet; tests use pytest.

## Development

```bash
poetry run pytest -v
```

## Related

- [dsh-library](https://github.com/PerryLink/dsh-library) — the DSH plugin this tool was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH Plugin Family

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
