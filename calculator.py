"""Calculator runing point file."""
from operation import Operation



class Calculator:
    """Calculator class."""
    def __init__(self,number1 : int, number2:int) -> None:
        """Initialization calculator class."""
        self.number1=number1
        self.number2=number2
        self.operation = Operation(number1, number2)

    def calculate(self) -> None:
        """Calculate of calculator class."""
        print("\n choose Operation:""1.addition\n"
                                       "2.subtraction\n"
                                       "3.multiplication\n"
                                       "4.division\n"
                                       "5.modulus\n")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == "1":print("Result:",self.operation.add())
        elif choice == "2":
            print("Result:",self.operation.sub())
        elif choice == "3":
            print("Result:",self.operation.mul())
        elif choice == "4":
            print("Result:",self.operation.div())
        elif choice == "5":
            print("Result:",self.operation.modu())
        else:
            print("Invalid choice")

