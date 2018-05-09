# ENIGMA#

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
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
L_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
L_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
L_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
L_4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
L_5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
L_6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

Ueberliste = [L_1, L_2, L_3, L_4, L_5, L_6]

wsetting = [2,2,2,2,2,2]#[int(input("Walze 1: ")), int(input("Walze 2: ")), int(input("Walze 3: ")), int(input("Walze 4: ")), int(input("Walze 5: ")),
           # int(input("Walze 6: "))]
count = 0
#for setting in wsetting:

    # for i in range(0, setting):
    #     Ueberliste[count].append(Ueberliste[count][0])
    #     Ueberliste[count].pop(0)
    # count = count + 1


class Rollen:
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    normal_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = 0
    enc_dict = {}
    dec_dict = {}

    def clickahead(self):
        self.normal_letters.append(self.normal_letters[0])
        self.normal_letters.pop(0)

    def update_dic(self):
        for letter in self.abc:
            self.enc_dict.update({letter : self.normal_letters[self.num]})
            self.dec_dict.update({self.normal_letters[self.num]: letter})
            self.num = self.num + 1
        self.num = 0
        
    def click(self):
        self.clickahead()
        self.update_dic()
        

    def __init__(self, stellung):

        for i in range(0, stellung):
            self.clickahead()
            self.update_dic()

    def encode(self, let):
        return self.enc_dict[let]

    def decode(self, let):
        return self.dec_dict[let]
    def encodedecodetest(self, let):
        l = self.enc_dict[let]
        l2 = self.dec_dict[l]
        return l, l2


class Controller:
    message = []
    letters = []
    
    def split(self, phrase):
        
        
        for let in phrase:
            
            self.letters.append(let)
        return self.letters
        
    def __init__(self):
        pass



c = Controller()



def control_encode(phrase):
    r0 = Rollen(wsetting[0])
    out_dic = []
    out_string = ""
    x = c.split(phrase)
    for i in x:
        out_dic.append(r0.encode(i))
        r0.click()
    for i in out_dic:
        out_string = out_string + i
    #print(out_string)
    return out_string
    
def control_decode(phrase):
    r0 = Rollen(wsetting[0])
    out_dic = []
    out_string = ""
    x = c.split(phrase)
    for i in x:
        out_dic.append(r0.decode(i))
        r0.click()
    for i in out_dic:
        out_string = out_string + i
    #print(out_string)
    return out_string


out_encode = control_encode("aaaaaaa")
out_decode = control_decode(out_encode)
print(out_encode, out_decode)




#e = Rollen(wsetting[0])
#print(e.encodedecodetest("i"))
#c = Controller()
#print(c.split("abcasdfasöldjfalöksdfjöalksdkgjajskhfaölsgjakldghöaq"))
