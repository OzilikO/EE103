import matplotlib.pyplot as plt

# Data
current = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
force = [0.0000, 0.00294, 0.00392, 0.00588, 0.00784, 0.00931, 0.01176, 0.01372, 0.01519, 0.01568, 0.01666]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(current, force, marker='o', linestyle='-', color='blue')
plt.title('Force vs Current')
plt.xlabel('Current (A)')
plt.ylabel('Force (N)')
plt.grid(True)
plt.tight_layout()
plt.show()
