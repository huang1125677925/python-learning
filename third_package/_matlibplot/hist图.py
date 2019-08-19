import numpy as np

import matplotlib.pyplot as plt
rng = np.random.RandomState(10)  # deterministic random data
a = np.hstack((rng.normal(size=1000),
               rng.normal(loc=5, scale=2, size=1000)))
_ = plt.hist(a, bins=20)  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")

plt.show()