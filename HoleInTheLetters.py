# -*- coding: utf-8 -*-

message = input("Digite a mensagem: ")

total = 0
for n in message:

    if n == "A" or n == "a":
        total = total + 1

    elif n == "B":
        total = total + 2

    elif n == "b":
        total = total + 1
        
    elif n == "D" or n == "d":
        total = total + 1

    elif n == "O" or n == "o":
        total = total + 1

    elif n == "P" or n == "p":
        total = total + 1

    elif n == "Q" or n == "q":
        total = total + 1

    elif n == "R" or n == "r":
        total = total + 1

print(total)
