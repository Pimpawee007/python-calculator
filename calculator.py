class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b): 
        return a - b # แก้เป็น a-b

    def multiply(self, a, b):
        result = 0
        if (a<0 and b<0):
            a, b = abs(a), abs(b)
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
        aNeg = False
        negative = False
        bOrigin = b 
        
        if (a<0) and (b<0):
            a = abs(a)
            b = abs(b)
            negative = True
        elif b<0:
            negative = True
            b = abs(b)
        elif a<0:
            a = abs(a)
            aNeg = True
            
        while a >= b: # a<=b ทำให้ลูปขาด 1 รอบ แก้เป็น a>=b
            a = a-b
            
        if a == 0:
            return 0
        if negative is True:
            if bOrigin > 0:
                return -a
            else:
                return -(b - a)
        else:
            if aNeg is True:
                return b - a
            else:
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