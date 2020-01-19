class Functions:
    mem = 0
    answer = 0

    def addition(self, num1):
        add = self + num1
        list.append(add)
        return add

    def subtract(self, num1):
        sub = self - num1
        list.append(sub)
        return sub

    def multiply(self, num1):
        multi = self * num1
        return multi

    def division(self, num1):
        divide = float(self // num1)
        return divide

    def memory(self):
        self.mem = self.answer
        return self.mem

    def clear_mem(self):
        self.mem = 0
        return self.mem

print(Functions.division(80, 2))
print(Functions.multiply(8, 2))
print(Functions.subtract(20, 5))
print(Functions.addition(2, 3))






