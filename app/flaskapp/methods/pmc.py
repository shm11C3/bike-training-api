import numpy as np
from decimal import Decimal

class CalculatePmc:
    def __init__(self):
        self = self

    # 昨日のATLと任意のTSSからATLを返す
    def current_atl(self, yesterday_atl, current_tss):
        a = np.exp(-1 / 7)
        return float(Decimal(yesterday_atl)) * a + float(Decimal(current_tss)) * (1 - a)

    # 昨日のCTLと任意のTSSからCTLを返す
    def current_ctl(self, yesterday_ctl, current_tss):
        a = np.exp(-1 / 42)
        return float(Decimal(yesterday_ctl)) * a + float(Decimal(current_tss)) * (1 - a)
