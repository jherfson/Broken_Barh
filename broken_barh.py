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
ax.broken_barh([(-257.41, 2019.61)], (0, 0.25), facecolors='violet')  # WO3 ok
ax.broken_barh([(-257.41, 642.28)], (0.25, 0.25), facecolors='red')  # MnO2 ok
ax.broken_barh([(-257.41, 2333.07)], (0.50, 0.25), facecolors='pink')  # SnO2 ok
# ax.broken_barh([(384.77, 612.95)], (0.75, 0.25), facecolors='orange')  # Mn2O3 ok
ax.broken_barh([(384.77, 612.95)], (0.25, 0.25), facecolors='orange')  # Mn2O3 ok
# ax.broken_barh([(568.43, 1213.29)], (1.0, 0.25), facecolors='black')  # MnWO4 ok
ax.broken_barh([(568.43, 1213.29)], (0.75, 0.25), facecolors='black')  # MnWO4 ok
# ax.broken_barh([(997.72, 642.88)], (1.25, 0.25), facecolors='Silver')  # Mn3O4 ok
ax.broken_barh([(997.72, 642.88)], (0.25, 0.25), facecolors='Silver')  # Mn3O4 ok

ax.broken_barh([(1385.01, 725.74)], (1.50, 0.25), facecolors='Brown')  # MnSnO3 ok
# ax.broken_barh([(683.47, 393.71)], (1.75, 0.25), facecolors='Gold')  # Mn2SnO4
# ax.broken_barh([(716.68, 308.20)], (2.0, 0.25), facecolors='green')  # Mn3WO6
# ax.broken_barh([(767.81, 565.38)], (2.25, 0.25), facecolors='turquoise')  # MnO
# ax.broken_barh([(833.83, 10.59)], (2.50, 0.25), facecolors='purple')  # W18O49
# ax.broken_barh([(844.83, 147.01)], (2.75, 0.25), facecolors='salmon')  # WO2
# ax.broken_barh([(991.84, 341.36)], (3.0, 0.25), facecolors='grey')  # W
# ax.broken_barh([(1003.96, 8.42)], (3.25, 0.25), facecolors='yellow')  # Sn5O6
# ax.broken_barh([(1012.38, 66.56)], (3.50, 0.25), facecolors='blue')  # SnO
# ax.broken_barh([(1078.94, 254.26)], (3.75, 0.25), facecolors='Magenta')  # Sn
# ax.broken_barh([(1333.29, 1.0)], (4.0, 0.25), facecolors='red')  # Mn

#  printing-subscript
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

fonte = int(12)

# legend of phase
ax.text(675, 0.090, 'WO3'.translate(SUB), fontsize=fonte)
ax.text(140, 0.330, 'MnO2'.translate(SUB), fontsize=fonte)
ax.text(675, 0.60, 'SnO2'.translate(SUB), fontsize=fonte)
# ax.text(660, 0.845, 'Mn2O3'.translate(SUB), fontsize=fonte)
ax.text(660, 0.330, 'Mn2O3'.translate(SUB), fontsize=fonte) # test
# ax.text(900, 1.08, 'MnWO4'.translate(SUB), fontsize=fonte, color='White')
ax.text(900, 0.845, 'MnWO4'.translate(SUB), fontsize=fonte, color='White')
# ax.text(1150, 1.33, 'Mn3O4'.translate(SUB), fontsize=fonte)
ax.text(1150, 0.330, 'Mn3O4'.translate(SUB), fontsize=fonte) # test
ax.text(1650, 1.60, 'MnSnO3'.translate(SUB), fontsize=fonte)
# ax.text(800, 1.79, 'Mn2SnO4'.translate(SUB), fontsize=fonte)
# ax.text(795, 2.05, 'Mn3WO6'.translate(SUB), fontsize=fonte)
# ax.text(950, 2.3, 'MnO'.translate(SUB), fontsize=fonte)
# ax.text(845, 2.55, 'W18O49'.translate(SUB), fontsize=fonte)
# ax.text(870, 2.80, 'WO2'.translate(SUB), fontsize=fonte)
# ax.text(1140, 3.05, 'W'.translate(SUB), fontsize=fonte)
# ax.text(880, 3.30, 'Sn5O6'.translate(SUB), fontsize=fonte)
# ax.text(1085, 3.55, 'SnO'.translate(SUB), fontsize=fonte)
# ax.text(1185, 3.80, 'Sn'.translate(SUB), fontsize=fonte)
# ax.text(1270, 4.05, 'Mn'.translate(SUB), fontsize=fonte)


x = range(0, 1400, 150)
ax.set_xlim(0, 1350)
ax.set_xticks(x)
ax.set_xticklabels([i for i in x])
ax.set_xlabel('Temperature (°C)')

ax.set_yticks([])

ax.grid(True)

plt.show()
