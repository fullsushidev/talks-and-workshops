def ePrimo(num):
    print(f"Chamando ePrimo com o argumento num: {num}")

    if num % 2 == 0:
        result = num % 2
        print(f"O resto da divisão de {num} por 2 (módulo) é: {result}")
        return num == 2

    iter_div = 3
    print(f"Iterando com iter_div: {iter_div}")
    while iter_div * iter_div <= num:
        print("Enquanto iter_div * iter_div <= num, continue...")
        if num % iter_div == 0:
            print("Se num % iter_div for igual a zero, então retorne falso")
            return False
        print("Incrementando iter_div + 2")
        iter_div += 2
        print(f"Agora o valor de iter_div é: {iter_div}")

    return True


print(f"## é primo?: {ePrimo(31)}\n")
