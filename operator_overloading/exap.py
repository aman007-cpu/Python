from ast import Num


class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num
    def __mul__(self,num2):
        print("lets Multiply")
        return self.num * num2.num   
    def __str__(self):
        return f"Decimal number : {self.num}"
        

n1 = Number(4)
n2 = Number(6)

sum = n1 + n2
mul = n1*n2
print(sum)
print(mul)