# Contributing to RAG Chunk Visualizer

## Project Status | 项目状态

This is currently a personal project maintained by [@PerryLink](https://github.com/PerryLink). While contributions are welcome, please note that this project is primarily developed and maintained by a single person.

这是一个由 [@PerryLink](https://github.com/PerryLink) 个人维护的项目。虽然欢迎贡献，但请注意这个项目主要由一个人开发和维护。

---

## How to Report Issues | 如何报告问题

If you encounter a bug or have a feature request, please:

如果你遇到 bug 或有功能请求，请：

1. **Search existing issues** to avoid duplicates | **搜索现有 issues** 避免重复
2. **Create a new issue** with a clear title and description | **创建新 issue** 并提供清晰的标题和描述
3. **Include the following information** | **包含以下信息**：
   - Python version | Python 版本
   - Operating system | 操作系统
   - Steps to reproduce the issue | 重现问题的步骤
   - Expected vs actual behavior | 期望行为 vs 实际行为
   - Error messages or screenshots (if applicable) | 错误信息或截图（如适用）

---

## Development Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.8 or higher | Python 3.8 或更高版本
- Git

### Setup Steps | 搭建步骤

1. **Fork and clone the repository** | **Fork 并克隆仓库**

```bash
git clone https://github.com/PerryLink/rag-chunk-visualizer.git
cd rag-chunk-visualizer
```

2. **Install dependencies** | **安装依赖**

```bash
pip install jinja2 rich chardet
```

3. **Install development dependencies** | **安装开发依赖**

```bash
pip install pytest pytest-cov black ruff
```

4. **Run tests to verify setup** | **运行测试验证安装**

```bash
PYTHONPATH=src pytest tests/ -v
```

---

## Code Standards | 代码规范

This project follows **PEP 8** style guidelines. Please ensure your code adheres to these standards.

本项目遵循 **PEP 8** 代码风格指南。请确保你的代码符合这些标准。

### Formatting | 格式化

Before submitting code, format it with Black:

提交代码前，使用 Black 格式化：

```bash
black src/ tests/
```

### Linting | 代码检查

Check your code with Ruff:

使用 Ruff 检查代码：

```bash
ruff check src/ tests/
```

### Testing | 测试

All new features and bug fixes should include tests:

所有新功能和 bug 修复都应包含测试：

```bash
PYTHONPATH=src pytest tests/ -v --cov=rag_chunk_visualizer
```

---

## Pull Request Process | 提交 Pull Request 流程

1. **Create a feature branch** | **创建功能分支**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** | **进行修改**
   - Write clean, readable code | 编写清晰、可读的代码
   - Add tests for new functionality | 为新功能添加测试
   - Update documentation if needed | 如需要更新文档

3. **Test your changes** | **测试你的修改**

```bash
PYTHONPATH=src pytest tests/ -v
black src/ tests/
ruff check src/ tests/
```

4. **Commit your changes** | **提交你的修改**

```bash
git add .
git commit -m "Brief description of your changes"
```

Follow conventional commit format:
- `feat:` for new features | 新功能
- `fix:` for bug fixes | bug 修复
- `docs:` for documentation changes | 文档修改
- `refactor:` for code refactoring | 代码重构
- `test:` for test additions/changes | 测试添加/修改

5. **Push to your fork** | **推送到你的 fork**

```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request** | **创建 Pull Request**
   - Provide a clear title and description | 提供清晰的标题和描述
   - Reference any related issues | 引用相关的 issues
   - Explain what changes you made and why | 解释你做了什么修改以及为什么

---

## Code Review | 代码审查

- The maintainer will review your PR as soon as possible | 维护者会尽快审查你的 PR
- Be open to feedback and suggestions | 对反馈和建议保持开放态度
- Make requested changes in new commits | 在新提交中进行请求的修改
- Once approved, your PR will be merged | 一旦批准，你的 PR 将被合并

---

## Questions? | 有问题？

If you have any questions about contributing, feel free to:

如果你对贡献有任何问题，请随时：

- Open an issue for discussion | 开启 issue 进行讨论
- Contact the maintainer at novelnexusai@outlook.com | 联系维护者：novelnexusai@outlook.com

---

Thank you for contributing to RAG Chunk Visualizer!

感谢你为 RAG Chunk Visualizer 做出贡献！
