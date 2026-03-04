"""HTML 渲染器"""

from typing import List
from jinja2 import Template
from .core import Chunk


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAG Chunk Visualizer</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; background: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        .header { padding: 20px; border-bottom: 2px solid #e0e0e0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 8px 8px 0 0; }
        .header h1 { font-size: 24px; margin-bottom: 10px; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; margin-top: 15px; }
        .stat-item { background: rgba(255,255,255,0.2); padding: 10px; border-radius: 4px; }
        .stat-label { font-size: 12px; opacity: 0.9; }
        .stat-value { font-size: 20px; font-weight: bold; margin-top: 5px; }
        .content { padding: 30px; line-height: 1.8; font-size: 16px; white-space: pre-wrap; word-wrap: break-word; }
        .chunk { display: inline; cursor: pointer; transition: all 0.2s; position: relative; }
        .chunk:hover { filter: brightness(0.85); }
        .chunk-0 { background-color: rgba(255, 107, 107, 0.3); }
        .chunk-1 { background-color: rgba(78, 205, 196, 0.3); }
        .chunk-2 { background-color: rgba(255, 195, 113, 0.3); }
        .overlap { background: repeating-linear-gradient(45deg, transparent, transparent 2px, rgba(0,0,0,0.1) 2px, rgba(0,0,0,0.1) 4px); border-left: 2px solid rgba(0,0,0,0.3); }
        .tooltip { position: fixed; background: rgba(0,0,0,0.9); color: white; padding: 10px 15px; border-radius: 4px; font-size: 14px; pointer-events: none; z-index: 1000; display: none; max-width: 300px; }
        .tooltip-row { margin: 3px 0; }
        .tooltip-label { opacity: 0.8; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>RAG Chunk Visualizer</h1>
            <div class="stats">
                <div class="stat-item">
                    <div class="stat-label">总 Chunk 数</div>
                    <div class="stat-value">{{ total_chunks }}</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">Chunk 大小</div>
                    <div class="stat-value">{{ chunk_size }}</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">重叠大小</div>
                    <div class="stat-value">{{ overlap }}</div>
                </div>
                <div class="stat-item">
                    <div class="stat-label">总字符数</div>
                    <div class="stat-value">{{ total_chars }}</div>
                </div>
            </div>
        </div>
        <div class="content">{% for chunk in chunks %}<span class="chunk chunk-{{ chunk.index % 3 }}{% if chunk.overlap_chars > 0 %} overlap{% endif %}" data-index="{{ chunk.index }}" data-start="{{ chunk.start_pos }}" data-end="{{ chunk.end_pos }}" data-chars="{{ chunk.end_pos - chunk.start_pos }}" data-overlap="{{ chunk.overlap_chars }}">{{ chunk.text }}</span>{% endfor %}</div>
    </div>
    <div class="tooltip" id="tooltip"></div>
    <script>
        const tooltip = document.getElementById('tooltip');
        const chunks = document.querySelectorAll('.chunk');

        chunks.forEach(chunk => {
            chunk.addEventListener('mouseenter', (e) => {
                const index = chunk.dataset.index;
                const start = chunk.dataset.start;
                const end = chunk.dataset.end;
                const chars = chunk.dataset.chars;
                const overlap = chunk.dataset.overlap;

                tooltip.innerHTML = `
                    <div class="tooltip-row"><span class="tooltip-label">Chunk:</span> #${index}</div>
                    <div class="tooltip-row"><span class="tooltip-label">位置:</span> ${start}-${end}</div>
                    <div class="tooltip-row"><span class="tooltip-label">字符数:</span> ${chars}</div>
                    <div class="tooltip-row"><span class="tooltip-label">重叠:</span> ${overlap}</div>
                `;
                tooltip.style.display = 'block';
            });

            chunk.addEventListener('mousemove', (e) => {
                tooltip.style.left = (e.clientX + 15) + 'px';
                tooltip.style.top = (e.clientY + 15) + 'px';
            });

            chunk.addEventListener('mouseleave', () => {
                tooltip.style.display = 'none';
            });
        });
    </script>
</body>
</html>"""


def generate_html(chunks: List[Chunk], chunk_size: int, overlap: int, total_chars: int) -> str:
    """生成 HTML 可视化文件"""
    template = Template(HTML_TEMPLATE)
    return template.render(
        chunks=chunks,
        total_chunks=len(chunks),
        chunk_size=chunk_size,
        overlap=overlap,
        total_chars=total_chars,
    )
