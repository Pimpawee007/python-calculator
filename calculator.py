class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b): 
        return a - b # แก้เป็น a-b

    def multiply(self, a, b):
        result = 0
        for i in range(b): # b+1 ทำให้ลูปเกินมา 1 รอบ แก้เป็น b
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        negative = False # ตั้งเงื่อนไขเช็คการหารเลขติดลบ
        if (a<0) and (b<0):
            a = abs(a)
            b = abs(b)
            negative = False
        elif (a<0) or (b<0):
            a = abs(a)
            b = abs(b)
            negative = True
        while a >= b: # a>b ทำให้ลูปขาด 1 รอบ แก้เป็น a>=b
            a = self.subtract(a, b)
            result += 1
        if negative is True:
            return -result
        else:
            return result
    
    def modulo(self, a, b):
        while a >= b: # a<=b ทำให้ลูปขาด 1 รอบ แก้เป็น a>=b
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))