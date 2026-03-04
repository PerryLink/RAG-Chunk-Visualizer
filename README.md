# RAG Chunk Visualizer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A visualization tool for RAG (Retrieval-Augmented Generation) text chunking. Helps developers intuitively understand chunk splitting effects, overlap regions, and context boundaries.

RAG（检索增强生成）文本切分可视化工具。帮助开发者直观理解 chunk 切分效果、重叠区域和上下文边界。

---

## Features | 特性

- **Interactive HTML Visualization** - Color-coded chunks with hover tooltips | 交互式 HTML 可视化，颜色编码的 chunk 和悬停提示
- **Clear Overlap Marking** - Diagonal stripes highlight overlapping regions | 清晰的重叠区域标记，斜纹高亮显示
- **Real-time Statistics** - Chunk count, size, and overlap metrics | 实时统计信息，包括 chunk 数量、大小和重叠度量
- **Color Coding** - Three-color rotation for easy chunk distinction | 三色循环标记，轻松区分不同 chunk
- **Detailed Tooltips** - Hover to see chunk index, position, and character count | 详细的工具提示，悬停查看 chunk 索引、位置和字符数
- **CLI Interface** - Simple command-line tool with rich output | 简洁的命令行界面，丰富的输出显示

---

## Quick Start | 快速开始

### Installation | 安装

```bash
# Clone the repository | 克隆仓库
git clone https://github.com/PerryLink/rag-chunk-visualizer.git
cd rag-chunk-visualizer

# Install dependencies | 安装依赖
pip install jinja2 rich chardet
```

### Basic Usage | 基本使用

```bash
# Basic usage with default parameters | 使用默认参数
python -m rag_chunk_visualizer input.txt

# Custom chunk size and overlap | 自定义 chunk 大小和重叠
python -m rag_chunk_visualizer -s 500 -o 100 -O result.html input.txt

# Verbose output | 详细输出
python -m rag_chunk_visualizer -v input.txt
```

---

## Usage Guide | 使用指南

### Command Line Arguments | 命令行参数

```
rag-chunk-visualizer [OPTIONS] INPUT_FILE

Arguments | 参数:
  INPUT_FILE              Input text file path | 输入文本文件路径（必需）

Options | 选项:
  -s, --chunk-size INT    Chunk size in characters [default: 200] | Chunk 大小（字符数）[默认: 200]
  -o, --overlap INT       Overlap size in characters [default: 50] | 重叠大小（字符数）[默认: 50]
  -O, --output PATH       Output HTML file path [default: output.html] | 输出 HTML 文件路径 [默认: output.html]
  --encoding TEXT         Text encoding [default: auto-detect] | 文本编码 [默认: 自动检测]
  -v, --verbose           Verbose output | 详细输出
  --version               Show version | 显示版本
  -h, --help              Show help message | 显示帮助信息
```

### Example | 示例

Create a test file | 创建测试文件:

```bash
echo "这是一段测试文本。它包含多个句子，用于验证切分效果。重叠区域应该被正确标记。RAG系统需要将长文本切分成多个chunk，以便更好地进行检索和生成。" > test.txt
```

Run the visualizer | 运行可视化工具:

```bash
python -m rag_chunk_visualizer -s 30 -o 10 test.txt
```

Open the generated `output.html` in your browser to see the visualization.

在浏览器中打开生成的 `output.html` 查看可视化结果。

---

## Project Structure | 项目结构

```
rag-chunk-visualizer/
├── src/rag_chunk_visualizer/
│   ├── __init__.py          # Package initialization | 包初始化
│   ├── __main__.py          # Entry point | 入口点
│   ├── cli.py               # Command-line interface | 命令行接口
│   ├── core.py              # Core chunking algorithm | 核心切分算法
│   ├── renderer.py          # HTML generation | HTML 生成
│   └── utils.py             # Utility functions | 工具函数
├── tests/
│   ├── __init__.py
│   └── test_core.py         # Unit tests | 单元测试
├── pyproject.toml           # Poetry configuration | Poetry 配置
├── README.md                # Project documentation | 项目文档
├── LICENSE                  # Apache 2.0 License | Apache 2.0 许可证
├── CONTRIBUTING.md          # Contribution guidelines | 贡献指南
└── .gitignore               # Git ignore rules | Git 忽略规则
```

---

## Tech Stack | 技术栈

- **Language | 语言**: Python 3.8+
- **Dependencies | 依赖**:
  - [Jinja2](https://jinja.palletsprojects.com/) - HTML template engine | HTML 模板引擎
  - [Rich](https://rich.readthedocs.io/) - CLI beautification | CLI 美化
  - [chardet](https://chardet.readthedocs.io/) - Encoding detection | 编码检测
- **Build Tool | 构建工具**: Poetry
- **Testing | 测试**: pytest

---

## Development | 开发

### Running Tests | 运行测试

```bash
# Install dev dependencies | 安装开发依赖
pip install pytest pytest-cov

# Run tests | 运行测试
PYTHONPATH=src pytest tests/ -v

# Run tests with coverage | 运行测试并生成覆盖率报告
PYTHONPATH=src pytest tests/ -v --cov=rag_chunk_visualizer
```

### Code Style | 代码风格

This project follows PEP 8 style guidelines. Format your code with:

本项目遵循 PEP 8 代码风格指南。使用以下工具格式化代码：

```bash
pip install black ruff
black src/ tests/
ruff check src/ tests/
```

---

## Contributing | 贡献

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

---

## License | 许可证

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

---

## Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com

---

**Made with ❤️ for RAG developers**
