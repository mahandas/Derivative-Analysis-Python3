import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'serif'
#strike price
K = 8000


#graphical output
S = np.linspace(7000,9000,100) #index level values
h= np.maximum(S - K, 0) #inner values of  call option

plt.figure()
plt.plot(S, h, lw=2.5)  #plot values at maturity
plt.xlabel('index level $S_t$ at maturity')
plt.ylabel('inner value of European call option')
plt.grid(True)

plt.show()

