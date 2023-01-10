# oop; inheritance: parent, child
# 
# class parent:
#     pass

# class child(parent):
#     pass

class Quad:
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    
    def Perimeter(self):
        print("Perimeter is: ",self.num1 + self.num2 + self.num3 + self.num4)

# obj = Quad(1,2,3,4)
# print(obj.Perimeter())

class rectangle(Quad):
    def __init__(self, num1, num2):
        super().__init__(num1, num2, num1, num2)

rect = rectangle(10,20)
rect.Perimeter()

class Square(Quad):
    def __init__(self, num1):
        super().__init__(num1, num1, num1, num1)
sqr = Square(10)
sqr.Perimeter()
        
    
        

        
        