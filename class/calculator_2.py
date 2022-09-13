class Calc():

    def set_number(self,a,b):
        self.num1 = a
        self.num2 = b

    def plus(self):
        return self.num1+self.num2

    def minus(self):
        return self.num1-self.num2

    def multiple(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2






calc = Calc()
calc.set_number(20, 10)
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값