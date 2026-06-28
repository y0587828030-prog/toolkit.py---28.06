#Part 1
#step 1
# def greet(name):
#     print(f"hello, {name}")
# greet("agent x")

# #step 2
# def add(a,b):
#     print(a + b)
# add(3, 4)

# #step 3
# def square(n):
#     print(n**2)
# square(12)

#step 4
def greet_with_title(name, title= "agent"):
    print("hello",title, name)
greet_with_title("yehosh")

def greet_with_title(name, title="agent"):
    print("hello",title, name)
greet_with_title("yehosh", "commander")

#step 5
def describe(name, level, active):
    print("name:", name, "level:", level , "active:" ,active )
describe(name="agent x.", active= True, level=5)

#step 6
def multiply(a, b=2):
    print(a * b)
multiply(5)

def multiply(a, b=2):
    print(a * b)
multiply(5,5)