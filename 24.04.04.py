# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

y1 = [350,410,520,695]
y2 = [200, 250, 385,350]
x=range(len(y1))

plt.bar(x, y1, width = 0.7, color = "blue")
plt.bar(x,y2,  width = 0.7, color = "red", bottom = y1)

plt.title("Quartely sales")

plt.xlabel("Quartely")
plt.ylabel("sales")

xLabel=['first','second','thrid','fourth']
plt.xticks(x, xLabel, fontsize = 10)
plt.legend(['chairs','desks'])
plt.show()
