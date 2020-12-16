import pygame
import clips
import time

#################
## CCLIPS PART ##

result_facts = []

def add_opened(x,y):
    return "(opened (x "+str(x)+") (y "+str(y)+"))"

def add_val(x,y,v):
    return "(val (x "+str(x)+") (y "+str(y)+") (v "+str(v)+"))"

def add_tile(x,y,h,f,v):
    return "(tile (x "+str(x)+") (y "+str(y)+") (hidden_neigh "+str(h)+") (flag_neigh "+str(f)+") (value "+str(v)+"))"

def add_decrementfn(x,y):
    # s = "(decrement_fn (x "+str(x-1)+") (y "+str(y-1)+"))"
    # s +=  "(decrement_fn (x "+str(x-1)+") (y "+str(y)+"))"
    # s += "(decrement_fn (x "+str(x-1)+") (y "+str(y+1)+"))"
    # s += "(decrement_fn (x "+str(x)+") (y "+str(y-1)+"))"
    # s += "(decrement_fn (x "+str(x)+") (y "+str(y+1)+"))"
    # s += "(decrement_fn (x "+str(x+1)+") (y "+str(y-1)+"))"
    # s +=  "(decrement_fn (x "+str(x+1)+") (y "+str(y)+"))"
    # s += "(decrement_fn (x "+str(x+1)+") (y "+str(y+1)+"))"


    return "(decrement_fn (x "+str(x)+") (y "+str(y)+"))"

def parse_opened(text):
    print(text)
    x = text[11]
    y = text[17]
    # print("opened")
    # print("X : " + x)
    # print("Y : " + y)
    # print( )
    return [int(x),int(y)]

def parse_bomb(text):
    print(text)
    x = text[9]
    y = text[15]
    # print("bomb")
    # print("X : " + x)
    # print("Y : " + y)
    # print( )
    return [int(x),int(y)]

    # buka2 pythonnn

    # tambah2in fakta

    # jalanin clips

    # masukin rule clips ke results
    # pass


#################
## CCLIPS PART ##

class isiPapan(object):
    def __init__(self,status,visibility):
        self.status = status # 5 Bomb, 0-4 Value
        self.visibility = visibility # 0 Hidden, 1 Flagged, 2 Show
    
    def setVisibility(self,visibility):
        self.visibility = visibility

    def setStatus(self,status):
        self.status = status

