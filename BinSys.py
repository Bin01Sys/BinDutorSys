def codificar(te):
    if te == "A":
        print("01000001", end="")
    elif te == "B":
        print("01000010", end="")
    elif te == "C":
        print("01000011", end="")
    elif te == "D":
        print("01000100", end="")
    elif te == "E":
        print("01000101", end="")
    elif te == "F":
        print("01000110", end="")
    elif te == "G":
        print("01000111", end="")
    elif te == "H":
        print("01001000", end="")
    elif te == "I":
        print("01001001", end="")
    elif te == "J":
        print("01001010", end="")
    elif te == "K":
        print("01001011", end="")
    elif te == "L":
        print("01001100", end="")
    elif te == "M":
        print("01001101", end="")
    elif te == "N":
        print("01001110", end="")
    elif te == "O":
        print("01001111", end="")
    elif te == "P":
        print("01010000", end="")
    elif te == "Q":
        print("01010001", end="")
    elif te == "R":
        print("01010010", end="")
    elif te == "S":
        print("01010011", end="")
    elif te == "T":
        print("01010100", end="")
    elif te == "U":
        print("01010101", end="")
    elif te == "V":
        print("01010110", end="")
    elif te == "W":
        print("01010111", end="")
    elif te == "X":
        print("01011000", end="")
    elif te == "Y":
        print("01011001", end="")
    elif te == "Z":
        print("01011010", end="")
    elif te == " ":
        print("00100000", end="")
    elif te == "Á":
        print("11000001", end="")
    elif te == "É":
        print("11001001", end="")
    elif te == "Ã":
        print("1100001100001010", end="")
    elif te == "?":
        print("0011111100001010", end="")
    elif te == "!":
        print("00100001", end="")
    elif te == ",":
        print("00101100", end="")
    elif te == ".":
        print("00101110", end="")
    elif te == "@":
        print("01000000", end="")

def decodificar(te):
    deco = {'01000001':'A','01000010':'B','01000011':'C','01000100':'D',
    '01000101':'E','01000110':'F','01000111':'G','01001000':'H','01001001':'I',
    '01001010':'J','01001011':'K','01001100':'L','01001101':'M','01001110':'N',
    '01001111':'O','01010000':'P','01010001':'Q','01010010':'R','01010011':'S',
    '01010100':'T','01010101':'U','01010110':'V','01010111':'W','01011000':'X',
    '01011001':'Y','01011010':'Z','00100000':' ','00111111':'?','00101110':'.'
    ,'00100001':'!','00101101':'-','11000001':'Á','11001001':'É','01000000':'@'
    ,'00101100':','}
    
    a = 0
    b = 8
    nu = len(te)
    while True:
        nu -= 8
        byte = (te)[a:b]
        print(deco[byte], end='')
        a += 8
        b += 8
        if nu == 0:
            break

print("="*50)
print("TRADUTOR BINÁRIO: >20")
print("="*50)

while True:
    eae = int(input("\nDigite  1 Para Codificar ou 2 Para Decodoficar: "))
    if eae == 1:
        nome = str(input("\nDigite alguma frase para ser codificada para binário: ")).upper()
        q = len(nome)
        for c in range(0, q):
            codificar(nome[c])
    elif eae == 2:
        codigo = input('\nDigite o codigo para ser decodificado: ')
        decodificar(codigo.replace(" ", ""))
    elif eae ==3:
        break
    else:
        print("\nOpção invalida!!!")
    print("\n")
    print("="*50)
    print("1=Codificar, 2=Decodificar ou 3=Sair do programa")
    print("="*50)
print("Bye!!")
