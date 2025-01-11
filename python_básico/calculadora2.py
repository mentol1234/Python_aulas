N1 = float(input("Digite o 1º número:"))
op = input("digite o sinal:")
N2 = float(input("Digite o 2º número:"))
           
if op == "+":
    R = N1 + N2 
    
elif op == "-":
    R = N1 - N2
    
elif op == "*":
    R = N1 * N2 
    
elif op == "**":
    R = N1 ** N2 
    
elif op == "/":
    R = N1 / N2
    
print(R)
