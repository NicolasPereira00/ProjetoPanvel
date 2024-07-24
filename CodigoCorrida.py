import random


def desenhar_movimento(rex, bob, oli):
    while True:
        linha = "-" * 21
        linha = list(linha)
        linha[rex] = "R"
        linha[bob] = "B"
        linha[oli] = "O"
        print("".join(linha))

        if abs(rex - oli) == 0 and abs(bob - oli) == 0:
            return "Oli"
        elif abs(rex - oli) == 0:
            return "Rex"
        elif abs(bob - oli) == 0:
            return "Bob"

        if rex < oli:
            rex += 1
        elif rex > oli:
            rex -= 1

        if bob < oli:
            bob += 1
        elif bob > oli:
            bob -= 1


rex = random.randint(0, 20)
bob = random.randint(0, 20)
oli = random.randint(0, 20)

print(f"Posições iniciais - Rex: {rex}, Bob: {bob}, Oli: {oli}")
resultado = desenhar_movimento(rex, bob, oli)
print(f"Resultado: {resultado}")
