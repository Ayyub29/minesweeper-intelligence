import pygame
import time

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
        print("O- 0 1 2 3 4 5 6 7 8 9")
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
            if (y >=1 and y <= self.size-1) and (x >= 0 and x <= self.size-1):
                if self.isi[x][y-1].visibility == 0:
                    self.open(x,y-1)
            if (y >= 1 and y <= self.size-1) and (x >= 1 and x <= self.size-1):
                if self.isi[x-1][y-1].visibility == 0:
                    self.open(x-1,y-1)
            if (y >= 0 and y <= self.size-2) and (x >= 1 and x <= self.size-1):
                if self.isi[x-1][y+1].visibility == 0:
                    self.open(x-1,y+1)
            if (y >= 0 and y <= self.size-1) and (x >= 1 and x <= self.size-1):
                if self.isi[x-1][y].visibility == 0:
                    self.open(x-1,y)
            if (y >=0 and y <= self.size-2) and (x >= 0 and x <= self.size-2):
                if self.isi[x+1][y+1].visibility == 0:
                    self.open(x+1,y+1)
            if (y >= 1 and y <= self.size-1) and (x >= 0 and x <= self.size-2):
                if self.isi[x+1][y-1].visibility == 0:
                    self.open(x+1,y-1)
            if (y >= 0 and y <= self.size-1) and (x >= 0 and x <= self.size-2):
                if self.isi[x+1][y].visibility == 0:
                    self.open(x+1,y)

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
    run = True
    pil = 0
    score = 0
    while run:
        print("Berikut Papan Minesweeper Anda:")
        print()
        game.draw()
        print()
        print()
        print("Jumlah bomb Tersisa: " + str(game.amtBombtoShow))
        print("Skor Sementara: " + str(score))
        print("Menu:")
        print("1. Buka Koordinat")
        print("2. Tandai Koordinat")
        print("3. Batal Tandai Koordinat")
        pil = int(input("Apa yang akan anda lakukan (1/2/3): "))
        x,y = tuple(map(int,input("Masukkan koordinat (contoh 2,3): ").split(',')))
        if (pil == 1):
            game.open(x,y)
            score += 1
        elif (pil == 2):
            game.flag(x,y)
        elif (pil == 3):
            game.unflag(x,y)
        else:
            print("Masukan tidak Valid!")
        run = not (game.isWin() or game.isLose())
    
    if game.isWin():
        game.drawWin()
    else:
        game.drawLose()

    """
    pygame.init()
    win = pygame.display.set_mode((1280,720)) # window dari pygamenya, ukurannya 1280x720 pixel
    pygame.display.set_caption("Let's Play Minesweeper!") # Judul gamenya

    run = True
    bg = pygame.image.load('bgstart1.png')
    win.blit(bg, (0,0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    """