import multiprocessing as mp
import numpy as np
import time


p = (0.3, 0.2, 0.1, 0.1, 0.3)


def sample():
    time.sleep(0.1)
    np.random.seed()
    return np.argmax(np.random.multinomial(1,p))


def _parallel_mc(iter=10):
    pool = mp.Pool(4)

    future_res = [pool.apply_async(sample) for _ in range(iter)]
    res = [f.get() for f in future_res]

    return res

def parallel_monte_carlo(iter=10):
    samples = _parallel_mc(iter)

    p = Counter(samples)

    p = dict(p)

    p.update([(item, prob / float(iter)) for item, prob in p.items()])

    return p

print(parallel_monte_carlo(iter=10))

