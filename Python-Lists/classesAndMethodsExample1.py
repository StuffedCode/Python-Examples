def Validation(num1, num2):
    var = bool( bool( type(num1) == int) and bool( type(num2) == int) )
    return var

#A simple math class
class MathClass:

    #Simple Add Method/Function
    def Add(num1, num2):
        if Validation(num1,num2):
            return num1 + num2
        else:
            return 'Incorrect number format.'

    #Simple Subtract Method/Function
    def Subtract(num1, num2):
        return num2 - num1

    #Simple Multiply Method/Function
    def Multiply(num1,num2):
        return num1 * num2

    #Simple Division Method/Function
    def Divide(num1,num2):
        if num1 == 0:
            return 'Cannot divide by zero!'
        return num2/num1

num1 = 10
num2 = 20
print(MathClass.Add(num1, num2))
print(MathClass.Subtract(num1,num2))
print(MathClass.Multiply(num1,num2))
print(MathClass.Divide(num1,num2))
print(MathClass.Divide(0,num2))
print(MathClass.Add('a',3))