class DivZeroError:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide(div, num):
        try:
            return div / num
        except:
            return f"Делить на ноль нельзя "


div = DivZeroError(5, 1)
print(DivZeroError.divide(10, 0))

