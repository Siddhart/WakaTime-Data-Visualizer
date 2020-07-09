from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

labels = ['dogs','cats','birds','fish']
sizes = [34, 24,18,13]
pie = plt.pie(sizes,autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.legend( loc = 'right', labels=['%s, %1.1f %%' % (l, s) for l, s in zip(labels, sizes)])
plt.show()