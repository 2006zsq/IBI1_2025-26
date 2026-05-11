# =============================================================================
# Practical 9 Task 3
# 1. Create 100x100 grid (0=susceptible,1=infected,2=recovered).
# 2. Randomly place one initial infected cell.
# 3. For each time step:
#    - Find all infected cells.
#    - Infect 8 neighbors with probability beta.
#    - Recover infected cells with probability gamma.
# 4. Plot grid at several time points to show spread.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

# Grid size
size = 100
beta = 0.3
gamma = 0.05
time_steps = 100

# Initialize all susceptible (0)
grid = np.zeros((size, size), dtype=int)

# Random initial infection
outbreak = np.random.choice(size, 2)
grid[outbreak[0], outbreak[1]] = 1

# Directions: 8 neighbors
directions = [(-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0), (1,1)]

# Plot at these time points
plot_times = {0, 10, 20, 50, 100}

for t in range(time_steps + 1):
    if t in plot_times:
        plt.figure(figsize=(5,5))
        plt.imshow(grid, cmap='viridis', interpolation='nearest')
        plt.title(f'Spatial SIR at time {t}')
        plt.colorbar(label='0=S,1=I,2=R')
        plt.show()

    # Copy grid to avoid overwriting during update
    new_grid = grid.copy()
    infected = np.argwhere(grid == 1)

    # Spread to neighbors
    for (i, j) in infected:
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            if 0 <= ni < size and 0 <= nj < size:
                if new_grid[ni, nj] == 0:
                    if np.random.rand() < beta:
                        new_grid[ni, nj] = 1

    # Recovery
    for (i, j) in infected:
        if np.random.rand() < gamma:
            new_grid[i, j] = 2

    grid = new_grid

print("Spatial SIR simulation completed.")