# -*- coding: utf-8 -*-
from pyasn1.compat.octets import null

message = raw_input("Digite a mensagem de até 255 caracteres: ")

if len(message) > 255:
    print("Mensagem maior que 255 caracteres")
else:
    result = []
    # começa a montar o array
    for n in range(len(message)):

        if message[n] == "A" or message[n] == "a":
            result.append(2)
            if message[n+1] == null:
                break;

            if message[n+1] == "B" or message[n+1] == "b" or message[n+1] == "C" or message[n+1] == "c":
                result.append("_")

        elif n == "B" or n == "b":
            result.append(22)
            if n.next() == "A" or n.next() == "a" or n.next() == "C" or n.next() == "c":
                result.append("_")

        elif n == "C" or n == "c":
            result.append(222)
            if n.next() == "B" or n.next() == "b" or n.next() == "A" or n.next() == "a":
                result.append("_")

        elif n == "D" or n == "d":
            result.append(3)

        elif n == "E" or n == "e":
            result.append(33)

        elif n == "F" or n == "f":
            result.append(333)

        elif n == "G" or n == "g":
            result.append(4)

        elif n == "H" or n == "h":
            result.append(44)

        elif n == "I" or n == "i":
            result.append(444)

        elif n == "J" or n == "j":
            result.append(5)

        elif n == "K" or n == "k":
            result.append(55)

        elif n == "L" or n == "l":
            result.append(555)

        elif n == "M" or n == "m":
            result.append(6)

        elif n == "N" or n == "n":
            result.append(66)

        elif n == "O" or n == "o":
            result.append(666)

        elif n == "P" or n == "p":
            result.append(7)

        elif n == "Q" or n == "q":
            result.append(77)

        elif n == "R" or n == "r":
            result.append(777)

        elif n == "S" or n == "s":
            result.append(7777)

        elif n == "T" or n == "t":
            result.append(8)

        elif n == "U" or n == "u":
            result.append(88)

        elif n == "V" or n == "v":
            result.append(888)

        elif n == "W" or n == "w":
            result.append(9)

        elif n == "X" or n == "x":
            result.append(99)

        elif n == "Y" or n == "y":
            result.append(999)

        elif n == "Z" or n == "z":
            result.append(9999)

        elif n == " ":
            result.append(0)

        print(result)