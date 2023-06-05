 class Calculator:
    def sum(self, a, b):
        return a + b
    
    def product(self, a, b):
        return a * b
    
    def quotient(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        else:
            return a / b
    
    def difference(self, a, b):
        return a - b

calc = Calculator()

print(calc.sum(4, 6))  
print(calc.product(4, 6))  
print(calc.quotient(10, 2))  
print(calc.quotient(10, 0))  
print(calc.difference(10, 6))  

 