import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# Generate some "random" data (actually, one would have here 
# some data from simulations/measurements)
np.random.seed(0)
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

# Plot the histogram:
num_bins = 50
fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)

# add a 'best fit' line
#y = mlab.normpdf(bins, mu, sigma)
y = scipy.stats.norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()

print("Mittelwert = {}\nVarianz = {}\n".format(np.mean(x), np.var(x)))