
#texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# exemplo utilizando a função iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:        
    print() # Adiciona uma quebra de linha  


# exemplo utilizando a função built-in range
for numero in range( 0, 51 , 5):
    print(numero, end=" ")