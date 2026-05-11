# =============================================================================
# Practical 9 Task 2
# 1. Define a range of vaccination rates from 0% to 100%.
# 2. For each vaccination rate:
#    a. Calculate the number of vaccinated (immune) individuals.
#    b. Initialize susceptible (S), infected (I), and recovered (R) populations.
#    c. Run a stochastic SIR simulation for a fixed number of time steps.
#    d. Record the number of infected individuals at each step.
# 3. Plot the infection curves for all vaccination rates on the same graph.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Simulation parameters
N = 10000               # Total population size
beta = 0.3              # Infection rate
gamma = 0.05            # Recovery rate
time_steps = 1000       # Number of time steps to simulate

# Vaccination rates to test (0%, 10%, ..., 100%)
vaccination_rates = np.arange(0, 1.1, 0.1)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

plt.figure(figsize=(6, 4), dpi=150)

for idx, v_rate in enumerate(vaccination_rates):
    # Calculate number of vaccinated individuals
    vaccinated = int(N * v_rate)
    remaining_population = N - vaccinated

    # Initialize S, I, R populations safely (no negative values)
    if remaining_population >= 1:
        # Start with 1 infected individual, rest susceptible
        S = remaining_population - 1
        I = 1
    else:
        # If everyone is vaccinated, there are no susceptible or infected people
        S = 0
        I = 0
    R = vaccinated

    # List to store infected counts over time
    infected_curve = [I]

    for t in range(time_steps):
        # Only calculate new infections if there are susceptible and infected individuals
        if I > 0 and S > 0:
            infection_probability = beta * (I / N)
            new_infections = np.random.binomial(S, infection_probability)
        else:
            new_infections = 0

        # Only calculate recoveries if there are infected individuals
        if I > 0:
            new_recoveries = np.random.binomial(I, gamma)
        else:
            new_recoveries = 0

        # Update population counts (ensure no negative values)
        S = max(S - new_infections, 0)
        I = max(I + new_infections - new_recoveries, 0)
        R = max(R + new_recoveries, 0)

        # Record the current number of infected individuals
        infected_curve.append(I)

    # Plot the infection curve for this vaccination rate
    plt.plot(infected_curve, color=colors[idx], label=f'{int(v_rate * 100)}%')

# Add plot labels and formatting
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Individuals')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend(title='Vaccination Rate', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot to a file
plt.savefig('SIR_vaccination.png', bbox_inches='tight')
plt.close()

print("✅ Simulation completed successfully. Plot saved as 'SIR_vaccination.png'.")