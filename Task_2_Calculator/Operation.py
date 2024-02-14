class Operation:
    def __init__(self, num1=0, num2=0):
        self.a = int(num1)
        self.b = int(num2)

    def add(self):
        res = self.a + self.b
        return res

    def subtract(self):
        res = self.a - self.b
        return res

    def multiply(self):
        res = self.a * self.b
        return res

    def divide(self):
        res = self.a / self.b
        return res


def calculate(a=0, op=1, b=0):
    o = Operation(a, b)
    if op == 1:
        return o.add()
    elif op == 2:
        return o.subtract()
    elif op == 3:
        return o.multiply()
    elif op == 4:
        return o.divide()


def operator_symbol(op):
    if op == 1:
        return '+'
    elif op == 2:
        return '-'
    elif op == 3:
        return '*'
    elif op == 4:
        return '/'
    else:
        return '.'
