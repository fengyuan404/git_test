#!/usr/bin/env python3
"""
🍉 水果目录管理工具 — 一个简单的命令行水果清单管理器。
"""

import sys
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "fruits.txt")

def load():
    """读取水果清单"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save(fruits):
    """保存水果清单"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(fruits) + "\n")

def cmd_list():
    fruits = load()
    if not fruits:
        print("🍽️  清单为空，快加点水果吧！")
        return
    print(f"\n🍉 当前库存（共 {len(fruits)} 种）：\n")
    for i, fruit in enumerate(fruits, 1):
        print(f"  {i:>2}. {fruit}")
    print()

def cmd_add(name):
    fruits = load()
    if name in fruits:
        print(f"⚠️  「{name}」已经在清单里了。")
        return
    fruits.append(name)
    save(fruits)
    print(f"✅ 已添加「{name}」。")

def cmd_remove(name):
    fruits = load()
    if name not in fruits:
        print(f"❌ 未找到「{name}」。")
        return
    fruits.remove(name)
    save(fruits)
    print(f"🗑️  已移除「{name}」。")

def cmd_search(keyword):
    fruits = load()
    matches = [f for f in fruits if keyword in f]
    if not matches:
        print(f"🔍 没有找到包含「{keyword}」的水果。")
        return
    print(f"\n🔍 找到 {len(matches)} 个匹配：\n")
    for f in matches:
        print(f"  🍎 {f}")
    print()

def cmd_sort():
    fruits = load()
    fruits.sort()
    save(fruits)
    print("🔤 已按字母顺序排序。")
    cmd_list()

def cmd_count():
    fruits = load()
    print(f"📊 当前共有 {len(fruits)} 种水果。")

def cmd_random():
    import random
    fruits = load()
    if not fruits:
        print("清单为空。")
        return
    print(f"🎲 随机推荐：{random.choice(fruits)}")

def usage():
    print("""
🍉 水果目录管理工具

用法:
  python fruits.py list        列出所有水果
  python fruits.py add <名称>   添加一种水果
  python fruits.py remove <名称> 移除一种水果
  python fruits.py search <关键词> 搜索水果
  python fruits.py sort         按字母排序
  python fruits.py count        统计数量
  python fruits.py random       随机推荐

示例:
  python fruits.py add 榴莲
  python fruits.py search 莓
""")


def main():
    if len(sys.argv) < 2:
        usage()
        return

    cmd = sys.argv[1].lower()
    arg = sys.argv[2] if len(sys.argv) > 2 else None

    commands = {
        "list": cmd_list,
        "add": lambda: cmd_add(arg) if arg else print("❌ 请输入水果名称。"),
        "remove": lambda: cmd_remove(arg) if arg else print("❌ 请输入要移除的水果名称。"),
        "search": lambda: cmd_search(arg) if arg else print("❌ 请输入搜索关键词。"),
        "sort": cmd_sort,
        "count": cmd_count,
        "random": cmd_random,
    }

    if cmd in commands:
        commands[cmd]()
    else:
        print(f"❌ 未知命令: {cmd}")
        usage()


if __name__ == "__main__":
    main()
