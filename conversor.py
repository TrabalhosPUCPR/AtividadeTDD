import math


def conversor(num, base_final):
    if isinstance(num, str) or isinstance(base_final, str) or num < 0 or base_final < 0:
        return "Numero ou base invalida"
    if 2 > base_final or 16 < base_final:
        return "Base numerica invalida"
    if num < base_final:
        return num_para_letra(num)
    resultado = ""
    while num >= base_final:
        resultado += str(num_para_letra(num % base_final))
        num = int(num / base_final)
        if num < base_final:
            resultado += str(num_para_letra(num))
    return resultado[::-1]


def letra_para_num(letra):
    if letra.isdigit():
        return int(letra)
    return (ord(letra) - 65) + 10


def conversor_para_decimal(base, num):
    if isinstance(base, str) or base < 2 or base > 16:
        return "Base numerica invalida"
    if isinstance(num, int) and num < 0:
        return "Numero invalido"
    elif base < 10 and isinstance(num, str) and int(num) < 0:
        return "Numero invalido"
    resultado = 0
    num_str = num
    if not(isinstance(num, str)):
        num_str = str(num)
    size = len(num_str)
    num_str = num_str[::-1]
    while size > 0:
        num = letra_para_num(num_str[size-1])
        if num >= base:
            return "Numero invalido"
        resultado += num * math.pow(base, size - 1)
        size -= 1
    if resultado < 0:
        return "Numero invalido"
    return resultado


def num_para_letra(num):  # converte o numero pra uma letra caso ele for maior que 9
    if num < 10:
        return num
    return chr(65 + (num - 10))