class papan(object):
    def __init__(self,size,arBomb):
        self.size = size
        self.amtBomb = len(arBomb)
        self.amtBombtoShow = len(arBomb)
        self.isi = [[isiPapan(0,0) for row in range(size)] for column in range(size)]

        for num in range(self.amtBomb):
            x = arBomb[num][0]
            y = arBomb[num][1]
            self.isi[x][y].setStatus(5)

        for num in range(self.amtBomb):
            x = arBomb[num][0]
            y = arBomb[num][1]
            if (y >=0 and y <= size-2) and (x >= 0 and x <= size-1):
                if self.isi[x][y+1].status != 5:
                    self.isi[x][y+1].status += 1 # center right

            if (y >=1 and y <= size-1) and (x >= 0 and x <= size-1):
                if self.isi[x][y-1].status != 5:
                    self.isi[x][y-1].status += 1 # center left

            if (y >= 1 and y <= size-1) and (x >= 1 and x <= size-1):
                if self.isi[x-1][y-1].status != 5:
                    self.isi[x-1][y-1].status += 1 # top left

            if (y >= 0 and y <= size-2) and (x >= 1 and x <= size-1):
                if self.isi[x-1][y+1].status != 5:
                    self.isi[x-1][y+1].status += 1 # top right

            if (y >= 0 and y <= size-1) and (x >= 1 and x <= size-1):
                if self.isi[x-1][y].status != 5:
                    self.isi[x-1][y].status += 1 # top center

            if (y >=0 and y <= size-2) and (x >= 0 and x <= size-2):
                if self.isi[x+1][y+1].status != 5:
                    self.isi[x+1][y+1].status += 1 # bottom right

            if (y >= 1 and y <= size-1) and (x >= 0 and x <= size-2):
                if self.isi[x+1][y-1].status != 5:
                    self.isi[x+1][y-1].status += 1 # bottom left

            if (y >= 0 and y <= size-1) and (x >= 0 and x <= size-2):
                if self.isi[x+1][y].status != 5:
                    self.isi[x+1][y].status += 1 # bottom center

    def draw(self):
        print("O-",end = " ")
        for i in range(size):
            print(i,end=" ")
        print()
        for x in range(size):
            print(str(x) + "-",end =" ")
            for y in range(size):
                if (self.isi[x][y].visibility == 2):
                    if (self.isi[x][y].status != 5):
                        print(self.isi[x][y].status, end = " ")
                    else:
                        print('X', end = " ")
                elif (self.isi[x][y].visibility == 1):
                    print('F', end = " ")
                else:
                    print('O', end = " ")
            print()

    def flag(self,x,y):
        if self.isi[x][y].visibility == 0:
            self.isi[x][y].visibility = 1
        self.amtBombtoShow -= 1

    def unflag(self,x,y):
        if self.isi[x][y].visibility == 1:
            self.isi[x][y].visibility = 0
        else:
            print("Koordinat tersebut belum ditandai!")

    def open(self,x,y):
        self.isi[x][y].visibility = 2
        if self.isi[x][y].status == 0:
            if (y >=0 and y <= self.size-2) and (x >= 0 and x <= self.size-1):
                if self.isi[x][y+1].visibility == 0:
                    self.open(x,y+1)
                    # result_facts.append(add_decrementfn(x,y+1))
                    result_facts.append(add_opened(x,y+1))

                    result_facts.append(add_decrementfn(x-1,y))
                    result_facts.append(add_decrementfn(x-1,y+1))
                    result_facts.append(add_decrementfn(x-1,y+2))

                    result_facts.append(add_decrementfn(x,y))
                    
                    result_facts.append(add_decrementfn(x,y+2))

                    result_facts.append(add_decrementfn(x+1,y))
                    result_facts.append(add_decrementfn(x+1,y+1))
                    result_facts.append(add_decrementfn(x+1,y+2))
                    


                    # result_facts.append(add_tile(x,y+1))
            if (y >=1 and y <= self.size-1) and (x >= 0 and x <= self.size-1):
                if self.isi[x][y-1].visibility == 0:
                    self.open(x,y-1)
                    # result_facts.append(add_decrementfn(x,y-1))
                    result_facts.append(add_opened(x,y-1))
                    
                    result_facts.append(add_decrementfn(x-1,y-2))
                    result_facts.append(add_decrementfn(x-1,y-1))
                    result_facts.append(add_decrementfn(x-1,y))

                    result_facts.append(add_decrementfn(x,y-2))
                    
                    result_facts.append(add_decrementfn(x,y))

                    result_facts.append(add_decrementfn(x+1,y-2))
                    result_facts.append(add_decrementfn(x+1,y-1))
                    result_facts.append(add_decrementfn(x+1,y))
                    
            if (y >= 1 and y <= self.size-1) and (x >= 1 and x <= self.size-1):
                if self.isi[x-1][y-1].visibility == 0:
                    self.open(x-1,y-1)
                    # result_facts.append(add_decrementfn(x-1,y-1))
                    result_facts.append(add_opened(x-1,y-1))

                    result_facts.append(add_decrementfn(x-2,y-2))
                    result_facts.append(add_decrementfn(x-2,y-1))
                    result_facts.append(add_decrementfn(x-2,y))

                    result_facts.append(add_decrementfn(x-1,y-2))
                    
                    result_facts.append(add_decrementfn(x-1,y))

                    result_facts.append(add_decrementfn(x-0,y-2))
                    result_facts.append(add_decrementfn(x-0,y-1))
                    result_facts.append(add_decrementfn(x-0,y))
            if (y >= 0 and y <= self.size-2) and (x >= 1 and x <= self.size-1):
                if self.isi[x-1][y+1].visibility == 0:
                    self.open(x-1,y+1)
                    # result_facts.append(add_decrementfn(x-1,y+1))
                    result_facts.append(add_opened(x-1,y+1))

                    result_facts.append(add_decrementfn(x-2,y))
                    result_facts.append(add_decrementfn(x-2,y+1))
                    result_facts.append(add_decrementfn(x-2,y+2))

                    result_facts.append(add_decrementfn(x-1,y))
                    
                    result_facts.append(add_decrementfn(x-1,y+2))

                    result_facts.append(add_decrementfn(x,y))
                    result_facts.append(add_decrementfn(x,y+1))
                    result_facts.append(add_decrementfn(x,y+2))
            if (y >= 0 and y <= self.size-1) and (x >= 1 and x <= self.size-1):
                if self.isi[x-1][y].visibility == 0:
                    self.open(x-1,y)
                    # result_facts.append(add_decrementfn(x-1,y))
                    result_facts.append(add_opened(x-1,y))

                    result_facts.append(add_decrementfn(x-2,y-1))
                    result_facts.append(add_decrementfn(x-2,y))
                    result_facts.append(add_decrementfn(x-2,y+1))

                    result_facts.append(add_decrementfn(x-1,y-1))
                    
                    result_facts.append(add_decrementfn(x-1,y+1))

                    result_facts.append(add_decrementfn(x,y-1))
                    result_facts.append(add_decrementfn(x,y))
                    result_facts.append(add_decrementfn(x,y+1))
            if (y >=0 and y <= self.size-2) and (x >= 0 and x <= self.size-2):
                if self.isi[x+1][y+1].visibility == 0:
                    self.open(x+1,y+1)
                    # result_facts.append(add_decrementfn(x+1,y+1))
                    result_facts.append(add_opened(x+1,y+1))
                    result_facts.append(add_decrementfn(x,y))
                    result_facts.append(add_decrementfn(x,y+1))
                    result_facts.append(add_decrementfn(x,y+2))

                    result_facts.append(add_decrementfn(x+1,y))
                
                    result_facts.append(add_decrementfn(x+1,y+2))

                    result_facts.append(add_decrementfn(x+2,y))
                    result_facts.append(add_decrementfn(x+2,y+1))
                    result_facts.append(add_decrementfn(x+2,y+2))
            if (y >= 1 and y <= self.size-1) and (x >= 0 and x <= self.size-2):
                if self.isi[x+1][y-1].visibility == 0:
                    self.open(x+1,y-1)
                    # result_facts.append(add_decrementfn(x+1,y-1))
                    result_facts.append(add_opened(x+1,y-1))
                    result_facts.append(add_decrementfn(x,y-2))
                    result_facts.append(add_decrementfn(x,y-1))
                    result_facts.append(add_decrementfn(x,y))

                    result_facts.append(add_decrementfn(x+1,y-2))
                    
                    result_facts.append(add_decrementfn(x+1,y))

                    result_facts.append(add_decrementfn(x+2,y-2))
                    result_facts.append(add_decrementfn(x+2,y-1))
                    result_facts.append(add_decrementfn(x+2,y))
            if (y >= 0 and y <= self.size-1) and (x >= 0 and x <= self.size-2):
                if self.isi[x+1][y].visibility == 0:
                    self.open(x+1,y)
                    # result_facts.append(add_decrementfn(x+1,y))
                    result_facts.append(add_opened(x+1,y))
                    result_facts.append(add_decrementfn(x,y-1))
                    result_facts.append(add_decrementfn(x,y))
                    result_facts.append(add_decrementfn(x,y+1))

                    result_facts.append(add_decrementfn(x+1,y-1))
                    result_facts.append(add_decrementfn(x+1,y))
                    result_facts.append(add_decrementfn(x+1,y+1))

                    result_facts.append(add_decrementfn(x+2,y-1))
                    result_facts.append(add_decrementfn(x+2,y))
                    result_facts.append(add_decrementfn(x+2,y+1))

    def isWin(self):
        for x in range(self.size):
            for y in range(self.size):
                if (self.isi[x][y].visibility == 0):
                    return False
        return True

    def isLose(self):
        for x in range(self.size):
            for y in range(self.size):
                if (self.isi[x][y].status == 5 and self.isi[x][y].visibility == 2):
                    return True
        return False

    def drawWin(self):
        print("Congratulations!")

    def drawLose(self):
        print("Oppsie, you lose!")

