#NumPy示例

import numpy as np

# 股票收益率数据
returns = np.array([0.02, 0.03, -0.01, 0.05, 0.02, -0.03, 0.04, 0.01, 0.03, -0.02])

# 计算平均收益率
mean_return = np.mean(returns)
print("平均收益率:", mean_return)

# 计算收益率的标准差(风险)
std_dev = np.std(returns)
print("收益率标准差:", std_dev)

# 股票数量
num_stocks = len(returns)

# 随机生成初始权重
weights = np.random.random(num_stocks)
weights /= np.sum(weights)
print("初始权重:", weights)

# 计算组合收益率
portfolio_return = np.dot(weights, returns)
print("组合收益率:", portfolio_return)

# 计算组合风险
portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(np.cov(returns), weights)))
print("组合风险:", portfolio_risk)

# 优化权重
def optimize_portfolio(returns, iterations=1000):
    num_stocks = len(returns)
    best_weights = None
    best_sharpe_ratio = float('-inf')
    
    for _ in range(iterations):
        weights = np.random.random(num_stocks)
        weights /= np.sum(weights)
        
        portfolio_return = np.dot(weights, returns)
        portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(np.cov(returns), weights)))
        
        sharpe_ratio = portfolio_return / portfolio_risk
        
        if sharpe_ratio > best_sharpe_ratio:
            best_sharpe_ratio = sharpe_ratio
            best_weights = weights
    
    return best_weights, best_sharpe_ratio

# 优化组合权重
optimized_weights, best_sharpe_ratio = optimize_portfolio(returns)
print("优化后的权重:", optimized_weights)
print("最优夏普比率:", best_sharpe_ratio)