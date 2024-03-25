#backtrader示例

import backtrader as bt

# 定义策略
class SmaCross(bt.Strategy):
    # 定义参数
    params = dict(
        pfast=5,  # 短期均线周期
        pslow=10  # 长期均线周期
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # 短期均线
        sma2 = bt.ind.SMA(period=self.p.pslow)  # 长期均线
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # 均线交叉信号

    def next(self):
        if not self.position:  # 还没有仓位
            if self.crossover > 0:  # 金叉
                self.buy()  # 买入
        elif self.crossover < 0:  # 死叉
            self.close()  # 卖出

# 创建Cerebro回测引擎
cerebro = bt.Cerebro()

# 读取数据
data = bt.feeds.GenericCSVData(dataname='stock.csv', dtformat='%Y-%m-%d', datetime=0, open=1, high=2, low=3, close=4, volume=5)

# 加载数据
cerebro.adddata(data)

# 添加策略
cerebro.addstrategy(SmaCross)

# 设置初始资金
cerebro.broker.setcash(10000.0)

# 设置佣金
cerebro.broker.setcommission(commission=0.001)

# 运行回测
cerebro.run()

# 绘图
cerebro.plot()