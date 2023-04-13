import pandas as pd
import numpy as np
import scipy.stats

chat_id = 1943224240 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = scipy.stats.ks_2samp(x, y, alternative='two-sided', method='auto')[1])
    p = 0.07
    if a <= p:
      return True
    else:
      return False

