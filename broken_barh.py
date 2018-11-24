"""
===========
Broken Barh
===========

Make a "broken" horizontal bar plot, i.e., one with gaps
"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(-4.93, -0.72)], (0, 0.5), facecolors='violet')  # WO3, MnO2, SnO2, -5.658827941874999 to -4.93552791875
ax.broken_barh([(-5.65, -0.23)], (0.5, 0.5), facecolors='red')  # WO3, Mn2O3, SnO2,-5.886984983124987 to -5.658827941874999
ax.broken_barh([(-5.88, -0.58)], (1.0, 0.5), facecolors='pink')  # -6.467741869375012 to -5.886984983124987
ax.broken_barh([(-6.46, -0.54)], (1.5, 0.5), facecolors='orange')  # MnWO4, SnO2, Mn3O4, WO3, -7.0095444099999975 to -6.467741869375012


# ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), facecolors=('red', 'yellow', 'green'))
ax.set_ylim(0, 10)
ax.set_xlim(-4.93, -9)
ax.set_xlabel('seconds since start')
# ax.set_yticks([15, 25])
# ax.set_yticklabels(['Bill', 'Jim'])
#a x.grid(True)
# ax.annotate('race interrupted', (61, 25),
#             xytext=(0.8, 0.9), textcoords='axes fraction',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             fontsize=16,
#             horizontalalignment='right', verticalalignment='top')

plt.show()
