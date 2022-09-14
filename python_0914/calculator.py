class Calc():

    def set_number(self):
        self.num1,self.num2 = map(int, input().split())

    def plus(self):
        return self.num1+self.num2

    def minus(self):
        return self.num1-self.num2

    def multiple(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2

  


calc = Calc()

try:
    calc.set_number()
    print(calc.plus()) # 더한 값
    print(calc.minus()) # 뺀 값
    print(calc.multiple()) # 곱한 값
    print(calc.divide()) # 나눈 값

except ValueError:
    print("숫자만 입력 가능합니다.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")