size = 0
amt_bomb = 0
arBombX = []
arBombY = []
arBomb = []
print("Welcome to Minesweeper tanpa GUI! ")
file = input("Silahkan input file konfigurasi: ")
file = str(file)

#Ukuran Papan
f = open(file)
line = f.readline()
size = int(line)
print(size)
if not (4 <= size <= 10):
    print("Ukuran tidak sesuai!")
    f.close()
    print("input file gagal!")
else:
    #Jumlah Bomb
    line = f.readline()
    amt_bomb = int(line)
    print(amt_bomb)

    #Isi Bomb
    for i in range(amt_bomb):
        line = f.readline()
        x,y = tuple(map(int,line.split(',')))
        arBombX.append(x)
        arBombY.append(y)

    arBomb = list(zip(arBombX,arBombY))
    print(arBomb)

    f.close()

    print("input file success!")
    print()
    print()
    game = papan(size,arBomb)


    env = clips.Environment()
    env.load('minesweeper3.clp')

    x = "(gameover 1)"

    result_facts.append(add_opened(0,0))
    for i in range(size):
        for k in range(size):
            result_facts.append(add_val(i,k,game.isi[i][k].status))
            if (((i == 0) and (k == 0)) or ((i == size-1) and (k == size-1)) or ((i == 0) and (k == size-1)) or ((i == size-1) and (k == 0))):
                result_facts.append(add_tile(i,k,3,0,-1))
            elif ((i == 0) or (k == 0) or (i == size-1) or (k == size-1)):
                result_facts.append(add_tile(i,k,5,0,-1))
            else:
                result_facts.append(add_tile(i,k,8,0,-1))

    game.open(0,0)

    while not game.isWin():
        for f in result_facts:
            print("ini fakta yang mau diassert: " + f)
            faktas = env.assert_string(str(f))
        print()
        print()
        env.run()
        result_facts.clear()

        for factz in env.facts():
            factx = str(factz)
            substringFactx = ""
            mulaiTarik = False
            for i in range(len(factx)):
                if (factx[i] == "(" and not mulaiTarik):
                    mulaiTarik = True
                    substringFactx += factx[i]
                elif mulaiTarik:
                    substringFactx += factx[i]
            # print("ini hasil ekstrrask: " + substringFactx)
            result_facts.append(substringFactx)
        print()
        print()
            
        for i in range(len(result_facts)):
            print("ini hasil result fact: " + result_facts[i])
            if(result_facts[i][1]=="o"):
                # print("ini hasil result factoooo: " + str(result_facts[i]))
                x = parse_opened(result_facts[i])
                game.open(x[0],x[1])
            elif(result_facts[i][1]=="b"):
                # print("ini hasil result factbbbb: " + result_facts[i])
                x = parse_bomb(result_facts[i])
                game.flag(x[0],x[1])
            else:
                pass
        print()
        print()
        