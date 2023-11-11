import random

BingoNum=[]
for item in range (1,76):
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

for BingoNum in range (1,16):
    B_list.append(BingoNum)
print ("B ==>", *B_list, sep = " ")

for BingoNum in range (16,31):
    I_list.append(BingoNum)
print ("I ==>", *I_list, sep = " ")

for BingoNum in range (31,46):
    N_list.append(BingoNum)
print ("N ==>", *N_list, sep = " ")

for BingoNum in range (46,61):
    G_list.append(BingoNum)
print ("G ==>", *G_list, sep = " ")

for BingoNum in range (61,76):
    O_list.append(BingoNum)
print ("O ==>", *O_list, sep = " ")

print()

while True:
    draw = input("Você gostaria de escolher um numero aleatório (S/N)")
    draw = draw.capitalize()
    if draw == "S":
            import _random
            BingoNum = []
            for item in range (1,76):
                BingoNum.append(item)

            picknum = random.choice (BingoNum)

            print()



