
class Area:
    
    def __init__(self, a,b):
        self.weight = a
        self.length = b

    def square(self):
        return self.weight*self.length

    def triangle(self):
        return self.weight*self.length/2

    def circle(self):
        return 3.14*(self.length^2)

area = Area(10,20,30)

print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이