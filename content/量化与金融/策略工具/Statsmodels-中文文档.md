---
title: Statsmodels 中文文档
url: https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source
fetch_source: agent_reach:gh
fetched_at: '2026-06-27T19:17:47+00:00'
polished_at: '2026-06-27T19:53:10+00:00'
github_readme_repaired_at: '2026-06-27T20:19:08+00:00'
wikilinks_unbulleted_at: '2026-06-28T05:48:29+00:00'
custom-width: 85
---

# Statsmodels 中文文档

**Repository:** https://github.com/TianFengshou/statsmodels-docs-zh

**在线文档入口：** https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source

## README

关于统计模型
=================

statsmodels是一个Python软件包，为scipy提供了补充，以进行统计计算，包括描述性统计以及统计模型的估计和推断。

statsmodels主要包括如下子模块：

回归模型：线性回归，广义线性模型，稳健的线性模型，线性混合效应模型等等。方差分析（ANOVA）。时间序列分析：AR，ARMA，ARIMA，VAR和其它模型。非参数方法： 核密度估计，核回归。统计模型结果可视化。比较：statsmodels更关注统计推断，提供不确定估计和参数p-value. 相反的，scikit-learn注重预测。主要特点
=============

* 线性回归模型：

  - 普通最小二乘法
  - 广义最小二乘法
  - 加权最小二乘法
  - 具有自回归误差的最小二乘
  - 分位数回归
  - 递归最小二乘法

* 具有混合效应和方差成分的混合线性模型
* GLM：支持所有单参数指数族分布的广义线性模型
* 用于二项式和泊松的贝叶斯混合GLM
* GEE：单向聚类或纵向数据的广义估计方程
* 离散模型:

  - Logit 和 Probit
  - 多项 logit (MNLogit)
  - 泊松和广义泊松回归
  - 负二项式回归
  - 零膨胀计数模型

* RLM: 鲁棒的线性模型，支持多个 M 估计器。
* 时间序列分析：时间序列分析模型

  - 完整的StateSpace建模框架

    - 季节性ARIMA和ARIMAX模型
    - VARMA和VARMAX模型
    - 动态因子模型
    - 未观测到的组件模型

  - 马尔可夫切换模型（MSAR），也称为隐马尔可夫模型（HMM）
  - 单变量时间序列分析：AR，ARIMA
  - 矢量自回归模型，VAR和结构VAR
  - 矢量误差修正模型，VECM
  - 指数平滑，Holt-Winters
  - 时间序列的假设检验：单位根，协整和其他
  - 用于时间序列分析的描述性统计数据和过程模型

* 生存分析:

  - 比例风险回归（Cox模型）
  - 生存者函数估计（Kaplan-Meier）
  - 累积发生率函数估计

* 多变量:

  - 缺失数据的主成分分析
  - 旋转因子分析
  - MANOVA
  - 典型相关

* 非参数统计：单变量和多变量核密度估计
* 数据集：用于示例和测试的数据集
* 统计：广泛的统计检验

  - 诊断和规格检验
  - 拟合优度和正态性检验
  - 多元测试函数
  - 各种其他统计检验

* 使用MICE进行插补，秩序统计回归和高斯插补
* 调解分析
* 图形包括用于数据和模型结果的可视化分析的绘图功能

* 输入/输出

  - 用于读取Stata .dta文件的工具，但pandas具有较新的版本
  -  表输出到ascii，latex和html

* 其他模型

* Sandbox：statsmodels包含一个 sandbox 文件夹，其中包含处于开发和测试各个阶段的代码，

  因此不被视为“生产就绪”。其中包括：

  - 广义矩法（GMM）估计器
  - 核回归
  - scipy.stats.distributions的各种扩展
  - 面板数据模型
  - 信息理论测度

如何获得
=============
GitHub上的master分支是最新的代码

https://www.github.com/statsmodels/statsmodels

发行标签的源代码下载可在GitHub上获得

https://github.com/statsmodels/statsmodels/tags

二进制文件和源代码发行版可从PyPi获得

https://pypi.org/project/statsmodels/

二进制文件可以安装在Anaconda中

conda install statsmodels

## 文档目录（docs/source）

- [_static](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/_static)
- [_templates](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/_templates)
- [about.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/about.rst)
- [anova.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/anova.rst)
- [api.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/api.rst)
- [conf.py](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/conf.py)
- [contingency_tables.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/contingency_tables.rst)
- [contrasts.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/contrasts.rst)
- [datasets](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/datasets)
- [dev](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/dev)
- [diagnostic.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/diagnostic.rst)
- [discretemod.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/discretemod.rst)
- [distributions.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/distributions.rst)
- [duration.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/duration.rst)
- [emplike.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/emplike.rst)
- [endog_exog.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/endog_exog.rst)
- [example_formulas.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/example_formulas.rst)
- [examples](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/examples)
- [extending.rst.TXT](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/extending.rst.TXT)
- [faq.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/faq.rst)
- [gam.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/gam.rst)
- [gee.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/gee.rst)
- [gettingstarted.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/gettingstarted.rst)
- [glm.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/glm.rst)
- [glm_techn1.rst.TXT](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/glm_techn1.rst.TXT)
- [glm_techn2.rst.TXT](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/glm_techn2.rst.TXT)
- [gmm.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/gmm.rst)
- [gmm_techn1.rst.TXT](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/gmm_techn1.rst.TXT)
- [graphics.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/graphics.rst)
- [images](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/images)
- [imputation.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/imputation.rst)
- [index.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/index.rst)
- [install.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/install.rst)
- [iolib.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/iolib.rst)
- [large_data.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/large_data.rst)
- [miscmodels.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/miscmodels.rst)
- [missing.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/missing.rst)
- [mixed_glm.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/mixed_glm.rst)
- [mixed_linear.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/mixed_linear.rst)
- [multivariate.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/multivariate.rst)
- [names_wordlist.txt](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/names_wordlist.txt)
- [nonparametric.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/nonparametric.rst)
- [optimization.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/optimization.rst)
- [pitfalls.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/pitfalls.rst)
- [plots](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/plots)
- [regression.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/regression.rst)
- [regression_techn1.rst.TXT](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/regression_techn1.rst.TXT)
- [release](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/release)
- [rlm.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/rlm.rst)
- [rlm_techn1.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/rlm_techn1.rst)
- [sandbox.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/sandbox.rst)
- [spelling_wordlist.txt](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/spelling_wordlist.txt)
- [statespace.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/statespace.rst)
- [stats.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/stats.rst)
- [tools.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/tools.rst)
- [tsa.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/tsa.rst)
- [tsastats.rst.TXT](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/tsastats.rst.TXT)
- [user-guide.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/user-guide.rst)
- [vector_ar.rst](https://github.com/TianFengshou/statsmodels-docs-zh/tree/master/docs/source/vector_ar.rst)
## 相关笔记

[[MOC-quant-finance|量化与金融（主题索引）]]
[[LayerNorm-与-BatchNorm|LayerNorm 与 BatchNorm]]
[[Python-时序预测四类模型|Python 时序预测四类模型]]
[[Quant-Wiki-量化百科|Quant Wiki 量化百科]]
[[Quantreo-量化交易博客|Quantreo 量化交易博客]]
[[QuantsPlaybook-金工研报复现|QuantsPlaybook 金工研报复现]]
[[mplfinance-金融-K-线可视化|mplfinance 金融 K 线可视化]]