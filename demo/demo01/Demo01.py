# 装饰器

user , pwd ='xsj' ,123;

login_status = False;

def login(func):
    if login_status == False:
        username = input("username:")
        password = input("password:")
        if user == username and pwd == password:
            print("welcome");

    else:
        pass;
@login
def home():
    print("welcome to home page");

@login
def finance():
    print("welcome to finance page");

home();