# =============================================================================
# Practical 9 Task 1
#
# 1. Initialize total population, S, I, R with given values.
# 2. Set infection rate beta and recovery rate gamma.
# 3. Use lists to track S, I, R over time.
# 4. Simulate 1000 time steps:
#    - Infect susceptible individuals probabilistically.
#    - Recover infected individuals with fixed probability.
# 5. Update S, I, R each step and store values.
# 6. Plot S, I, R against time with labels and legend.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# Total population
N = 10000

# Initial conditions
S = N - 1
I = 1
R = 0

# Parameters
beta = 0.3
gamma = 0.05

# Track time series
S_list = [S]
I_list = [I]
R_list = [R]

# Simulate 1000 time steps
for t in range(1000):
    # Infection probability depends on infected proportion
    infection_prob = beta * (I / N)

    # Stochastic infection
    new_infected = np.random.binomial(S, infection_prob)
    # Stochastic recovery
    new_recovered = np.random.binomial(I, gamma)

    # Update states
    S -= new_infected
    I += new_infected - new_recovered
    R += new_recovered

    # Ensure non-negative
    S = max(S, 0)
    I = max(I, 0)
    R = max(R, 0)

    # Record
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('SIR_plot.png', bbox_inches='tight')
plt.close()

print("SIR simulation done. Plot saved as SIR_plot.png")