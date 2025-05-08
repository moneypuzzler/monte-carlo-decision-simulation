import numpy as np
import matplotlib.pyplot as plt

# 📌 Monte Carlo Decision-Making Simulation
# Evaluating two strategic options under uncertainty using probabilistic modeling.

# 🔧 Parameters and Configuration
n_simulations = 10000  # Number of Monte Carlo simulations

# 🎲 Defining strategic options:
# Option A (Stable): Lower average return, lower risk
option_a_mean, option_a_std = 80, 10
option_a_results = np.random.normal(option_a_mean, option_a_std, n_simulations)

# Option B (Aggressive): Higher average return, higher risk
option_b_mean, option_b_std = 110, 40
option_b_results = np.random.normal(option_b_mean, option_b_std, n_simulations)

# 🔍 Probabilistic Comparison of Strategies
# Calculating the probability that Option B outperforms Option A
probability_b_better_than_a = np.mean(option_b_results > option_a_results)

# Calculating expected differences in returns between strategies
expected_return_difference = np.mean(option_b_results - option_a_results)

# Calculating risk (standard deviation of differences between returns)
risk_difference = np.std(option_b_results - option_a_results)

# ⚖️ Utility-Based Analysis (Log-Utility for Risk Aversion)
# To represent decision-maker's risk aversion using logarithmic utility function
# Clip results to avoid log(0) or log(negative) if results can be non-positive
option_a_results_clipped = np.clip(option_a_results, 1e-9, None) # Clipping at a very small positive number
option_b_results_clipped = np.clip(option_b_results, 1e-9, None) # Clipping at a very small positive number

utility_option_a = np.mean(np.log(option_a_results_clipped))
utility_option_b = np.mean(np.log(option_b_results_clipped))
utility_difference = utility_option_b - utility_option_a

# 📈 Visualization of Simulation Results
plt.figure(figsize=(12, 6))
plt.hist(option_a_results, bins=50, alpha=0.7, label="Option A (Stable)", color='skyblue', edgecolor='black')
plt.hist(option_b_results, bins=50, alpha=0.7, label="Option B (Aggressive)", color='orange', edgecolor='black')

# Plotting mean lines for both options
plt.axvline(np.mean(option_a_results), color='blue', linestyle='dashed', linewidth=2, label=f"Mean of Option A: {np.mean(option_a_results):.2f}")
plt.axvline(np.mean(option_b_results), color='red', linestyle='dashed', linewidth=2, label=f"Mean of Option B: {np.mean(option_b_results):.2f}")

plt.title("Monte Carlo Simulation for Decision-Making under Uncertainty", fontsize=14)
plt.xlabel("Simulated Outcomes (e.g., Profit, ROI)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
# plt.show() # Commented out to prevent blocking in non-interactive environments; save instead
plt.savefig("/home/ubuntu/monte_carlo_simulation_plot.png")
print("Plot saved to /home/ubuntu/monte_carlo_simulation_plot.png")

# 📝 Detailed Summary of Simulation Results
print("\n===== Monte Carlo Decision Simulation Detailed Summary =====\n")
print(f"Number of simulations conducted: {n_simulations:,}\n")

print("Strategic Option Comparison:")
print(f" - Probability Option B outperforms Option A: {probability_b_better_than_a*100:.2f}%")
print(f" - Expected Return Difference (Option B - Option A): {expected_return_difference:.2f}")
print(f" - Risk Difference (Std Dev of Return Differences): {risk_difference:.2f}\n")

print("Utility Analysis (Considering Risk Aversion):")
print(f" - Log-Utility of Option A (Stable): {utility_option_a:.4f}")
print(f" - Log-Utility of Option B (Aggressive): {utility_option_b:.4f}")
print(f" - Utility Advantage (Option B - Option A): {utility_difference:.4f}\n")

print("=============================================================")

# Example of how to run and what to expect:
# This script will print a summary of the simulation and save a plot.
# The plot visualizes the distribution of outcomes for Option A and Option B.
# The summary provides key metrics like the probability of one option outperforming the other,
# expected return differences, risk differences, and utility-based comparisons.
