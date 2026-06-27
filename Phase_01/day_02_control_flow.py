
def check_number(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
    
print(check_number(5))
print(check_number(-2))
print(check_number(0))

#----------

def check_number(n):
    if n>0:
        return "positive"
    else:
        return "zero"
    
print(check_number(5))
print(check_number(-2))
print(check_number(0))

#-----

def calculate(a,b,operation):
    if operation == "add":
        return a+b
    elif operation == "multiply":
        return a*b
    elif operation == "m":
        return a-b
    else:
        return "No operation"
    
addition = calculate(2,4,"add")
print(addition)
print(calculate(2,4,"add"))
print(calculate(2,4,"m"))