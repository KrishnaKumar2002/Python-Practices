rom matplotlib import pyplot as plt
import style from matplotlib
import numpy as np
style.use('ggplot')
x,y=np.loadtxt('plotting.csv',unpack=True,delimiter=',')
plt.plot(x,y)