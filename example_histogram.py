import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Generate some data for this
# demonstration.
data = np.random.normal(170, 10, 250)
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)

plt.show()
