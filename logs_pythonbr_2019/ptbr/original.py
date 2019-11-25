def ePrimo(num):
    # verifica se é par
    if num % 2 == 0:
        # retorna verdadeiro somente quando num for 2
        return num == 2

    # itera a partir de 3, enquanto < sqrt(num)
    iter_div = 3
    while iter_div * iter_div <= num:
        # se o mod for 0, num é divisível por iter_num, num não é um número primo
        if num % iter_div == 0:
            return False

        # próximo número ímpar
        iter_div += 2

    # loop terminou sem interrupção, não foram encontrados outros divisores de num.
    # o número é primo
    return True


# Verificando se 31 é número primo
print(f"## é primo? {ePrimo(31)}\n")
