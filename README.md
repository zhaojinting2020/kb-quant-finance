# 量化学习笔记

个人量化金融学习路径与读书笔记（Obsidian vault + [Quartz](https://quartz.jzhao.xyz) 站点）。

在线阅读：https://zhaojinting2020.github.io/kb-quant-finance/

适合想从「金融基础 → 数学 → Python → 回测实战」串起来的自学者。内容以 Markdown 为主，附件走 Git LFS。

> 这是学习笔记，不是投资建议。策略示例仅用于理解方法，不构成实盘推荐。

## 快速开始

```bash
git lfs install
git clone https://github.com/zhaojinting2020/kb-quant-finance.git
cd kb-quant-finance
```

用 Obsidian 打开 `content/` 作为 vault，从 [`content/index.md`](content/index.md) 进入。

本地预览站点：

```bash
npm ci
npx quartz build --serve
```

## 学习路径（建议顺序）

入口总览：[`量化交易之路`](content/量化与金融/读书笔记/00-路径/量化交易之路-Qod0dMaR.md)

1. 金融基础：术语、财报、投资学、计量、衍生品
2. 数学基础：概率统计、线性代数、微积分、时序
3. 编程与实战：Python 数据分析、算法交易、回测
4. 面试：Quant interview 题集

## 目录

| 路径 | 内容 |
|------|------|
| [`content/量化与金融/读书笔记/00-路径/`](content/量化与金融/读书笔记/00-路径/) | 学习路线 |
| [`content/量化与金融/读书笔记/10-金融基础/`](content/量化与金融/读书笔记/10-金融基础/) | 金融基础笔记 |
| [`content/量化与金融/读书笔记/20-数学基础/`](content/量化与金融/读书笔记/20-数学基础/) | 数学基础笔记 |
| [`content/量化与金融/读书笔记/30-编程与实战/`](content/量化与金融/读书笔记/30-编程与实战/) | 编程与实战笔记 |
| [`content/量化与金融/读书笔记/40-面试/`](content/量化与金融/读书笔记/40-面试/) | 面试笔记 |
| [`content/量化与金融/策略工具/`](content/量化与金融/策略工具/) | 工具、库、博客摘记 |
| [`content/量化与金融/数据源/`](content/量化与金融/数据源/) | 数据入口 |
| [`content/00-导航/MOC-quant-finance.md`](content/00-导航/MOC-quant-finance.md) | 主题导航（含外链） |
| [`content/attachments/`](content/attachments/) | PDF / 图片 / notebook（Git LFS） |

## 可直接打开的几篇

- [量化交易之路](content/量化与金融/读书笔记/00-路径/量化交易之路-Qod0dMaR.md)（路径总览）
- [清华大学《量化交易》学习笔记](content/量化与金融/读书笔记/10-金融基础/学习笔记%20-%20清华大学《量化交易》-%20QWvgdchv.md)
- [《Python 算法交易》学习笔记](content/量化与金融/读书笔记/30-编程与实战/学习笔记%20-%20《Python-算法交易》-Cpv4djLF.md)
- [量化必备：100 个金融术语](content/量化与金融/读书笔记/10-金融基础/量化必备100个金融术语-VfHgd6ls.md)
- [a practical guide to quantitative finance interviews](content/量化与金融/读书笔记/40-面试/a-practical-guide-to-quantitative-finance-interviews.md)

## 设计取舍（向这些公开专栏学的）

| 仓库 | 可借鉴点 | 本仓怎么落地 |
|------|----------|--------------|
| [rzeng0812/quant-atlas](https://github.com/rzeng0812/quant-atlas) | 编号主题树 + MOC + Quartz | 读书笔记已按 00/10/20/30/40 编号；Quartz Pages 已接入 |
| [ebrahimpichka/open-MFE](https://github.com/ebrahimpichka/open-MFE) | 按 MFE 课表模块化 | 学习路径按「基础 → 数学 → 编程 → 面试」排 |
| [warwickquant/KnowledgeBase](https://github.com/warwickquant/KnowledgeBase) | textbooks / tutorials / careers | 对应读书笔记 / 策略工具 / 数据源 |
| [sw-yx/brain](https://github.com/sw-yx/brain) | 公开 digital garden | 以可跟读笔记为主 |
| [jeremyrayner/kb-template](https://github.com/jeremyrayner/kb-template) | raw → wiki | 笔记为编译后的 wiki；附件当 raw |

## 协作与许可

- Issues / PR 欢迎纠错、补链接、修断链
- 笔记版权归原作者与整理者；引用请标明出处
- 大文件需 [Git LFS](https://git-lfs.com/)；克隆前执行 `git lfs install`

## 相关仓库

| 仓库 | 说明 |
|------|------|
| [kb-deep-learning-ai](https://github.com/zhaojinting2020/kb-deep-learning-ai) | 深度学习与 AI 笔记 |
| [kb-robotics](https://github.com/zhaojinting2020/kb-robotics) | 机器人与自动驾驶笔记 |
