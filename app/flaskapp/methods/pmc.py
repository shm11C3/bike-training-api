import numpy as np
from decimal import Decimal

# 昨日のATLと任意のTSSからATLを返す
def current_atl(yesterday_atl, current_tss):
    yesterday_atl = float(Decimal(yesterday_atl))
    current_tss = float(Decimal(current_tss))

    if current_tss > 2400:
        current_tss = 0

    a = np.exp(-1 / 7)
    return yesterday_atl * a + current_tss * (1 - a)

# 昨日のCTLと任意のTSSからCTLを返す
def current_ctl(yesterday_ctl, current_tss):
    yesterday_ctl = float(Decimal(yesterday_ctl))
    current_tss = float(Decimal(current_tss))

    if current_tss > 2400:
        current_tss = 0


    a = np.exp(-1 / 42)
    return yesterday_ctl * a + current_tss * (1 - a)
