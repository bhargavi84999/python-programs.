'''def power(base,exponent=2):
    return base **exponent
print(power(5,2))
print(power(2))'''

'''def connect(host,port=3306,protocol='TCP'):
     return (f'host:{host},port:{port},protocol:{protocol}')
print(connect("localhost"))'''

'''def fun(age,name='bhargavi'):
    print(f'name:{name}')
    print(f'age:{age}')
fun(20)'''

'''def discount_price(price,discount=10):
    return (f'price:{price},discount:{discount}')
print(discount_price(100))'''

'''def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_all(2, 3, 4))'''

'''def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(key, ":",value)
print(display_tags(name="bhargavi",age=20,city="porumamilla"))'''

'''def describe_person(name,*hobbies):
    print("name:",name)
    print("hobbies:",hobbies)
describe_person("bhargavi","reading","playing","listing")'''

'''def f(*args):
    print(type(args))
f(1,2,3)'''

def create_html_tag(tag, **attributes):
    print("<" + tag, end=" ")
    for key, value in attributes.items():
        print(f"{key}='{value}'", end=" ")
    print(">")
create_html_tag(
    "a",
    href="https://python.org",
    target="_blank"
    )

def mixed(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
mixed(10,20,"hanish","hyd",x=6,y=5)




