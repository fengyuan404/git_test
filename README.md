# 🍉 Fruit Catalog

> A collaboratively curated fruit inventory — powered by Git, grown with love.

[![Git](https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white)](https://git-scm.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 Overview

**Fruit Catalog** is a lightweight, version-controlled collection of fruits. It serves as a hands-on demonstration of Git branching, merging, conflict resolution, and collaborative workflows — all wrapped in a deliciously simple dataset.

Every fruit in the catalog represents a commit, every branch a seasonal harvest.

## 🌳 Current Inventory

| # | Fruit | # | Fruit | # | Fruit |
|:-:|-------|:-:|-------|:-:|-------|
| 1 | 🍌 香蕉 (Banana) | 4 | 🍎 苹果 (Apple) | 7 | 🍊 橘子 (Tangerine) |
| 2 | 🍓 草莓 (Strawberry) | 5 | 🍉 西瓜 (Watermelon) | 8 | 🍇 葡萄 (Grape) |
| 3 | 🥭 芒果 (Mango) | 6 | 🫐 杨梅 (Bayberry) | 9 | 🫐 蓝莓 (Blueberry) |

## 🚀 Quick Start

```bash
git clone https://github.com/fengyuan404/git_test.git
cd git_test
cat fruits.txt
```

## 📁 Project Structure

```
.
├── fruits.txt    # The canonical fruit inventory
└── README.md     # You are here
```

## 🌿 Branch Strategy

| Branch | Purpose |
|--------|---------|
| `master` | Stable, production-ready fruit list |
| `develop` | Integration branch for new fruits |
| `feature/*` | Individual fruit proposals (e.g. `feature/strawberry`, `feature/mango`) |

## 🤝 Contributing

Want to add a fruit? Here''s how:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-fruit`
3. Add your fruit to `fruits.txt` (alphabetical order preferred)
4. Commit and open a Pull Request

All contributions go through merge review — conflicts are resolved collaboratively.

## 📄 License

MIT © 2025
