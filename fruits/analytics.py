"""📊 数据分析与可视化 — 零依赖 SVG 图表生成。"""

from . import data

LABELS = {
    "kcal": "热量 (kcal/100g)",
    "carbs": "碳水 (g/100g)",
    "protein": "蛋白质 (g/100g)",
    "fat": "脂肪 (g/100g)",
    "fiber": "膳食纤维 (g/100g)",
    "vitamin_c": "维生素C (mg/100g)",
}

COLORS = ["#FF6384","#36A2EB","#FFCE56","#4BC0C0","#9966FF","#FF9F40","#C9CBCF","#7BC8A4","#E8A87C"]


def generate_chart(field):
    """生成营养对比柱状图 SVG（纯 Python，零依赖）"""
    fruits = data.get_all()
    names = list(fruits.keys())
    values = [fruits[n][field] for n in names]
    label = LABELS.get(field, field)
    max_val = max(values)

    bar_w = 50
    gap = 20
    chart_w = len(names) * (bar_w + gap) + 60
    chart_h = 300
    left_margin = 80
    bottom_margin = 80
    total_w = chart_w + left_margin
    total_h = chart_h + bottom_margin

    bars_svg = ""
    for i, (name, val) in enumerate(zip(names, values)):
        x = left_margin + i * (bar_w + gap)
        bar_h = (val / max_val) * chart_h
        y = chart_h - bar_h + 10
        color = COLORS[i % len(COLORS)]
        label_x = left_margin + i * (bar_w + gap) + bar_w / 2

        bars_svg += f'''
        <rect x="{x}" y="{y}" width="{bar_w}" height="{bar_h:.1f}" rx="4"
              fill="{color}" opacity="0.85">
          <title>{name}: {val}</title>
        </rect>
        <text x="{label_x}" y="{total_h - 45}" text-anchor="middle"
              fill="#ccc" font-size="12">{name}</text>
        <text x="{x + bar_w/2}" y="{y - 5}" text-anchor="middle"
              fill="#fff" font-size="11" font-weight="bold">{val}</text>'''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}"
     width="100%" height="100%" style="background:#1a1a2e;border-radius:12px">
  <text x="20" y="30" fill="#ffd200" font-size="18" font-weight="bold">🍉 {label} 对比</text>
  {bars_svg}
  <line x1="{left_margin}" y1="{total_h - 30}" x2="{left_margin+chart_w}" y2="{total_h - 30}"
        stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
</svg>'''
    return svg


def summary():
    """生成文本摘要报告"""
    fruits = data.get_all()
    st = data.stats()

    lines = [
        "=" * 40,
        "🍉 水果营养数据报告",
        "=" * 40,
        f"\n📊 共收录 {st['count']} 种水果\n",
    ]

    for field, label in LABELS.items():
        f = st[field]
        top_fruit = max(fruits, key=lambda k: fruits[k][field])
        lines.append(f"  {label}: 最高 {top_fruit}({f['max']}) / 最低 {f['min']} / 平均 {f['avg']}")

    lines.append("\n" + "=" * 40)
    return "\n".join(lines)
