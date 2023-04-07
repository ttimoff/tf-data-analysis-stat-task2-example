import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import gamma

chat_id = 223196602 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    loc = x.mean()
    return (loc + gamma.ppf(alpha / 2, a=n) / n - 1 / 2) * 2 / 26 ** 2, \
           (loc + gamma.ppf(1 - alpha / 2, a=n) / n - 1 / 2) * 2 / 26 ** 2
