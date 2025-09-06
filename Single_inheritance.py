class Father:
    def skill(self):
        print("coding")

class Mother:
    def skill(self):
        print("cooking")

class Child(Father, Mother):
    def show(self):
        print("I have multiple skills:")