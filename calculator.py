def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

num1, num2 = map(float, input("두 수를 입력하시오: ").split())

print(add(num1, num2))
print(sub(num1, num2))
print(mul(num1, num2))
print(div(num1, num2))
print("충돌을 만들기 위해 수정함 in branch 2")