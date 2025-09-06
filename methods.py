class MyClass:
    def instance_method(self):
        print("This is an instance method")
obj = MyClass()
obj.instance_method()


class Myclass:
    @classmethod
    def class_method(cls):
        print("This is a class method")
Myclass.class_method()

class Myclasss:
    @staticmethod
    def static_method():
        print("This is a static method")

Myclasss.static_method()