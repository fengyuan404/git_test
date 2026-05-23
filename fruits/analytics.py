"""📊 数据分析与可视化 — 水果营养数据图表生成。"""

import io
import base64
from . import data

LABELS = {
    "kcal": "热量 (kcal/100g)",
    "carbs": "碳水 (g/100g)",
    "protein": "蛋白质 (g/100g)",
    "fat": "脂肪 (g/100g)",
    "fiber": "膳食纤维 (g/100g)",
    "vitamin_c": "维生素C (mg/100g)",
}


def generate_chart(field):
    """生成营养对比柱状图，返回 Base64 PNG"""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fruits = data.get_all()
        names = list(fruits.keys())
        values = [fruits[n][field] for n in names]

        # 设置中文字体
        plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
        plt.rcParams["axes.unicode_minus"] = False

        fig, ax = plt.subplots(figsize=(10, 5))
        colors = plt.cm.Set3(range(len(names)))
        bars = ax.bar(names, values, color=colors, edgecolor="white", linewidth=0.5)

        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(values) * 0.01,
                    str(val), ha="center", va="bottom", fontsize=9, fontweight="bold")

        ax.set_title(f"🍉 水果 {LABELS.get(field, field)} 对比", fontsize=14, fontweight="bold")
        ax.set_ylabel(LABELS.get(field, field))
        ax.set_ylim(0, max(values) * 1.15)

        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format="png", dpi=100)
        plt.close()
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")
    except ImportError:
        return None


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
