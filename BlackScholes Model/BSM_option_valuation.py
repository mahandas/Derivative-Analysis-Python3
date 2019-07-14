import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'serif'
from scipy.integrate import quad

#BSM : Black Scholes Merton model


def dN(x):
    # Probabilty density function 
    return math.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)
def N(d):
    # Cumulative density function 
    return quad(lambda x: dN(x), -20, d, limit=50) [0]

def dlf(St, K, t, T, r, sigma):
    # Block-scholes-Merton d1 function
    dl = (math.log(St/ K) + (r + 0.5 * sigma ** 2) * (T - t)) / (sigma * (T - t))
    return dl

def BSM_call_value(St, K, t, T, r, sigma) :
    d1 = dlf(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * N(d1) - math.exp(-r * (T - t)) * K * N(d2)
    return call_value

def BSM_put_value(St, K, t, T, r, sigma) :
    put_value = BSM_call_value(St, K, t, T, r, sigma) - St + math.exp( -r * (T - t)) * K
    return put_value


def plot_values(function):
    ''' plot values for different parameters '''
    plot.figure(figsize=(10, 8.3))
    points = 100

    St = 100.0 # index level
    K = 100.0 # option strike
    t = 0.0 # valuation date
    T = 1.0 # maturity date
    r = 0.05 # risk free rate
    sigma = 0.2 # volatility

    # C(K) plot
    plt.subplot(221)
    klist = np.linspace(80, 120, points)
    vlist = [function(St, K, t, T, r, sigma) for K in Klist]
    plt.plot(klist, vlist)
    plt.grid()
    plt.xlabel('strike $K$')
    plt.ylabel('present value')

    # C(T) plot
    plt.subplot(222)
    tlist = np.linspace(0.001, 1, points)
    vlist = [function(St, K, t, r, sigma) for T in tlist]
    plt.plot(tlist, vlist)
    plt.grid(True)
    plt.xlabel('maturity $T$')

    # C(r) plot
    plt.subplot(223)
    rlist = np.linspace(0, 0.1, points)
    vlist = [function(St, K, t, T, r, sigma) for r in rlist]
    plt.plot(tlist, vlist)
    plt.grid(True)
    plt.xlabel('Short rate $r$')
    plt.ylabel('present value')
    plt.axis('tight')

    # C(sigma) plot
    plt.subplot(224)
    slist = np.linsplace(0.01, 0.5, points)
    vlist = [funtion(St, K, t, r, sigma) for sigma in slist]
    plt.plot(slist, vlist)
    plt.grid(True)
    plt.xlabel('Volatility $\sigma$')
    plt.tight_layout
