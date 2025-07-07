import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated data to mimic historical returns (since yfinance is not available)
np.random.seed(42)
dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='B')  # Business days
stocks = ['AAPL', 'MSFT', 'TSLA']
returns = pd.DataFrame(np.random.normal(0, 0.02, (len(dates), len(stocks))), index=dates, columns=stocks)

# Step 1: Calculate daily returns (already simulated here)
# returns = data.pct_change().dropna()  # If using real price data

# Step 2: Calculate VaR and CVaR at 95% confidence level
confidence_level = 0.95
alpha = 1 - confidence_level

# Historical VaR
historical_var = returns.quantile(alpha)

# Parametric VaR (Variance-Covariance)
mean_returns = returns.mean()
std_returns = returns.std()
z_score = np.percentile(np.random.randn(100000), alpha * 100)
parametric_var = mean_returns + std_returns * z_score

# Monte Carlo VaR
simulations = np.random.normal(mean_returns, std_returns, (1000, len(returns.columns)))
simulated_returns = pd.DataFrame(simulations, columns=returns.columns)
montecarlo_var = simulated_returns.quantile(alpha)

# Historical CVaR (Expected Shortfall)
historical_cvar = returns[returns.lt(historical_var)].mean()

# Step 3: Stress Test - assume a 20% market crash and assess impact on portfolio
stress_factor = -0.20
portfolio_weights = [0.4, 0.3, 0.3]  # Portfolio weights for AAPL, MSFT, TSLA
stressed_returns = pd.Series(stress_factor, index=returns.columns)
portfolio_stress_loss = np.dot(stressed_returns, portfolio_weights)

# Step 4: Apply Risk Limits and check which stocks exceed limits
risk_limits = {'AAPL': -0.04, 'MSFT': -0.03, 'TSLA': -0.06}
alerts = {}
for stock in returns.columns:
    if historical_var[stock] < risk_limits[stock]:
        alerts[stock] = '⚠️ Limit Exceeded'
    else:
        alerts[stock] = '✅ OK'

# Step 5: Simple Hedging simulation - Assume buying a put option on TSLA
put_cost = 0.02  # Simulated cost of put option
hedged_loss_tsla = historical_var['TSLA'] + put_cost

# Visualization - Plot distribution with Historical VaR for AAPL
plt.figure(figsize=(10, 6))
sns.histplot(returns['AAPL'], bins=50, kde=True)
plt.axvline(historical_var['AAPL'], color='r', linestyle='--', label='Historical VaR')
plt.title('AAPL Return Distribution with Historical VaR')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()

from tabulate import tabulate

# Align all series to the same index before creating the DataFrame
summary = pd.DataFrame({
    'Historical VaR': historical_var,
    'Parametric VaR': parametric_var,
    'Monte Carlo VaR': montecarlo_var,
    'CVaR': historical_cvar,
    'Risk Alert': pd.Series(alerts, index=historical_var.index)
})

# Print nicely formatted table
print(tabulate(summary, headers='keys', tablefmt='psql'))


