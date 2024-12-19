a = int(input("digite a 1º num: "))
op = input("digite a operação: ")
b = int(input("digite o 2º num: "))

if op == "+":
    c = a + b
    
elif op == "-":
    c = a - b

elif op == "*":
    c = a * b
    
elif op == "**":
    c = a**b
    
elif op == "/":
    c = a/b
    
print(c)
