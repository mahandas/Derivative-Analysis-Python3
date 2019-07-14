## BSM implied volatilities

from math import log, sqrt, exp

from scipy import  stats
from scipy.optimize import fsolve

class class_option(object):
    ''' Class for European options in BSM model

Attributes :
S0 : initial stock index level
K : strike price
t : detetime/Timestamp object
M : datetime/timestamp object
r : constant risk-free short rate 
sigma : volatility

'''
    def __init__(self, S0, K, t, M, r, sigma) :
        self.K = K
        self.S0 = float(S0)
        self.t = t
        self.M = M
        self.r = r
        self.sigma = sigma

    def update_ttm(self):
        '''updates time to maturity '''
        if self.t > self.M :
            raise ValueError("Pricing date later than maturity.")
        self.T = (self.M - self.t).days / 365

    def d1(self):
        ''' Helper function  '''
        d1 = ((log(self.S0 / self.K) + (self.r + 0.5 * self.sigma ** 2 ) * self.T) / (self.sigma * saqrt(self.T)))
        return d1

    def value(self):
        ''' Return option value '''
        self.update_ttm()
        d1 = self.d1()
        d2 = ((log(self.S0 / self.K) + (self.r - 0.5 * self.sigma ** 2) * self.T) / (self.sigma * sqrt(self.T)))

        value = (self.S0 * stats.norm.cdf(d1, 0.0, 1.0) - self.K * exp(-self.r * self.T) * stats.norm.cdf(d2, 0.0, 1.0))
        return value

    def vega(self):
        ''' Return vega of option '''
        self.update_ttm()
        d1 = self.d1()
        vega = self.S0 * stats.norm.pdf(d1, 0.0, 1.0) * sqrt(self.T)
        return vega


    def imp_vol(self, C0, sigma_est=0.2) :
        ''' return implied volatility for given option price '''
        option = call_option(self.S0, self.K, self.t, self.M, self.r, sigma_est)
        option.update_ttm()
        def difference(sigma):
            option.sigma = sigma
            return option.value() - C0
        iv = fsolve(difference, sigma_est)[0]
        return iv
                    
        
