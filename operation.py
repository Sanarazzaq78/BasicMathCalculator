"""Files to stores Mathematics basic operation."""


class Operation:
    """Basic Mathematical Operation class."""
    def __init__(self,number1: int ,number2:int ) -> None:
        """Initializer."""
        self.number1=number1
        self.number2=number2

    def add(self):
      print("add operation",self.number1+self.number2)

    def sub(self):
        print("sub operation", self.number1- self.number2)
    def mul(self):
        print("mul operation", self.number1* self.number2)
    def div(self):
        print("div operation", self.number1/ self.number2)
    def modu(self):
        print("modu operation", self.number1 % self.number2)