import numpy as np
import random
from abc import ABC, abstractmethod
from typing import Type


def argmin(array):
    return min((x, random.random(), i) for i,x in array)[2]
    # get array[j][0] s.t. array[j][1] is minimal
    # if tied, choose randomly
    # array can be interpreted as zip(args, values)

def randround(x:float):
    prob = x%1
    return int(x) + (prob > random.random())

def quantile(x, quantiles):
    i = 0
    for q in quantiles:
        if x < q:
            return i
        i += 1
    return i

class Strategy(ABC):
    name:str
    def choose(candidates:list[int], alloc:np.ndarray, info) -> int:
        pass
    def info(alloc:np.ndarray):
        pass

class strat:
    class Null(Strategy):
        name='na'

    class Compare(Strategy):
        name='cmp'
        def choose(candidates:list[int], alloc:np.ndarray, info=None) -> int:
            return argmin([(i, alloc[i]) for i in candidates])
        
    class Median(Strategy):
        name='med'
        def choose(candidates:list[int], alloc:np.ndarray, median) -> int:
            return argmin([(i, alloc[i] >= median) for i in candidates])
        def info(alloc:np.ndarray):
            return np.median(alloc)
        
    class Quartile(Strategy):
        name='qua'
        def choose(candidates:list[int], alloc:np.ndarray, quartiles) -> int:
            return argmin([(i, quantile(alloc[i], quartiles)) for i in candidates])
        def info(alloc:np.ndarray):
            return np.quantile(alloc, q=[0.25, 0.5, 0.75])

def choose_bin(d:int, m:int, alloc:np.ndarray, strategy:Type[Strategy], info):
    if d == 1:
        return random.randrange(m)
    else:
        candidates = [random.randrange(m) for _ in range(d)]
        return strategy.choose(candidates, alloc, info)

def balls_and_bins(
        n:int, #balls
        m:int, #bins
        d:int|float, #choices
        b:int = 1, #batch size
        strategy:Type[Strategy] = strat.Compare,
):
    alloc = np.zeros(m, dtype=np.int64)
    batch = np.zeros(m, dtype=np.int64)
    if d == 1:
        strategy = strat.Null
    for i in range(n):
        if i % b == 0:
            alloc += batch
            batch = np.zeros(m, dtype=np.int64)
            info = strategy.info(alloc)
        bin = choose_bin(randround(d), m, alloc, strategy, info)
        batch[bin] += 1
    alloc += batch
    return alloc

def max_gap(alloc:np.ndarray, expected_value:float):
    return max(alloc) - expected_value
