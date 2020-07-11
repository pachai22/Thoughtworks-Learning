
def decorator1(arg):
    def outer():
        return " outer "+arg()+" outer "
    return outer



def decorator2(arg1):
    def inner():
        return " inner "+arg1()+" inner "
    return inner



@decorator1
@decorator2
def string():
    return "inside"
print(string())
