class Demo:
    def __init__(self):
        self.name = "Public Member"
        self.__age = 18  
        self.__salary = 50000


    def show(self):
        print("Inside class")
        print("Public:", self.name)
        print("Protected:", self.__age)
        print("Private:", self.__salary)

obj = Demo()
obj.show()