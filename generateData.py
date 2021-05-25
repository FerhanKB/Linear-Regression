import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
import csv

# Generate 100 random points
m = 0.5
c = 4
x = np.arange(0, 10, 0.1, dtype=np.float32)
d = np.random.uniform(-1, 1, size = x.shape[0])
y = m * x + c + d

# Save the points in data.csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["X", "Y"])
    for i in range(x.shape[0]):
        writer.writerow([x[i], y[i]])

# Plot the points
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()