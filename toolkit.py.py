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

# #step 4
# def greet_with_title(name, title= "agent"):
#     print("hello",title, name)
# greet_with_title("yehosh")

# def greet_with_title(name, title="agent"):
#     print("hello",title, name)
# greet_with_title("yehosh", "commander")

# #step 5
# def describe(name, level, active):
#     print("name:", name, "level:", level , "active:" ,active )
# describe(name="agent x.", active= True, level=5)

# #step 6
# def multiply(a, b=2):
#     print(a * b)
# multiply(5)

# def multiply(a, b=2):
#     print(a * b)
# multiply(5,5)

# #step 7
# def print_largest(a, b, c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#      print(c)
# print_largest(3,8,5)
# print_largest(7,2,10)
# print_largest(1,4,4)

# #step 8
# def show_fahrenheit(c):
#     f = (c * 9 / 5) + 32
#     print(f)

# show_fahrenheit(0)
# show_fahrenheit(100)
# show_fahrenheit(37.5)

# #step 9
# def check_even(n):
#     if n % 2 == 0:
#         print(n, "- number is even ")
#     else: 
#         print(n, "- number is odd ")
# check_even(4)
# check_even(7)

# #step 10

# def summarize(items):
#    total = 0
#    smallest = items[0]
#    largern= items[0]

#    for num in items:
#       total +=num
#       if num < smallest:
#          smallest = num
#       if num > largern:
#            largern = num

#    print(f"sum :{total}")
#    print(f"smallest: {smallest}")
#    print(f"largern : {largern}")

# tast_list = [4, 9, 2, 10, 3]
# summarize(tast_list)

## part 2 Optional Advanced Basics
#step 1
def show_all(*args):
    print(args)
    for item in args:
        print(item)
show_all("radio", "map", "flashlight")

#step 2
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_profile(name="Agent X", level=7, active=True)