---
title: LayerNorm 与 BatchNorm
url: https://blog.csdn.net/FrankieHello/article/details/122656652
curated_at: '2026-06-28T20:00:00+00:00'
custom-width: 85
---

# LayerNorm 与 BatchNorm

## 使用 Normalization 的目的

梯度下降优化时，网络加深会导致各层输入特征分布持续变化。加入 Normalization 可以**稳定特征分布**，从而：

- 使用更大的学习率，加速收敛
- 一定程度缓解过拟合，训练更平稳

具体地，Normalization 在特征进入激活函数之前将其变换为**均值 0, 方差 1**，避免大量激活落在饱和区，减轻梯度消失。

## LayerNorm 与 BatchNorm

BN（BatchNorm）和 LN（LayerNorm）都将输入归一化为均值 0, 方差 1，一般形式为：

\[
y = \frac{x - E(x)}{\sqrt{\mathrm{Var}(x) + \epsilon}} \cdot \gamma + \beta
\]

其中 \(\gamma\), \(\beta\) 为可学习缩放与平移参数。

### 归一化维度

以二维矩阵为例：行 = `batch_size`，列 = 特征数 `fea_nums`。

| 方法 | 归一化方向 | 效果 |
|------|-----------|------|
| **BatchNorm** | 沿 batch 维（竖着） | 抹平**不同特征**间的大小关系，保留**不同样本**间的大小关系 |
| **LayerNorm** | 沿特征维（横着） | 抹平**不同样本**间的大小关系，保留**不同特征**间的大小关系 |

### 适用场景

- **BN**：任务依赖样本间关系时更有效，典型如 **CV**（不同图片样本分类，样本间关系得以保留）。
- **LN**：更适合 **NLP** 等序列任务；单个样本的特征对应各 token 的 embedding，LN 能保留特征间的时序/结构关系。推理阶段不依赖 batch 统计，也与变长序列更契合。

## 相关笔记

[[MOC-quant-finance|量化与金融（主题索引）]]
[[Python-时序预测四类模型|Python 时序预测四类模型]]
[[Quant-Wiki-量化百科|Quant Wiki 量化百科]]
[[Quantreo-量化交易博客|Quantreo 量化交易博客]]
[[QuantsPlaybook-金工研报复现|QuantsPlaybook 金工研报复现]]
[[Statsmodels-中文文档|Statsmodels 中文文档]]
[[mplfinance-金融-K-线可视化|mplfinance 金融 K 线可视化]]