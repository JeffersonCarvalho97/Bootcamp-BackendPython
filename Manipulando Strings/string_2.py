nome = "Jefferson"
Idade = 27
profissão = "Programador"
Linguagem = "Python"
saldo =  45.435

dados = {"nome" : "Jefferson", "idade": 27 }

print("Nome: %s Idade: %d " % (nome,Idade))

print("Nome:{} Idade: {} ".format(nome,Idade))

print("Nome:{1} Idade: {0} ".format(Idade,nome))

print("Nome:{1} Idade: {0} Nome: {1} {1} ".format(Idade,nome))

print("Nome:{nome} Idade: {idade} ".format(nome=nome,idade=Idade))

print("Nome:{name} Idade: {age} {name} {name} ".format(age=Idade,name=nome))

print("Nome:{nome} Idade: {idade} ".format(**dados))


print(f"Nome : {nome} Idade: {Idade}")
print(f"Nome : {nome} Idade: {Idade} Saldo: {saldo:.2f}")






