class MathClass:

    def Add(self,num1,num2):
        if self.Validation(num1,num2):
            return num1 + num2
        else:
            return 'Incorrect number format.'

    def Subtract(num1,num2):
        return num2 - num1

    def Validation(num1,num2):
        var = bool( bool (type(num1) == int) and bool ( type(num2) == int) )
        return var

num1 = 10
num2 = 20
print(MathClass.Add(MathClass,num1,num2))
print(MathClass.Add(MathClass,'a',num2))
print(MathClass.Subtract(num1,num2))
