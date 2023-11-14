# Projeto: Jogo de Bingo;
# Jogo desenvolvido por: Márcio Almeida de Souza;
# data de início do projeto 11\2023;
# proposito do projeto: estudo
# email: marciosouzagcm@gmail.com

#importação do pacote Random

import random

#criação de listas com numeração de 1 até 99
BingoNum=[]
for item in range (1,100):
    BingoNum.append(item)

B_list = []
I_list = []
N_list = []
G_list = []
O_list = []
B = []
I = []
N = []
G = []
O = []
print()
print("\t\t\t\t\t Jogo Bingo")
print()

#escolha aleatoria de numeros de 1 ate 20 para lista "B"
for BingoNum in range (1,21):
    B_list.append(BingoNum)
print ("B ==>", *B_list, sep=" ")

#escolha aleatoria de numeros de 21 até 40 para lisra "I"
for BingoNum in range (22,41):
    I_list.append(BingoNum)
print ("I ==>", *I_list, sep=" ")

#escolha aleatoria de numeros de 41 até 60 para lista "N"
for BingoNum in range (42,61):
    N_list.append(BingoNum)
print ("N ==>", *N_list, sep=" ")

#escolha aleatoria de numeros de 61 até 80 para lista "G"
for BingoNum in range (62,81):
    G_list.append(BingoNum)
print ("G ==>", *G_list, sep=" ")

#escolha aleatoria de numeros de 81 até 99 para lista "O"
for BingoNum in range (81,100):
    O_list.append(BingoNum)
print ("O ==>", *O_list, sep=" ")
print()
print()

#laço perguntado se deseja escolher numero aleatório
while True:
    draw = input("Você gostaria de escolher um numero aleatório (S/N)")
    draw = draw.capitalize()
    if draw == "S":

        import random
        BingoNum = []
        for item in range (1,100):
            BingoNum.append(item)

        picknum = random.choice (BingoNum)
        print()

        if picknum>= 1 and picknum <= 20:
            B.append (picknum)
            if picknum in B_list:
                B_list.remove(picknum)
                print("B ==>", *B_list, sep=" ")
                print("I ==>", *I_list, sep=" ")
                print("N ==>", *N_list, sep=" ")
                print("G ==>", *G_list, sep=" ")
                print("O ==>", *O_list, sep=" ")

                print("\nSelecionar numero")
                print("B==>" + str(B)[1:-1], sep=" ")
                print("I==>" + str(I)[1:-1], sep=" ")
                print("N==>" + str(N)[1:-1], sep=" ")
                print("G==>" + str(G)[1:-1], sep=" ")
                print("O==>" + str(O)[1:-1], sep=" ")
                print()
                print("Seleção aleatoria de numeros: B-" +str(picknum))
                print()
                print()

        if picknum>= 21 and picknum <= 40:
            I.append (picknum)
            if picknum in I_list:
                I_list.remove(picknum)
                print("B ==>", *B_list, sep=" ")
                print("I ==>", *I_list, sep=" ")
                print("N ==>", *N_list, sep=" ")
                print("G ==>", *G_list, sep=" ")
                print("O ==>", *O_list, sep=" ")

                print("\nSelecionar numero")
                print("B==>" + str(B)[1:-1], sep=" ")
                print("I==>" + str(I)[1:-1], sep=" ")
                print("N==>" + str(N)[1:-1], sep=" ")
                print("G==>" + str(G)[1:-1], sep=" ")
                print("O==>" + str(O)[1:-1], sep=" ")
                print()
                print("Seleção aleatoria de numeros: I-" +str(picknum))
                print()
                print()

        if picknum>= 41 and picknum <= 60:
            N.append (picknum)
            if picknum in N_list:
                N_list.remove(picknum)
                print("B ==>", *B_list, sep=" ")
                print("I ==>", *I_list, sep=" ")
                print("N ==>", *N_list, sep=" ")
                print("G ==>", *G_list, sep=" ")
                print("O ==>", *O_list, sep=" ")

                print("\nSelecionar numero")
                print("B==>" + str(B)[1:-1], sep=" ")
                print("I==>" + str(I)[1:-1], sep=" ")
                print("N==>" + str(N)[1:-1], sep=" ")
                print("G==>" + str(G)[1:-1], sep=" ")
                print("O==>" + str(O)[1:-1], sep=" ")
                print()
                print("Seleção aleatoria de numeros: N-" +str(picknum))
                print()
                print()

        if picknum>= 61 and picknum <= 80:
            G.append (picknum)
            if picknum in G_list:
                G_list.remove(picknum)
                print("B ==>", *B_list, sep=" ")
                print("I ==>", *I_list, sep=" ")
                print("N ==>", *N_list, sep=" ")
                print("G ==>", *G_list, sep=" ")
                print("O ==>", *O_list, sep=" ")

                print("\nSelecionar numero")
                print("B==>" + str(B)[1:-1], sep=" ")
                print("I==>" + str(I)[1:-1], sep=" ")
                print("N==>" + str(N)[1:-1], sep=" ")
                print("G==>" + str(G)[1:-1], sep=" ")
                print("O==>" + str(O)[1:-1], sep=" ")
                print()
                print("Seleção aleatoria de numeros: G-" +str( picknum))
                print()
                print()

        if picknum>= 81 and picknum <= 99:
            O.append (picknum)
            if picknum in O_list:
                O_list.remove(picknum)
                print("B ==>", *B_list, sep=" ")
                print("I ==>", *I_list, sep=" ")
                print("N ==>", *N_list, sep=" ")
                print("G ==>", *G_list, sep=" ")
                print("O ==>", *O_list, sep=" ")

                print("\nSelecionar numero")
                print("B==>" + str(B)[1:-1], sep=" ")
                print("I==>" + str(I)[1:-1], sep=" ")
                print("N==>" + str(N)[1:-1], sep=" ")
                print("G==>" + str(G)[1:-1], sep=" ")
                print("O==>" + str(O)[1:-1], sep=" ")
                print()
                print("Seleção aleatoria de numeros: O-" +str(picknum))
                print()
                print()

    elif draw=="N":
        print()
        print("Esse Jogo do Bingo acabou")
        print()

        anotherdraw = input ("Você quer definir outro Jogo de Bingo(S/N)?")
        print()

        if anotherdraw =="S":
            print("Jogo Bingo")
            print()
            B_list.clear()
            I_list.clear()
            N_list.clear()
            G_list.clear()
            O_list.clear()
            B.clear()
            I.clear()
            N.clear()
            G.clear()
            O.clear()
            print()
            print()

            for BingoNum in range(1, 21):
                B_list.append(BingoNum)
            print("B ==>", *B_list, sep=" ")

            for BingoNum in range(21, 41):
                I_list.append(BingoNum)
            print("I ==>", *I_list, sep=" ")

            for BingoNum in range(41, 61):
                N_list.append(BingoNum)
            print("N ==>", *N_list, sep=" ")

            for BingoNum in range(61, 81):
                G_list.append(BingoNum)
            print("G ==>", *G_list, sep=" ")

            for BingoNum in range(81, 100):
                O_list.append(BingoNum)
            print("O ==>", *O_list, sep=" ")
            print()
    else:
        print()
        print()
        print("Obrigado por usar este pragrama de Jogo de Bingo")
        break
