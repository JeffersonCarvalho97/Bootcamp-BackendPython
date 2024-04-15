MAIOR_IDADE = 18
OPCIONAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")    

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH")  

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == OPCIONAL:
    print("Pode tirar a CNH com permissão do responsável")

else:
    print("Ainda não pode tirar a CNH")      