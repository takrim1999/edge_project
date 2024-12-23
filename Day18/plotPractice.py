import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)  # 100 evenly spaced numbers from 0 to 10
y = np.sin(x)

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Wave")

# Display the plot
plt.show()