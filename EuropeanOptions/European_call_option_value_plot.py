import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'serif'


#import the defined function

import sys
sys.path.append('05_com')
from BSM_option_valuation import BSM_call_value

#Model and option Parameters
K = 8000
T = 1.0
r = 0.025
vol = 0.2

#sample generation
S = np.linspace(4000, 12000, 150)
h = np.maximum(S - K, 0)
C = [BSM_call_value(S0, K, 0, T, r, vol) for S0 in S]

plt.figure()
plt.plot(S, h, 'b-.', lw=2.5, label = 'inner value')
#plot inner value at maturity
plt.plot(S, C, 'r', lw=2.5, label='present value')
#plot option present value
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('index level $S_0$ ')
plt.ylabel('present value $C(t=0)$')
plt.show()
