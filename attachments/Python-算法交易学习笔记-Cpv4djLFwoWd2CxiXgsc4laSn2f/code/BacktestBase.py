#
# Python Script with Base Class
# for Event-Based Backtesting
#
# Python for Algorithmic Trading
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
import numpy as np
import pandas as pd
from pylab import mpl, plt

try:
    plt.style.use('seaborn')            # 旧版 Matplotlib
except OSError:
    plt.style.use('seaborn-v0_8')       # 新版 Matplotlib
mpl.rcParams['font.family'] = 'serif'

class BacktestBase(object):
    '''事件驱动回测的基类。'''

    def __init__(self, symbol, start, end, amount,
                 ftc=0.0, ptc=0.0, verbose=True):
        '''初始化回测状态，并自动调用 get_data()。'''
        self.symbol = symbol           # TR RIC（金融标的）
        self.start = start             # 数据起始日期
        self.end = end                 # 数据结束日期
        self.initial_amount = amount   # 初始资金（保持不变）
        self.amount = amount           # 当前现金余额（一次性或按笔投入）
        self.ftc = ftc                 # 每笔固定交易成本（买/卖）
        self.ptc = ptc                 # 每笔比例交易成本（买/卖）
        self.units = 0                 # 持有数量
        self.position = 0              # 仓位：0 为市场中性
        self.trades = 0                # 交易次数
        self.verbose = verbose         # True 时输出完整信息
        self.get_data()

    def get_data(self):
        '''从 CSV 读取指定区间的 EOD 数据，并计算对数收益率。'''
        raw = pd.read_csv('http://hilpisch.com/pyalgo_eikon_eod_data.csv',
                          index_col=0, parse_dates=True).dropna()
        raw = pd.DataFrame(raw[self.symbol])
        raw = raw.loc[self.start:self.end]
        raw.rename(columns={self.symbol: 'price'}, inplace=True)
        raw['return'] = np.log(raw / raw.shift(1))
        self.data = raw.dropna()

    def plot_data(self, cols=None):
        '''绘制标的收盘价。'''
        if cols is None:
            cols = ['price']
        self.data['price'].plot(figsize=(10, 4), title=self.symbol) # plot 标的收盘价序列 self.data['price']

    def get_date_price(self, bar):
        '''返回指定 K 线的日期和价格。'''
        date = str(self.data.index[bar])[:10]
        price = self.data.price.iloc[bar]
        return date, price

    def print_balance(self, bar):
        '''打印当前现金余额。'''
        date, price = self.get_date_price(bar=bar)
        print(f'{date} | current balance {self.amount:.2f}')

    def print_net_wealth(self, bar):
        '''打印当前净资产（现金 + 持仓市值）。'''
        date, price = self.get_date_price(bar=bar)
        net_wealth = self.units * price + self.amount
        print(f'{date} | current net wealth {net_wealth:.2f}')

    def place_buy_order(self, bar, units=None, amount=None):
        '''市价买入。units 未给定时按 amount / price 取整；扣 ptc 与 ftc，不检查资金是否充足, 基类只提供原始买卖动作。'''
        date, price = self.get_date_price(bar=bar)
        if units is None:
            units = int(amount / price)
        self.amount -= (units * price) * (1 + self.ptc) + self.ftc
        self.units += units
        self.trades += 1
        if self.verbose: # 为 True 时打印买卖明细、余额、净资产
            print(f'{date} | buying {units} units at {price:.2f}')
            self.print_balance(bar=bar)
            self.print_net_wealth(bar=bar)

    def place_sell_order(self, bar, units=None, amount=None):
        '''市价卖出。units 未给定时按 amount / price 取整；扣 ptc 与 ftc，不检查持仓是否充足, 基类只提供原始买卖动作。'''
        date, price = self.get_date_price(bar=bar)
        if units is None:
            units = int(amount / price)
        self.amount += (units * price) * (1 - self.ptc) - self.ftc
        self.units -= units
        self.trades += 1
        if self.verbose:
            print(f'{date} | selling {units} units at {price:.2f}')
            self.print_balance(bar=bar)
            self.print_net_wealth(bar=bar)

    def close_out(self, bar):
        '''期末按市价平仓（不计交易成本），并打印最终余额与净绩效。'''
        date, price = self.get_date_price(bar=bar)
        self.amount += self.units * price
        self.units = 0
        self.trades += 1
        if self.verbose:
            print(f'{date} | inventory {self.units} units at {price:.2f}')
            print('=' * 55)
        print('Final balance   [$] {:.2f}'.format(self.amount))
        perf = ((self.amount - self.initial_amount) / self.initial_amount * 100) # performence, 净收益率
        print('Net Performance [%] {:.2f}'.format(perf))
        print('Trades Executed [#] {:.2f}'.format(self.trades))
        print('=' * 55)
