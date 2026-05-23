"""🍉 水果数据引擎 — 包含真实营养数据的水果数据库。"""

# 每 100g 的营养数据：热量(kcal)、碳水(g)、蛋白质(g)、脂肪(g)、纤维(g)、维C(mg)
FRUITS = {
    "香蕉":   {"kcal": 89,  "carbs": 22.8, "protein": 1.1, "fat": 0.3, "fiber": 2.6, "vitamin_c": 8.7,  "season": "全年"},
    "草莓":   {"kcal": 32,  "carbs": 7.7,  "protein": 0.7, "fat": 0.3, "fiber": 2.0, "vitamin_c": 58.8, "season": "冬春"},
    "芒果":   {"kcal": 60,  "carbs": 15.0, "protein": 0.8, "fat": 0.4, "fiber": 1.6, "vitamin_c": 36.4, "season": "春夏"},
    "苹果":   {"kcal": 52,  "carbs": 13.8, "protein": 0.3, "fat": 0.2, "fiber": 2.4, "vitamin_c": 4.6,  "season": "秋冬"},
    "西瓜":   {"kcal": 30,  "carbs": 7.6,  "protein": 0.6, "fat": 0.2, "fiber": 0.4, "vitamin_c": 8.1,  "season": "夏季"},
    "杨梅":   {"kcal": 34,  "carbs": 8.2,  "protein": 0.6, "fat": 0.3, "fiber": 1.0, "vitamin_c": 43.0, "season": "夏季"},
    "橘子":   {"kcal": 47,  "carbs": 11.8, "protein": 0.9, "fat": 0.1, "fiber": 2.4, "vitamin_c": 53.2, "season": "秋冬"},
    "葡萄":   {"kcal": 69,  "carbs": 18.1, "protein": 0.7, "fat": 0.2, "fiber": 0.9, "vitamin_c": 3.2,  "season": "夏秋"},
    "蓝莓":   {"kcal": 57,  "carbs": 14.5, "protein": 0.7, "fat": 0.3, "fiber": 2.4, "vitamin_c": 9.7,  "season": "夏季"},
}


def get_all():
    """返回所有水果数据"""
    return dict(FRUITS)


def get(name):
    """获取单个水果的营养数据"""
    return FRUITS.get(name)


def search(keyword):
    """按名称搜索水果"""
    return {k: v for k, v in FRUITS.items() if keyword in k}


def filter_by_season(season):
    """按季节筛选"""
    return {k: v for k, v in FRUITS.items() if v["season"] == season}


def top_by(field, n=5):
    """按某营养指标排序取 Top N"""
    sorted_items = sorted(FRUITS.items(), key=lambda x: x[1][field], reverse=True)
    return dict(sorted_items[:n])


def stats():
    """全局统计"""
    count = len(FRUITS)
    fields = ["kcal", "carbs", "protein", "fat", "fiber", "vitamin_c"]
    result = {"count": count}
    for field in fields:
        values = [v[field] for v in FRUITS.values()]
        result[field] = {
            "max": max(values),
            "min": min(values),
            "avg": round(sum(values) / count, 1),
        }
    return result


def names():
    """获取水果名称列表"""
    return list(FRUITS.keys())
