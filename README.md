# 量化学习笔记

个人量化金融学习路径与读书笔记（Obsidian vault）。

适合想从「金融基础 → 数学 → Python → 回测实战」串起来的自学者。内容以 Markdown 为主，附件走 Git LFS。

> 这是学习笔记，不是投资建议。策略示例仅用于理解方法，不构成实盘推荐。

## 快速开始

```bash
git lfs install
git clone https://github.com/zhaojinting2020/kb-quant-finance.git
cd kb-quant-finance
```

用 Obsidian 打开仓库根目录作为 vault，从 [`Home.md`](Home.md) 进入。

## 学习路径（建议顺序）

入口总览：[`量化交易之路`](content/量化与金融/读书笔记/量化交易之路-Qod0dMaR.md)

1. 金融基础：术语、财报、投资学、计量、衍生品  
2. 数学基础：概率统计、线性代数、微积分  
3. 编程基础：Python 数据分析、金融时序、Python for Finance  
4. 量化实战：向量化回测、动量 / 均值回归、过拟合陷阱  
5. （进行中）机器学习预测市场

对应精读笔记多在 [`content/量化与金融/读书笔记/`](content/量化与金融/读书笔记/)。

## 目录

| 路径 | 内容 | 约篇数 |
|------|------|--------|
| [`content/量化与金融/读书笔记/`](content/量化与金融/读书笔记/) | 书 / 课程 / 面试题笔记 | 33 |
| [`content/量化与金融/策略工具/`](content/量化与金融/策略工具/) | 工具、库、博客摘记 | 8 |
| [`content/量化与金融/数据源/`](content/量化与金融/数据源/) | 数据入口与相关摘记 | 4 |
| [`index/MOC-quant-finance.md`](index/MOC-quant-finance.md) | 主题导航（含外链） | — |
| [`attachments/`](attachments/) | PDF / 图片 / notebook（Git LFS） | — |

## 可直接打开的几篇

- [量化交易之路](content/量化与金融/读书笔记/量化交易之路-Qod0dMaR.md)（路径总览）  
- [清华大学《量化交易》学习笔记](content/量化与金融/读书笔记/学习笔记%20-%20清华大学《量化交易》-%20QWvgdchv.md)  
- [《Python 算法交易》学习笔记](content/量化与金融/读书笔记/学习笔记%20-%20《Python-算法交易》-Cpv4djLF.md)  
- [量化必备：100 个金融术语](content/量化与金融/读书笔记/量化必备100个金融术语-VfHgd6ls.md)  
- [a practical guide to quantitative finance interviews](content/量化与金融/读书笔记/a-practical-guide-to-quantitative-finance-interviews.md)

## 设计取舍（向这些公开专栏学的）

| 仓库 | 可借鉴点 | 本仓怎么落地 |
|------|----------|--------------|
| [rzeng0812/quant-atlas](https://github.com/rzeng0812/quant-atlas) | 编号主题树 + MOC 入口 + Quartz 站点 | 先用 `Home` / MOC；站点可后加 |
| [ebrahimpichka/open-MFE](https://github.com/ebrahimpichka/open-MFE) | 按 MFE 课表模块化资源地图 | 学习路径按「基础 → 数学 → 编程 → 实战」排 |
| [warwickquant/KnowledgeBase](https://github.com/warwickquant/KnowledgeBase) | textbooks / tutorials / careers 分区 | 对应 `读书笔记` / `策略工具` / `数据源` |
| [sw-yx/brain](https://github.com/sw-yx/brain) | 公开 digital garden：原始笔记可看，精选另发 | 本仓以「可跟读笔记」为主，不包装成课程 |
| [jeremyrayner/kb-template](https://github.com/jeremyrayner/kb-template) | Karpathy LLM Wiki：raw → wiki | 笔记已是编译后的 wiki；附件当 raw |

暂不做的（可后续）：

- Quartz / Obsidian Publish 静态站  
- 面试刷题专区、代码作业仓库拆分  
- 英文双语目录

## 协作与许可

- Issues / PR 欢迎纠错、补链接、修断链  
- 笔记版权归原作者与整理者；引用请标明出处  
- 大文件需 [Git LFS](https://git-lfs.com/)；克隆前执行 `git lfs install`

## 相关仓库

| 仓库 | 说明 |
|------|------|
| [kb-deep-learning-ai](https://github.com/zhaojinting2020/kb-deep-learning-ai) | 深度学习与 AI 笔记 |
| [kb-robotics](https://github.com/zhaojinting2020/kb-robotics) | 机器人与自动驾驶笔记 |
