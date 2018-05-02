#ENIGMA#
print("         _____ ")
print("	      /  ___  \ ")
print("	    /  /  _  \  \ ")
print("	  /( /( /(_)\ )\ )\ ")
print("	 (  \  \ ___ /  /  )")
print("	 (    \ _____ /    )")
print("	 /(               )\ ")
print("	|  \             /  |")
print("	|    \ _______ /    |")
print("	 \    / \   / \    /")
print("	   \/    | |    \/")
print("	         | |")
print("	         | |")
print("	         |_|")
print("Guten Tag und Willkommen bei Erika&Krupp Enigma Corp")


# LISTEN
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L_5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L_6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Ueberliste = [L_1, L_2, L_3, L_4, L_5, L_6]

wsetting = [ input("Walze 1: "), input("Walze 2: "), input("Walze 3: "), input("Walze 4: "), input("Walze 5: "), input("Walze 6: ")]
count = 0
for setting in wsetting:
    
    for i in range(0, setting):
        Ueberliste[count].append(Ueberliste[count][0])
        Ueberliste[count].pop(0)
     count ++
    
