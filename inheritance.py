class parent:
    def greet(self):
        print("Hello from Parent")

class child(parent):
    pass

obj = child()
obj.greet()


class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print(f"Hello, {self.name} from Child")
c = Child("Priyanka")
c.display()