class Helpers:
    def __init__(self):
        self = self

    # 受け取った文字列が数値に変換できるか判定する
    def is_num(self, t: str) -> bool:
        try:
            float(t)
            return True
        except ValueError:
            return False

