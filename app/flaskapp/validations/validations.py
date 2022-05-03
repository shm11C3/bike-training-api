from array import array
from crypt import methods
from decimal import Decimal

class Validation:
    def __init__(self):
        self = self

    def required(self, request: any):
        return (request != "")

    def max(self, request: any, value: int):
        if self.num(request):
            return float(Decimal(request)) <= value
        else:
            return len(request) <= value

    def min(self, request: any, value: int):
        if self.num(request):
            return float(Decimal(request)) >= value
        else:
            return len(request) >= value

    # 受け取った文字列が数値に変換できるか判定する
    def num(self, request: str) -> bool:
        try:
            float(request)
            return True
        except ValueError:
            return False

