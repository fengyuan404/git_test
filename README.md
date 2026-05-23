# 🍉 Fruit Catalog

> 基于真实营养数据的水果数据库，提供 REST API、命令行工具和可视化分析。

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg?style=flat&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## ✨ 特性

- 📊 **真实营养数据** — 每种水果包含热量、碳水、蛋白质、脂肪、纤维、维生素 C
- 🌐 **REST API** — 基于 FastAPI，自动生成 Swagger 文档
- 📈 **数据可视化** — 营养对比柱状图，API 直出 Base64 图片
- 🐳 **Docker 部署** — 一行命令启动微服务
- 💻 **CLI 工具** — 命令行查询、搜索、排行

## 🚀 快速开始

### 方式一：本地运行

```bash
pip install -e .
python -m fruits info 香蕉
```

### 方式二：启动 API 服务

```bash
pip install -r requirements.txt
uvicorn fruits.api:app --reload
```

打开 http://localhost:8000/docs 查看交互式 API 文档。

### 方式三：Docker 部署

```bash
docker-compose up -d
```

## 📡 API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/fruits` | 获取所有水果及营养数据 |
| GET | `/fruits/{name}` | 查询单个水果详情 |
| GET | `/fruits/search?q=莓` | 按名称搜索 |
| GET | `/fruits/season/夏季` | 按季节筛选 |
| GET | `/fruits/top/vitamin_c?n=3` | 按营养指标 Top N |
| GET | `/fruits/stats` | 全局统计概览 |
| GET | `/chart/vitamin_c` | 营养对比柱状图（Base64） |

## 💻 CLI 命令

```bash
python -m fruits list              # 列出所有水果
python -m fruits info 香蕉          # 查看营养详情
python -m fruits search 莓          # 搜索水果
python -m fruits top vitamin_c 3   # 维C含量 Top 3
python -m fruits stats              # 统计概览
python -m fruits report             # 生成数据报告
```

## 🗄️ 数据示例

```json
{
  "香蕉": {
    "kcal": 89,
    "carbs": 22.8,
    "protein": 1.1,
    "fat": 0.3,
    "fiber": 2.6,
    "vitamin_c": 8.7,
    "season": "全年"
  }
}
```

## 📁 项目结构

```
.
├── fruits/            # Python 包
│   ├── __init__.py
│   ├── __main__.py    # python -m fruits 入口
│   ├── data.py        # 水果营养数据库
│   ├── api.py         # FastAPI 应用
│   ├── cli.py         # 命令行工具
│   └── analytics.py   # 数据分析与可视化
├── setup.py           # 安装配置
├── requirements.txt   # 依赖清单
├── Dockerfile         # Docker 镜像
├── docker-compose.yml # 一键部署
└── README.md
```

## 🧪 API 调用示例

```bash
# 查询香蕉的营养数据
curl http://localhost:8000/fruits/香蕉

# 维C含量 Top 3
curl http://localhost:8000/fruits/top/vitamin_c?n=3

# 获取热量对比图
curl http://localhost:8000/chart/kcal
```

## 📄 License

MIT © 2025
