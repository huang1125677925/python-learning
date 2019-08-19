import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig= plt.figure()

ax=plt.subplot(221)
# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

ax1 = plt.subplots(222)

# Example data
people1 = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos1 = np.arange(len(people))
performance1 = 3 + 10 * np.random.rand(len(people))
error1 = np.random.rand(len(people))

ax1.barh(y_pos1, performance1, xerr=error, align='center')
ax1.set_yticks(y_pos1)
ax1.set_yticklabels(people1)


plt.show()