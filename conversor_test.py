from conversor import *


def test_conversor_string_base():
    assert conversor(5, "ssss") == "Numero ou base invalida"


def test_conversor_numero_negativo():
    assert conversor(-5, 2) == "Numero ou base invalida"


def test_conversor_numero_negativo_base():
    assert conversor(5, -255) == "Numero ou base invalida"


def test_conversor_base_alta():
    assert conversor(255, 166) == "Base numerica invalida"


def test_conversor_base_baixa():
    assert conversor(255, 1) == "Base numerica invalida"


def test_conversor_10_binario():
    assert conversor(10, 2) == "1010"


def test_conversor_25_binario():
    assert conversor(25, 2) == "11001"


def test_conversor_999999_binario():
    assert conversor(999999, 2) == "11110100001000111111"


def test_conversor_10_octal():
    assert conversor(10, 8) == "12"


def test_conversor_25_octal():
    assert conversor(25, 8) == "31"


def test_conversor_999999_octal():
    assert conversor(999999, 8) == "3641077"


def test_conversor_10_hexadecimal():
    assert conversor(10, 16) == "A"


def test_conversor_25_hexadecimal():
    assert conversor(25, 16) == "19"


def test_conversor_999999_hexadecimal():
    assert conversor(999999, 16) == "F423F"


def test_conversor_hex_para_decimal():
    assert conversor_para_decimal(16, "A15") == 2581


def test_conversor_hex_para_decimal2():
    assert conversor_para_decimal(16, "FF67") == 65383


def test_conversor_oct_para_decimal():
    assert conversor_para_decimal(8, 5025) == 2581


def test_conversor_oct_para_decimal2():
    assert conversor_para_decimal(8, 177547) == 65383


def test_conversor_bin_para_decimal():
    assert conversor_para_decimal(2, "101000010101") == 2581


def test_conversor_bin_para_decimal2():
    assert conversor_para_decimal(2, "001111111101100111") == 65383

def test_conversor_bin_para_decimal_string():
    assert conversor_para_decimal("2", "101000010101") == "Base numerica invalida"


def test_conversor_bin_para_decimal_negativo():
    assert conversor_para_decimal(-2, "001111111101100111") == "Base numerica invalida"

def test_conversor_bin_para_decimal_negativo2():
    assert conversor_para_decimal(8, -55) == "Numero invalido"


def test_conversor_bin_para_decimal_negativo_string():
    assert conversor_para_decimal(8, "-55") == "Numero invalido"


def test_conversor_hex_para_decimal_negativo_string():
    assert conversor_para_decimal(16, "-A15") == "Numero invalido"


def test_conversor_hex_para_decimal_hex_inexistente():
    assert conversor_para_decimal(16, "G15") == "Numero invalido"


def test_conversor_basex_para_decimal_base_inexistente():
    assert conversor_para_decimal(11, "F15") == "Numero invalido"


def test_conversor_basex_para_decimal():
    assert conversor_para_decimal(9, "16") == 15


def test_letra_para_num():
    assert letra_para_num('A') == 10


def test_letra_para_num2():
    assert letra_para_num('F') == 15


def test_num_para_letra():
    assert num_para_letra(10) == 'A'


def test_num_para_letra2():
    assert num_para_letra(15) == 'F'
