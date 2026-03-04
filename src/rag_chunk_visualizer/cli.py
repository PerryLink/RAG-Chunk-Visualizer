"""命令行接口"""

import argparse
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from . import __version__
from .core import chunk_text
from .renderer import generate_html
from .utils import read_file_with_encoding


console = Console()


def main():
    parser = argparse.ArgumentParser(
        description="RAG Chunk Visualizer - 文本切分可视化工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("input_file", help="输入文本文件路径")
    parser.add_argument("-s", "--chunk-size", type=int, default=200, help="Chunk 大小（字符数）[默认: 200]")
    parser.add_argument("-o", "--overlap", type=int, default=50, help="重叠大小（字符数）[默认: 50]")
    parser.add_argument("-O", "--output", default="output.html", help="输出 HTML 文件路径 [默认: output.html]")
    parser.add_argument("--encoding", help="文本编码 [默认: 自动检测]")
    parser.add_argument("-v", "--verbose", action="store_true", help="详细输出")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    try:
        input_path = Path(args.input_file)
        if not input_path.exists():
            console.print(f"[red]错误: 文件不存在: {args.input_file}[/red]")
            sys.exit(1)

        if args.verbose:
            console.print(f"[cyan]读取文件: {args.input_file}[/cyan]")

        text = read_file_with_encoding(args.input_file, args.encoding)

        if args.verbose:
            console.print(f"[cyan]文件大小: {len(text)} 字符[/cyan]")
            console.print(f"[cyan]切分参数: chunk_size={args.chunk_size}, overlap={args.overlap}[/cyan]")

        chunks = chunk_text(text, args.chunk_size, args.overlap)

        html_content = generate_html(chunks, args.chunk_size, args.overlap, len(text))

        output_path = Path(args.output)
        output_path.write_text(html_content, encoding="utf-8")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("项目", style="cyan")
        table.add_column("值", style="green")
        table.add_row("总 Chunk 数", str(len(chunks)))
        table.add_row("Chunk 大小", str(args.chunk_size))
        table.add_row("重叠大小", str(args.overlap))
        table.add_row("总字符数", str(len(text)))
        table.add_row("输出文件", str(output_path.absolute()))

        console.print(Panel(table, title="[bold green]生成成功[/bold green]", border_style="green"))

    except ValueError as e:
        console.print(f"[red]参数错误: {e}[/red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]错误: {e}[/red]")
        if args.verbose:
            import traceback
            console.print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
