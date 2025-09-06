a = 12
b = 12
print(a + b)

def addition(a, b):
    return a + b

print(addition(11, 12))   
print(addition(20, 30))


 
class Addition:
    def __init__(self, a, b):
        print(a + b)

obj = Addition(10, 20)