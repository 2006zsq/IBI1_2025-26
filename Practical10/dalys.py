# =============================================================================
# Practical 10
# 1. Set working directory and load the DALYs CSV dataset using pandas.
# 2. Explore dataframe structure: head, info, describe.
# 3. Use iloc to access rows and columns by index.
# 4. Use Boolean indexing with loc to filter country data (Zimbabwe).
# 5. Extract 2019 data to find countries with max and min DALYs.
# 6. Plot DALYs over time for a selected country.
# 7. Answer a self-defined question with analysis and plotting.
# =============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------
# 1. Set working directory
# ---------------------------
# Replace this path with your own folder path
os.chdir("C:/Users/邹思琪/Downloads/1.20/IBI1_2025-26/Practical10")

# Check current directory
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# ---------------------------
# 2. Load dataset
# ---------------------------
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show first 5 rows
print("\n=== First 5 rows ===")
print(dalys_data.head(5))

# Show dataframe info
print("\n=== Dataframe info ===")
dalys_data.info()

# Show summary statistics
print("\n=== Summary statistics ===")
print(dalys_data.describe())

# ---------------------------
# 3. Access with iloc
# ---------------------------
# Show third and fourth columns (Year, DALYs) for first 10 rows
first10 = dalys_data.iloc[0:10, [2, 3]]
print("\n=== First 10 rows: Year and DALYs ===")
print(first10)

# Find year with maximum DALYs in Afghanistan's first 10 entries
max_idx = first10["DALYs"].idxmax()
year_max_afg = first10.loc[max_idx, "Year"]
print(f"\nYear with max DALYs in first 10 Afghan records: {year_max_afg}")

# ---------------------------
# 4. Locate Zimbabwe data using Boolean index
# ---------------------------
zimbabwe = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print("\n=== Zimbabwe data ===")
print(zimbabwe)

# First and last year for Zimbabwe
first_zim = zimbabwe["Year"].min()
last_zim = zimbabwe["Year"].max()
print(f"\nZimbabwe DALYs recorded from {first_zim} to {last_zim}")

# ---------------------------
# 5. 2019 data: max and min DALYs countries
# ---------------------------
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

# Country with maximum DALYs in 2019
max_country = recent_data.loc[recent_data["DALYs"].idxmax(), "Entity"]
max_value = recent_data["DALYs"].max()

# Country with minimum DALYs in 2019
min_country = recent_data.loc[recent_data["DALYs"].idxmin(), "Entity"]
min_value = recent_data["DALYs"].min()

print(f"\n2019 Max DALYs: {max_country} ({max_value})")
print(f"2019 Min DALYs: {min_country} ({min_value})")

# ---------------------------
# 6. Plot DALYs over time for one country (e.g., lowest country)
# ---------------------------
country_data = dalys_data.loc[dalys_data["Entity"] == min_country]

plt.figure(figsize=(8, 4))
plt.plot(country_data["Year"], country_data["DALYs"], "bo-", linewidth=2, markersize=6)
plt.xlabel("Year")
plt.ylabel("DALYs rate")
plt.title(f"DALYs over time in {min_country} (2019 minimum)")
plt.xticks(rotation=-90)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("dalys_trend.png")
plt.close()

# ---------------------------
# 7. Self-defined question (line 90)
# Question: What is the DALYs trend distribution in China from 1990 to 2019?
# ---------------------------
china_data = dalys_data.loc[dalys_data["Entity"] == "China"]

plt.figure(figsize=(8, 4))
plt.boxplot(china_data["DALYs"], vert=False, widths=0.6)
plt.xlabel("DALYs rate")
plt.title("DALYs distribution in China (1990-2019)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("china_dalys_boxplot.png")
plt.close()

print("\nAll tasks completed. Plots saved as PNG files.")