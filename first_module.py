def my_name(name):
    return "Hi,This is "+name+"."
class var():
    def __new__(self,a,b):
        self.a=a
        self.b=b
        return '''x : %s
y : %s'''%(self.a,self.b)
    




