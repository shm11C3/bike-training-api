import numpy as np
from decimal import Decimal

class CalculatePmc:
    def __init__(self):
        self = self

    # 昨日のATLと任意のTSSからATLを返す
    def current_atl(self, yesterday_atl, current_tss):
        yesterday_atl = float(Decimal(yesterday_atl))
        current_tss = float(Decimal(current_tss))

        if current_tss > 2400 or current_tss < 0:
            return None

        if yesterday_atl > 2400 or yesterday_atl < 0:
            return None

        a = np.exp(-1 / 7)
        return yesterday_atl * a + current_tss * (1 - a)

    # 昨日のCTLと任意のTSSからCTLを返す
    def current_ctl(self, yesterday_ctl, current_tss):
        yesterday_ctl = float(Decimal(yesterday_ctl))
        current_tss = float(Decimal(current_tss))

        if current_tss > 2400 or current_tss < 0:
            return None

        if yesterday_ctl > 2400 or yesterday_ctl < 0:
            return None


        a = np.exp(-1 / 42)
        return yesterday_ctl * a + current_tss * (1 - a)
