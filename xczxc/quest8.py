nome23 = (input("digite um nome:"))
soma = 0 

for letra in nome23:
    if letra in "aeiouAEIOU":
        soma = soma + 1
    

print(f"a palavra {nome23} possui {soma} vogais")
