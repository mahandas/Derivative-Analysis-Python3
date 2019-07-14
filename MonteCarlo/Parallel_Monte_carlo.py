## creating a naive Monte-Carlo Implementation

import numpy as np
import time

p = (0.3,0.2,0.1,0.3)

def sample():
    time.sleep(0.1)
    return np.argmax(np.random.multinomial(1,p))

from collections import Counter

def monte_carlo(iter=1000):
    samples = []

    for _ in range(iter):
        x = sample()
        samples.append(x)

    p = Counter(samples)

    p = dict(p)

    p.update([(item, prob / float(iter)) for item, prob in p.items()])
    return p



    
k = monte_carlo()
print(k)
