palavra = str(input("digite uma palavra:"))
contador = 0

for letra in palavra:
    if letra  in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        contador = contador + 1

print(contador) 

