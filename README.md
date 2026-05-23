# 🍉 水果目录

> 一个基于 Git 协作维护的水果清单 —— 用版本控制管理每一颗果实。

[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white)](https://git-scm.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 项目简介

**水果目录** 是一个轻量级、版本可控的水果集合。它既是 Git 分支管理、合并冲突解决、协作工作流的实战演示项目，也是一份简单有趣的数据集。

每一次提交都是一颗水果，每一个分支都是一季丰收。

## 🌳 当前库存

| # | 水果 | # | 水果 | # | 水果 |
|:-:|------|:-:|------|:-:|------|
| 1 | 🍌 香蕉 | 4 | 🍎 苹果 | 7 | 🍊 橘子 |
| 2 | 🍓 草莓 | 5 | 🍉 西瓜 | 8 | 🍇 葡萄 |
| 3 | 🥭 芒果 | 6 | 🫐 杨梅 | 9 | 🫐 蓝莓 |

## 🚀 快速开始

```bash
git clone https://github.com/fengyuan404/git_test.git
cd git_test
cat fruits.txt
```

## 📁 项目结构

```
.
├── fruits.txt    # 水果清单（唯一数据源）
└── README.md     # 项目说明
```

## 🌿 分支策略

| 分支 | 用途 |
|------|------|
| `master` | 稳定版，生产级水果清单 |
| `develop` | 开发集成分支，新水果在此汇合 |
| `feature/*` | 单个水果的特性分支，如 `feature/strawberry`、`feature/mango` |

## 🤝 参与贡献

想加一种水果？按以下步骤来：

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/你的水果`
3. 在 `fruits.txt` 中添加你的水果（建议按字母顺序）
4. 提交并发起 Pull Request

所有贡献均经过合并审查，冲突协作解决。

## 📄 开源协议

MIT © 2025
