# Define population data (2020 and 2024, unit: millions)
countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
pop_2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop_2024 = [69.2, 1410, 58.9, 212.0, 340.1]
pop_change = {}

import matplotlib.pyplot as plt

# Calculate percentage change in population
for i in range(len(countries)):
    pct = (pop_2024[i] - pop_2020[i]) / pop_2020[i] * 100
    pop_change[countries[i]] = round(pct, 3)

print("=== 3. Population Growth Rate Analysis ===")
print("Population percentage change (2020-2024):")
for country, pct in pop_change.items():
    print(f"{country}: {pct}%")

# Sort countries by population change rate in descending order
sorted_pop = sorted(pop_change.items(), key=lambda x: x[1], reverse=True)
print("\nCountries sorted by population change rate (descending):", sorted_pop)

# Find country with maximum growth and maximum decrease
max_growth = sorted_pop[0]
max_decrease = sorted_pop[-1]
print(f"Country with highest population growth: {max_growth[0]} ({max_growth[1]}%)")
print(f"Country with largest population decrease: {max_decrease[0]} ({max_decrease[1]}%)")

# Create bar chart for population percentage change
plt.figure(figsize=(9, 6))
sorted_countries = [x[0] for x in sorted_pop]
sorted_pcts = [x[1] for x in sorted_pop]

# Use green for positive growth, red for negative growth
colors = ['green' if p > 0 else 'red' for p in sorted_pcts]
plt.bar(sorted_countries, sorted_pcts, color=colors)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)  # Add zero baseline

# Add chart title and axis labels
plt.title('Population Percentage Change (2020-2024)', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)
plt.tight_layout()
plt.show()