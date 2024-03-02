def decimal_to_binary(decimal):
    binary = ''
    powers_of_two = [128, 64, 32, 16, 8, 4, 2, 1]
    for power in powers_of_two:
        if decimal >= power:
            binary += '1'
            decimal -= power
        else:
            binary += '0'
    return binary

def binary_to_hex(binary):
    hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    hex_string = ''
    for i in range(0, len(binary), 4):
        hex_chunk = binary[i:i+4]
        hex_string += hex_dict[hex_chunk]
    return hex_string

def main():
    decimal_input = int(input('請您輸入一個介於0到255之間的十進位數字:'))
    if decimal_input <0:
        print('0您所輸入的數字超出指定範圍了')
    if decimal_input >255:
        print('您所輸入的數字超出指定範圍了')
    else:
        binary_output = decimal_to_binary(decimal_input)
        hex_output = binary_to_hex(binary_output)

        print('您所輸入的數字', decimal_input, '的二進位表示方法為:', binary_output)
        print('您所輸入的數字', decimal_input, '的十六進位表示方法為:', hex_output)

if __name__ == '__main__':
    main()


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
