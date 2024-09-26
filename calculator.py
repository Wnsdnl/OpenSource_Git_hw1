def add(x, y):
    return x + y

def sub(x, y):
    return x - y

num1, num2 = map(float, input("두 수를 입력하시오: ").split())

print(add(num1, num2))
print(sub(num1, num2))