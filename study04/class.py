class Hello:
    def greeting(self):
        print("Hello world!")
        
a = Hello()
a.greeting()

# result = 0
# def add(num):
#     global result
#     result += num 
#     return result

# print(add(3))
# print(add(5))

result01 = 0
result02 = 0

def add01(num):
    global result01
    result01 += num
    return result01

def add02(num):
    global result02
    result02 += num
    return result02

print("01 : ", add01(3))
print("01 : ", add01(4))

print("02 : ", add02(3))
print("02 : ", add02(7))

class Simple:
    pass

a = Simple()


# class Service :
#     secret = "영구는 배꼽이 두개다"
    
# print("-------------------------------------")

# pey = Service()
# pey.secret()

# class Service :
#     secret = "영구는 배꼽이 두 개다"
#     def sum(a, b):
#         result = a + b
#         print("%s + %s = %s 입니다." % (a, b, result))
        
        
# pey = Service
# pey.sum(1, 5)

class Foo :
    def func1():
        print("function1")
        
    def func2(self):
        print(id(self))
        print("function2")
        
f = Foo()
# print(id(f))

f2 = Foo()
f2.func2()

Foo.func1()


print("------------------------------------------------")

class Main_Service:
    secret = "영구는 귀엽다"
    def set_name(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s 입니다." %(self.name, a,b, result))

pey = Main_Service()
pey.set_name("김재경")
pey.sum(1,2)
print("------------------------------------------------")

class Sub_Service:
    secret = "영구는 귀엽다"
    def __init__(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s 입니다." %(self.name, a,b, result))
        
load = Sub_Service("김재경")
load.sum(4,5)