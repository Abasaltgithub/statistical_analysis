import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Define prior distributions for the parameters of the two PDFs
prior_mean1 = 1227559.4166666667
prior_std1 = 521646.716744749
prior_mean2 = -181423.75
prior_std2 = 167500.34586382203

# Create a range of values for plotting
x = np.linspace(-500000, 2500000, 1000)  # Adjust the range as needed

# Calculate the prior and posterior distributions for both PDFs
prior1 = norm.pdf(x, loc=prior_mean1, scale=prior_std1)
likelihood1 = norm.pdf(x, loc=prior_mean1, scale=prior_std1)
posterior1 = likelihood1 / np.sum(likelihood1)

prior2 = norm.pdf(x, loc=prior_mean2, scale=prior_std2)
likelihood2 = norm.pdf(x, loc=prior_mean2, scale=prior_std2)
posterior2 = likelihood2 / np.sum(likelihood2)

# Plot the prior and posterior distributions for both PDFs
plt.figure(figsize=(10, 5))
plt.plot(x, prior1, label='Prior 1', linestyle='--')
plt.plot(x, posterior1, label='Posterior 1')
plt.plot(x, prior2, label='Prior 2', linestyle='--')
plt.plot(x, posterior2, label='Posterior 2')
plt.xlabel('Parameter Value')
plt.ylabel('Probability Density')
plt.legend()
plt.title('Prior and Posterior Distributions for Two PDFs')
plt.show()
