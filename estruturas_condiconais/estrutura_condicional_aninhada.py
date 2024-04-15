
conta_normal = True
conta_universitaria = False


saldo = 2000
saque = 2400
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível Realizar o saque. Motivo: O saque foi de saque é  Maior que o  saldo  e o Cheque Especial. ")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")   
    else:
        print("Saldo insuficiente!")
