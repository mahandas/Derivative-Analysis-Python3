import math
import numpy as np
import pandas as pd
import scipy.stats as scs
##import statsmodels.api as sm
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'serif'

def dN(x, mu, sigma):
    #Probability density function (pdf)
    z = (x - mu) / sigma
    pdf = np.exp(-.05 * z ** 2) / math.sqrt(2 * math.pi * sigma ** 2)
    return pdf

def simulate_gbm():
    #parameters
    S0 = 100.0
    T = 10.0
    r = 0.05
    vol = 0.2

    #simulation parameters
    np.random.seed(250000)
    gbm_dates = pd.DatetimeIndex(start='30-09-2004',end='30-09-2014',freq='B')
    M = len(gbm_dates) #time steps
    I = 1 #index leve;
    dt = 1/252.
    df = math.exp(-r * dt)
    # stock price paths
    rand = np.random.standard_normal((M, I))
    S = np.zeros_like(rand)
    S[0] = S0
    for t in range(1, M):
        S[t] = S[t -1] * np.exp((r-vol ** 2 / 2) * dt + vol * rand[t] * math.sqrt(dt))
    gbm = pd.DataFrame(S[:, 0] , index=gbm_dates, columns=['index'])
    gbm['returns'] = np.log(gbm['index'] / gbm['index'].shift(1))


    # Realized Volatility
    gbm['rea_var'] = 252 * np.cumsum(dbm['returns'] ** 2) / np.arrange(len(gbm))
    gbm['rea_vol'] = np.sqrt(gbm['rea_var'])
    gbm = gbm.dropna()
    return gbm

def print_statistics(data):
    print ("RETURN SAMPLE STATS")
    print ("---------------------------------------")
    print ("Mean of Daily Log Returns %9.6f" % np.mean(data['returns']))
    print ("Std of Daily Log Returns %9.6f" % np.std(data['returns']))
    print ("Mean of Annua. Log Returns %9.6f" % (np.mean(data['returns']) * 252))
    print ("Std of Annua. Log Returns %9.6f" % (np.std(data['returns']) * math.sqrt(252)))
    print ("---------------------------------------------")
    print ("Skew of Sample Log Returns %9.6f" % scs.skew(data['returns']))
    print ("Skew Normal Test p-value %9.6f" % scs.skewtest(data['returns'])[1])
    print ("---------------------------------------------")
    print ("Kurt of Sample Log Returns %9.6f" % scs.kurtosis(data['returns']))
    print ("Kurt Normal Test p-value %9.6f" % scs.kurtosistest(data['returns'])[1])
    print ("---------------------------------------------")
    print ("Normal Test p-value %9.6f" % scs.normaltest(data['returns'])[1])
    print ("---------------------------------------------")
    print ("Realized Volatility %9.6f" % data['rea_vol'].iloc[-1])
    print ("Realized Variance %9.6f" % data['rea_var'].iloc[-1])

def quotes_returns(data):
    plt.figure(figsize=(9, 6))
    plt.subplot(211)
    data['index'].plot()
    plt.ylabel('daily quotes')
    plt.grid(True)
    plt.axis('tight')

    plt.subplot(212)
    data['returns'].plot()
    plt.ylabel('daily log returns')
    plt.grid(True)
    plt.axis('tight')

def return_histogram(data):
    plt.figure(figsize=(9,5))
    x = np.linspace(min(data['returns']), max(data['returns']), 100)
    plt.hist(np.array(data['returns']), bins=50, normed=True)
    y = dN(x, np.mean(data['returns']), np.std(data['returns']))
    plt.plot(x, y, linewidth=2)
    plt.xlabel('log returns')
    plt.ylabel('frequency/probability')
    plt.grid(True)
