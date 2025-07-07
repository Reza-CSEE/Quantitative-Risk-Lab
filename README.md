# Quantitative-Risk-Lab
# Re-run code to regenerate the README file after reset

readme_content = """
# 📊 Market Risk Analysis and Management using VaR, CVaR & Monte Carlo Simulation

## 🔍 Overview

This project presents a complete, real-world quantitative risk framework to assess and manage **market risk** using statistical models.  
It evaluates the risk profile of equity portfolios (e.g., AAPL, MSFT, TSLA) with three methods of Value at Risk (**VaR**) — Historical, Parametric, and Monte Carlo — and also computes **Conditional VaR (CVaR)**, runs **Stress Tests**, checks **Risk Limits**, and models basic **Hedging with Options**.

---

## 📌 Key Features

- Compute Historical, Parametric, and Monte Carlo VaR
- Estimate Conditional Value at Risk (CVaR)
- Stress Test portfolios under crisis scenarios (e.g., -20% market crash)
- Evaluate risk thresholds with alerts
- Simulate simple hedging strategies using Put Options
- Generate insightful visualizations for daily returns and simulated distributions

---

## 📚 Concepts Covered

- Value at Risk (VaR)
- Conditional VaR (CVaR) / Expected Shortfall
- Monte Carlo Simulations
- Normal Distribution Modeling
- Portfolio Stress Testing
- Risk Limits and Alerts
- Option-Based Hedging

---

## 🛠️ Technologies Used

- Python
- NumPy, Pandas
- Matplotlib, Seaborn
- Tabulate (for CLI-friendly tables)

---

## 🧪 Sample Output

- 📈 AAPL daily return histogram with Historical VaR & CVaR lines
- 🎲 Simulated return distributions via Monte Carlo
- 📉 Comparison chart across VaR calculation methods
- ⚠️ Risk Alert system detecting limit breaches

---

## ✍️ Author

**Reza Ghasemi**  
Quantitative Analyst | Risk Modeler | Python Developer  
[LinkedIn or Website (optional)]

---

## 💡 Note

This project is for educational and research purposes. Always validate models before using them in production trading systems.

"""

# Save the README content to a file
readme_path = "/mnt/data/README.md"
with open(readme_path, "w") as f:
    f.write(readme_content)

readme_path
