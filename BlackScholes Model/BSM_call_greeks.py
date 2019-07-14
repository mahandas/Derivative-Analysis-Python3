import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
##import mpl_toolkits.mplot3d.axes3 as p3
mpl.rcParams['font.family'] = 'serif'

from BSM_option_valuation import dlf, N, dN

def BSM_delta(St, K, t, T, r, sigma):
    d1 = dlf(St, K, t, T, r, sigma)
    delta = N(d1)
    return delta

def BSM_gamma(St, K, t, T, r, sigma):
    gamma = dN(d1) / (St * sigma * math.sqrt(T - t))
    return gamma

def BSM_theta(St, K, t, T, r, sigma):
    d1= dlf(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    theta = -(St * dN(d1) * sigma / (2 * math.sqrt(T-t))  + r * K * math.exp(-r * (T - t) * N(d2)))
    return theta

def BSM_rho(St, K, t, T, r, sigma):
    d1 = dlf(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    rho = K * (T - t) * math.exp(-r * (T - t)) * N(d2)
    return rho

def BSM_vega(St, K, t, T, r, sigma):
    d1 = dlf(St, K, t, T, r, sigma)
    vega = St * dN(d1) * math.sqrt(T - t)
    return vega


def plot_greeks(function, greek):
    St = 100.0
    K = 100.0
    t = 0.0
    T = 1.0
    r = 0.305
    sigma = 0.2
    # greek calculations
    tlist = np.linspace(0.01, 1, 25)
    klist = mp.linspace(80, 120, 25)
    V = np.zereos((len(tlist),len(klist)), dtype=np.float)
    for j in range(len(klist)):
        for i in range(len(tlist)):
            V[i, j] = function(St, klist[j], tlist[i], r, sigma)

    #3d plotting
    x, y = np.meshgrid(klist, tlist)
    fig = plt.figure(figsize=(9, 5))
    plot.plot_wireframe(x, y, V)
    plot.set_xlabel('strike $K$')
    plot.set_ylabel('maturity $T$')
    plot.set_zlabel('%s(K, T)' % greek)
