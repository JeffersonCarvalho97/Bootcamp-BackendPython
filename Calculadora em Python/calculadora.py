#Calculadora em Python


Operacao = input("Escolha a operação desejada (soma, div, sub, mult): ")
num1 = input("Digite o primeiro Número: ")
num2 = input("Digite o segundo Número: ")


if   Operacao == "soma":
    resultado =  int(num1) + int(num2)
if   Operacao == "div":
    resultado =  int(num1) / int(num2)
if   Operacao == "sub":
    resultado =  int(num1) - int(num2)    
if   Operacao == "mult":
    resultado =  int(num1) * int(num2) 
else:
        resultado = "Operação ínvalida"    

print(" O Resultado da operação é : " +  str(resultado))

range(10)
