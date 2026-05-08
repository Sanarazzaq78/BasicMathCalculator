class BasicCalculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2


class Calculator(BasicCalculator):

    def Calculate(self,choice):
        "some choice.."
        if choice==1: return self.number1 +self.number2
        elif choice == 2: return self.number1 - self.number2
        elif choice == 3:   return self.number1 * self.number2
        elif choice == 4:
           if self.number2 != 0:return self.number1 / self.number2
           else:
                return "Cannot divide by zero"
        elif choice == 5: return self.number1 % self.number2
        else:
                return "Invalid choice"
number1=int(input("enter first number:"))
number2=int(input("enter second number:"))

calc=Calculator(numer1,number2)
" some calculator..."
print("result,{(1.addition,2.subtraction,3.multiplication,4.division,5.modulus)}")
choice=int(input("enter your choice.."))
result=calc.Calculate(choice)
print(result)
