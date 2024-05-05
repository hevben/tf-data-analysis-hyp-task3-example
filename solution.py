import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, shapiro


chat_id = 310598863 # Ваш chat ID, не меняйте название переменной

def solution(x) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.08
    mean = 300
    s, p = ttest_1samp(x,popmean=mean, alternative='greater')
    return p<alpha
