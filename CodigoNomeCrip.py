def rotate_text(rotacoes, texto):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    texto_cifrado = []

    for char in texto:
        if char.isalpha() and char.lower() in alfabeto:
            is_upper = char.isupper()
            original_index = alfabeto.index(char.lower())
            new_index = (original_index + rotacoes) % len(alfabeto)
            new_char = alfabeto[new_index]
            if is_upper:
                new_char = new_char.upper()
            texto_cifrado.append(new_char)
        else:
            texto_cifrado.append(char)

    return "".join(texto_cifrado)


texto = "Ola, meu nome eh Carlos! e o Seu?"
rotacoes = 7
resultado = rotate_text(rotacoes, texto)
print(resultado)
