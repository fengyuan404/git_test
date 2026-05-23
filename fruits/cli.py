"""💻 CLI 工具 — 命令行水果数据查询。"""
from . import data, analytics


def run(args):
    if not args:
        print("""
🍉 水果目录 CLI

用法:
  python -m fruits list              列出所有水果
  python -m fruits info <名称>        查看营养详情
  python -m fruits search <关键词>     搜索水果
  python -m fruits top <字段> [n]     Top N 排行
  python -m fruits stats              统计概览
  python -m fruits report             生成数据报告

字段: kcal / carbs / protein / fat / fiber / vitamin_c

示例:
  python -m fruits info 香蕉
  python -m fruits top vitamin_c 3
  python -m fruits report
""")
        return

    cmd = args[0]

    if cmd == "list":
        for name in data.names():
            print(f"  🍎 {name}")

    elif cmd == "info":
        if len(args) < 2:
            print("❌ 请输入水果名称")
            return
        fruit = data.get(args[1])
        if not fruit:
            print(f"❌ 未找到「{args[1]}」")
            return
        print(f"\n🍎 {args[1]}")
        print(f"  热量:     {fruit['kcal']} kcal/100g")
        print(f"  碳水:     {fruit['carbs']} g")
        print(f"  蛋白质:   {fruit['protein']} g")
        print(f"  脂肪:     {fruit['fat']} g")
        print(f"  膳食纤维: {fruit['fiber']} g")
        print(f"  维生素C:  {fruit['vitamin_c']} mg")
        print(f"  季节:     {fruit['season']}")

    elif cmd == "search":
        if len(args) < 2:
            print("❌ 请输入关键词")
            return
        result = data.search(args[1])
        for name in result:
            print(f"  🍎 {name}")

    elif cmd == "top":
        field = args[1] if len(args) > 1 else "vitamin_c"
        n = int(args[2]) if len(args) > 2 else 5
        result = data.top_by(field, n)
        print(f"\n🥇 {field} Top {n}:")
        for i, (name, info) in enumerate(result.items(), 1):
            print(f"  {i}. {name} — {info[field]}")

    elif cmd == "stats":
        st = data.stats()
        print(f"\n📊 共 {st['count']} 种水果")
        for field in ["kcal", "carbs", "protein", "fat", "fiber", "vitamin_c"]:
            print(f"  {field}: 最高 {st[field]['max']} / 平均 {st[field]['avg']}")

    elif cmd == "report":
        print(analytics.summary())

    else:
        print(f"❌ 未知命令: {cmd}")
