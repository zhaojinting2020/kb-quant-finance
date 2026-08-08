# 量化学习笔记

个人量化金融学习路径与读书笔记（Obsidian vault）。

| 用途 | 链接 |
|------|------|
| 源码仓库 | https://github.com/zhaojinting2020/kb-quant-finance |
| 飞书路径原稿 | https://my.feishu.cn/docx/Qod0dMaRSoht42xl4jMcUV6jnqg |

适合想从「金融基础 → 数学 → Python → 回测实战」串起来的自学者。内容以 Markdown 为主，附件走 Git LFS。

> 这是学习笔记，不是投资建议。策略示例仅用于理解方法，不构成实盘推荐。

## 写作与同步（飞书为主）

1. 在飞书写 / 改（正文真相源）
2. Cursor 打开本仓，拉取对应飞书文档到 `content/`
3. Obsidian 打开 `content/`：修 wikilink、核对编号目录与附件
4. `git push` 到 GitHub

分享协作改大纲用飞书；需要版本与附件时用本仓库。

## 快速开始

```bash
git lfs install
git clone https://github.com/zhaojinting2020/kb-quant-finance.git
cd kb-quant-finance
```

用 Obsidian 打开 `content/` 作为 vault，从 [`content/index.md`](content/index.md) 进入。

## 学习路径（建议顺序）

入口总览：[`量化交易之路`](content/量化与金融/读书笔记/00-路径/量化交易之路-Qod0dMaR.md)

1. 金融基础：术语、财报、投资学、计量、衍生品
2. 数学基础：概率统计、线性代数、微积分、时序
3. 编程与实战：Python 数据分析、算法交易、回测
4. 面试：Quant interview 题集

## 目录

| 路径 | 内容 |
|------|------|
| [`00-路径`](content/量化与金融/读书笔记/00-路径/) | 学习路线 |
| [`10-金融基础`](content/量化与金融/读书笔记/10-金融基础/) | 金融基础笔记 |
| [`20-数学基础`](content/量化与金融/读书笔记/20-数学基础/) | 数学基础笔记 |
| [`30-编程与实战`](content/量化与金融/读书笔记/30-编程与实战/) | 编程与实战笔记 |
| [`40-面试`](content/量化与金融/读书笔记/40-面试/) | 面试笔记 |
| [`策略工具`](content/量化与金融/策略工具/) | 工具、库、博客摘记 |
| [`数据源`](content/量化与金融/数据源/) | 数据入口 |
| [`attachments`](content/attachments/) | PDF / 图片 / notebook（Git LFS） |

## 相关仓库

| 仓库 | 说明 |
|------|------|
| [kb-deep-learning-ai](https://github.com/zhaojinting2020/kb-deep-learning-ai) | 深度学习与 AI 笔记 |
| [kb-robotics](https://github.com/zhaojinting2020/kb-robotics) | 机器人与自动驾驶笔记 |
