# -*- coding: utf-8 -*-
from pyasn1.compat.octets import null

message = raw_input("Digite a mensagem de até 255 caracteres: ")

if len(message) > 255:
    print("Mensagem maior que 255 caracteres")
else:
    result = ""
    # começa a montar o array
    for n in message:

        if n == "A" or n == "a":
            if result.endswith("2"):
                result += "_"
            result += "2"

        elif n == "B" or n == "b":
            if result.endswith("2"):
                result += "_"
            result += "22"

        elif n == "C" or n == "c":
            if result.endswith("2"):
                result += "_"
            result += "222"

        elif n == "D" or n == "d":
            if result.endswith("3"):
                result += "_"
            result += "3"

        elif n == "E" or n == "e":
            if result.endswith("3"):
                result += "_"
            result += "33"

        elif n == "F" or n == "f":
            if result.endswith("3"):
                result += "_"
            result += "333"

        elif n == "G" or n == "g":
            if result.endswith("4"):
                result += "_"
            result += "4"

        elif n == "H" or n == "h":
            if result.endswith("4"):
                result += "_"
            result += "44"

        elif n == "I" or n == "i":
            if result.endswith("4"):
                result += "_"
            result += "444"

        elif n == "J" or n == "j":
            if result.endswith("5"):
                result += "_"
            result += "5"

        elif n == "K" or n == "k":
            if result.endswith("5"):
                result += "_"
            result += "55"

        elif n == "L" or n == "l":
            if result.endswith("5"):
                result += "_"
            result += "555"

        elif n == "M" or n == "m":
            if result.endswith("6"):
                result += "_"
            result += "6"

        elif n == "N" or n == "n":
            if result.endswith("6"):
                result += "_"
            result += "66"

        elif n == "O" or n == "o":
            if result.endswith("6"):
                result += "_"
            result += "666"

        elif n == "P" or n == "p":
            if result.endswith("7"):
                result += "_"
            result += "7"

        elif n == "Q" or n == "q":
            if result.endswith("7"):
                result += "_"
            result += "77"

        elif n == "R" or n == "r":
            if result.endswith("7"):
                result += "_"
            result += "777"

        elif n == "S" or n == "s":
            if result.endswith("7"):
                result += "_"
            result += "7777"

        elif n == "T" or n == "t":
            if result.endswith("8"):
                result += "_"
            result += "8"

        elif n == "U" or n == "u":
            if result.endswith("8"):
                result += "_"
            result += "88"

        elif n == "V" or n == "v":
            if result.endswith("8"):
                result += "_"
            result += "888"

        elif n == "W" or n == "w":
            if result.endswith("9"):
                result += "_"
            result += "9"

        elif n == "X" or n == "x":
            if result.endswith("9"):
                result += "_"
            result += "99"

        elif n == "Y" or n == "y":
            if result.endswith("9"):
                result += "_"
            result += "999"

        elif n == "Z" or n == "z":
            if result.endswith("9"):
                result += "_"
            result += "9999"

        elif n == " ":
            result += "0"

        print(result)