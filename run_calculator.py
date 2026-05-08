class Calculate:
   def __init__(self,calculator):
      self.calculator=calculator

   def Calculate(self):
      number1=int(input("enter first number:"))
      number2 = int(input("enter second number:"))
      result=self.calculator.Calculate(number1,number2)
      print("rsult",result)


calc1=Calculate()
calc1.Calculate()