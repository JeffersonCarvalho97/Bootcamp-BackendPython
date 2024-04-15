
# AND =  Para ser TRUE, tudo tem que ser
# OR =  Para ser TRUE, apenas um tem que ser TRUE
print( True and True)
print( True and False)
print( False and False)
print( True or True)
print( True or False)
print( False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente =  conta_especial and saldo >= saque

exp_3  = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)


e = saldo >= saque and saque <= limite
print(e)
e = saldo >= saque or saque <= limite
print(e)
