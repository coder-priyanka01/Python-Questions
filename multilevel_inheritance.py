class GrandParent:
    def heritage(self):
        print("Heritage from GrandParent")

class Parent(GrandParent):
    pass

class Child(Parent):
    pass