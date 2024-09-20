class PersonList:
    def __init__(self) -> None:
        pass
class Person:
    class Adress:
        def __init__(self) -> None:
            self.__purok = None
            self.__balangay = None
        def setPurok(self)-> None:
            self.__purok = prompt("Input Purok: ")
        def setAll(self):
            self.setPurok()
    def __init__(self) -> None:
        pass
def prompt(phrase:str, type:type[str|int]= str)-> str:
    __input  = input("Enter {}: ".format(phrase))
    if type is int:
        try:
            return int(__input)
        except Exception as err:
            print(f'Error Message: {err}')
    elif type is str:
        return __input
print(prompt("nice", type=int))