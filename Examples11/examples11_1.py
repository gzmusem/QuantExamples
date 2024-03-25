#数据存储示例

import yfinance as yf
import pandas as pd

# 设置股票代码和日期范围
symbol = "AAPL"
start_date = "2020-01-01"
end_date = "2023-12-31"

# 从Yahoo Finance获取数据
data = yf.download(symbol, start=start_date, end=end_date)

# 保存数据到CSV文件
data.to_csv("stock.csv")

# 打印数据的前几行
print(data.head())