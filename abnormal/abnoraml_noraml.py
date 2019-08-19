import matplotlib
import matplotlib.pyplot as plt
import numpy as np



abnoraml=[1064, 360, 3867, 8222, 114, 7396, 5663, 62, 1428, 1407, 5609, 2514, 349, 6095, 6822, 1285, 878, 6, 178, 13, 7254, 7363, 6853, 1121, 93, 556, 2767, 110, 105]
# noraml=[146254, 146239, 146204, 129046, 8784, 128872, 106475, 8866, 146254, 146253, 108071, 146126, 8863, 108074, 128784, 146255, 146255, 8784, 11138, 8784, 128789, 107717, 129010, 146228, 8784, 146243, 145135, 128992, 128787]
noraml=[145190, 145879, 142337, 120824, 8670, 121476, 100812, 8804, 144826, 144846, 102462, 143612, 8514, 101979, 121962, 144970, 145377, 8778, 10960, 8771, 121535, 100354, 122157, 145107, 8691, 145687, 142368, 128882, 128682]
labels=['kpi11', 'kpi10', 'kpi12', 'kpi13', 'kpi9', 'kpi17', 'kpi16', 'kpi8', 'kpi28', 'kpi14', 'kpi15', 'kpi29', 'kpi6', 'kpi24', 'kpi18', 'kpi19', 'kpi25', 'kpi7', 'kpi5', 'kpi27', 'kpi26', 'kpi4', 'kpi22', 'kpi23', 'kpi1', 'kpi3', 'kpi21', 'kpi20', 'kpi2']
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars
plt.figure(figsize=(20,6))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, noraml, width, label='normal')
rects2 = ax.bar(x + width/2, abnoraml, width, label='abnormal')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('number')
ax.set_title('every kpi abnoram numbers and normal numbers')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


# autolabel(rects1)
# autolabel(rects2)

# fig.tight_layout()

plt.show()