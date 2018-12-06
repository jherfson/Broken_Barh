"""
===========
Broken Barh
===========

Make a "broken" horizontal bar plot, i.e., one with gaps

Created on Wed Nov  20 16:53:08 2018

@author: jherfson
"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(-257.41, 1091.24)], (0, 0.25), facecolors='violet')  # WO3
ax.broken_barh([(-257.41, 343.55)], (0.25, 0.25), facecolors='red')  # MnO2
ax.broken_barh([(-257.41, 1003.96)], (0.50, 0.25), facecolors='pink')  # SnO2
ax.broken_barh([(86.14, 332.6)], (0.75, 0.25), facecolors='orange')  # Mn2O3
ax.broken_barh([(183.02, 825.68)], (1.0, 0.25), facecolors='black')  # MnWO4
ax.broken_barh([(418.74, 349.08)], (1.25, 0.25), facecolors='Silver')  # Mn3O4
ax.broken_barh([(629.05, 393.95)], (1.50, 0.25), facecolors='Brown')  # MnSnO3
ax.broken_barh([(683.47, 393.71)], (1.75, 0.25), facecolors='Gold')  # Mn2SnO4
ax.broken_barh([(716.68, 308.20)], (2.0, 0.25), facecolors='green')  # Mn3WO6
ax.broken_barh([(767.81, 565.38)], (2.25, 0.25), facecolors='turquoise')  # MnO
ax.broken_barh([(833.83, 10.59)], (2.50, 0.25), facecolors='purple')  # W18O49
ax.broken_barh([(844.83, 147.01)], (2.75, 0.25), facecolors='salmon')  # WO2
ax.broken_barh([(991.84, 341.36)], (3.0, 0.25), facecolors='grey')  # W
ax.broken_barh([(1003.96, 8.42)], (3.25, 0.25), facecolors='yellow')  # Sn5O6
ax.broken_barh([(1012.38, 66.56)], (3.50, 0.25), facecolors='blue')  # SnO
ax.broken_barh([(1078.94, 254.26)], (3.75, 0.25), facecolors='Magenta')  # Sn
ax.broken_barh([(1333.29, 1.0)], (4.0, 0.25), facecolors='red')  # Mn

#  printing-subscript
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

fonte = int(11)

# legend of phase
ax.text(400, 0.06, 'WO3'.translate(SUB), fontsize=fonte)
ax.text(90, 0.3, 'MnO2'.translate(SUB), fontsize=fonte)
ax.text(400, 0.55, 'SnO2'.translate(SUB), fontsize=fonte)
ax.text(220, 0.79, 'Mn2O3'.translate(SUB), fontsize=fonte)
ax.text(500, 1.05, 'MnWO4'.translate(SUB), fontsize=fonte, color='White')
ax.text(550, 1.30, 'Mn3O4'.translate(SUB), fontsize=fonte)
ax.text(750, 1.53, 'MnSnO3'.translate(SUB), fontsize=fonte)
ax.text(800, 1.79, 'Mn2SnO4'.translate(SUB), fontsize=fonte)
ax.text(795, 2.05, 'Mn3WO6'.translate(SUB), fontsize=fonte)
ax.text(950, 2.3, 'MnO'.translate(SUB), fontsize=fonte)
ax.text(845, 2.55, 'W18O49'.translate(SUB), fontsize=fonte)
ax.text(870, 2.80, 'WO2'.translate(SUB), fontsize=fonte)
ax.text(1140, 3.05, 'W'.translate(SUB), fontsize=fonte)
ax.text(880, 3.30, 'Sn5O6'.translate(SUB), fontsize=fonte)
ax.text(1085, 3.55, 'SnO'.translate(SUB), fontsize=fonte)
ax.text(1185, 3.80, 'Sn'.translate(SUB), fontsize=fonte)
ax.text(1270, 4.05, 'Mn'.translate(SUB), fontsize=fonte)







# ax.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), facecolors=('red', 'yellow', 'green'))ax.set_ylim(0, 10)
ax.set_xlim(0, 1400)
ax.set_xlabel('Temperature')
#ax.set_yticks([0, 2.5])
# ax.set_yticklabels(['Bill', 'Jim'])
# ax.grid(True)
# ax.annotate('race interrupted', (61, 25),
#             xytext=(0.8, 0.9), textcoords='axes fraction',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             fontsize=16,
#             horizontalalignment='right', verticalalignment='top')

plt.show()
