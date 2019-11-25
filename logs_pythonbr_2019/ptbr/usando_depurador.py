def ePrimo(num):
    breakpoint()
    if num % 2 == 0:
        return num == 2
    iter_div = 3
    while iter_div * iter_div <= num:
        if num % iter_div == 0:
            return False
        iter_div += 2
    return True


print(f"## é primo? {ePrimo(31)}\n")
