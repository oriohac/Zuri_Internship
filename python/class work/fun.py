def new_func():
     print("Hello")
new_func()
def new(x):
    return x*2 
print(new(2))
def get_input(user_input):
    user_input = input("what is your name: ")
    print(user_input)
get_input('hello')

def your_name():
    name = input("whats your name: ")
    print(name)
for i in range(3):
    your_name()
def user_info(age, name, country):
    print("this is the age of the user",age, "this is the name of the user",name,"this is the country of the user",country)
user_info(8,"chike","Nigeria")
user_info(90,"Zuri","Kenya")

def user_info(*args):
    for i in args:
        print(i)
    
user_info(h = 'hello', o= 'orange', a = 'apple')
def user_info(**kwargs):
    for i in kwargs:
        print(i)
user_info(h = 'hello', o= 'orange', a = 'apple')

def greater(first,second):
    if first > second:
        return True
    else:
        return False
print(greater(6,8))

