import pygame
import time
import math
import clips

result_facts = []

def add_isClear(x,y,h,f,v):
    return "(clear (x "+str(x)+") (y "+str(y)+"))"

def add_opened(x,y):
    return "(opened (x "+str(x)+") (y "+str(y)+"))"

def add_val(x,y,v):
    return "(val (x "+str(x)+") (y "+str(y)+") (v "+str(v)+"))"

def add_tile(x,y,h,f,v):
    return "(tile (x "+str(x)+") (y "+str(y)+") (hidden_neigh "+str(h)+") (flag_neigh "+str(f)+") (value "+str(v)+"))"

def add_decrementfn(x,y):
    return "(decrement_fn (x "+str(x)+") (y "+str(y)+"))"

def parse_opened(text):
    x = text[11]
    y = text[17]
    print("Bot membuka: " + x + "," + y)
    return int(x),int(y)

def parse_bomb(text):
    x = text[9]
    y = text[15]
    print("Bot menandai: " + x + "," + y)
    return int(x),int(y)

class isiPapan(object):

    arrIsipapan = [pygame.image.load('design\\square_open.png'),pygame.image.load('design\\square_open_1.png'),pygame.image.load('design\\square_open_2.png'),pygame.image.load('design\\square_open_3.png'),pygame.image.load('design\\square_open_4.png'),pygame.image.load('design\\square_open_bomb.png'),pygame.image.load('design\\square_close.png'),pygame.image.load('design\\square_close_flag.png')]
    
    def __init__(self,status,visibility,x,y,size):
        self.status = status # 5 Bomb, 0-4 Value
        self.visibility = visibility # 0 Hidden, 1 Flagged, 2 Show
        self.size = size
        self.x = x
        self.y = y
        self.hitbox = ((382 + self.x * int(55 * (8/self.size))), (60 + self.y * int(58 * (8/self.size))), int(53 * (8/self.size)), int(56 * (8/self.size))) #area yang bisa diklik

    def setVisibility(self,visibility):
        self.visibility = visibility

    def setStatus(self,status):
        self.status = status

    def draw(self,win):
        size = int(50 * (8/self.size))
        if(self.visibility == 0):
            isiPapan = pygame.transform.scale(self.arrIsipapan[6], (size,size))
            win.blit(isiPapan, ((382 + self.x * int(55 * (8/self.size))), 60 + (self.y * int(58 * (8/self.size)))))
        elif(self.visibility == 1):
            isiPapan = pygame.transform.scale(self.arrIsipapan[7], (size,size))
            win.blit(isiPapan, ((382 + self.x * int(55 * (8/self.size))), 60 + (self.y * int(58 * (8/self.size)))))
        else:
            isiPapan = pygame.transform.scale(self.arrIsipapan[self.status], (size,size))
            win.blit(isiPapan, ((382 + self.x * int(55 * (8/self.size))), 60 + (self.y * int(58 * (8/self.size)))))

class papan(object):
    def __init__(self,size,arBomb):
        self.size = size
        self.amtBomb = len(arBomb)
        self.amtBombtoShow = len(arBomb)
        self.amtFlagtoShow = 0
        self.gameState = 0 #-1 kalah, 0 seri, 1 menang
        self.isi = [[isiPapan(0,0,row,column,size) for row in range(size)] for column in range(size)]
        self.startHitbox = (323, 320, 315, 70)
        self.restartHitbox = (23, 300, 240, 50)

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

    def draw(self,win):
        for x in range(self.size):
            for y in range(self.size):
                self.isi[x][y].draw(win)

    def flag(self,x,y):
        if (self.amtBombtoShow >= 1):
            if self.isi[x][y].visibility == 0:
                self.isi[x][y].visibility = 1
            self.amtBombtoShow -= 1
            self.amtFlagtoShow += 1

    def unflag(self,x,y):
        if self.isi[x][y].visibility == 1:
            self.isi[x][y].visibility = 0
            self.amtBombtoShow += 1
            self.amtFlagtoShow -= 1
        else:
            print("Koordinat tersebut belum ditandai!")

    def open(self,x,y):
        self.isi[x][y].visibility = 2

    def open_result(self,x,y):
        self.isi[x][y].visibility = 2

        result_facts.append(add_opened(x,y))
        
        result_facts.append(add_decrementfn(x-1,y-1))
        result_facts.append(add_decrementfn(x-1,y+1))
        result_facts.append(add_decrementfn(x-1,y))

        result_facts.append(add_decrementfn(x,y-1))
        result_facts.append(add_decrementfn(x,y+1))

        result_facts.append(add_decrementfn(x+1,y-1))
        result_facts.append(add_decrementfn(x+1,y+1))
        result_facts.append(add_decrementfn(x+1,y)) 

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
        font = pygame.font.SysFont('comicsansms', 50)
        pygame.draw.rect(win, (124,252,0), (450,250,270,100),0)
        text = font.render('You Win!', 1, (255, 255, 255))
        win.blit(text, (470, 260))
        pygame.display.update()

    def drawLose(self):
        font = pygame.font.SysFont('comicsansms', 50)
        pygame.draw.rect(win, (178,34,34), (450,250,270,100),0)
        text = font.render('You Lose!', 1, (255, 255, 255))
        win.blit(text, (470, 260))
        pygame.display.update()

    def drawScore(self,win):

        fonts = pygame.font.SysFont('Consolas', 35)
        texts = fonts.render(str(self.amtFlagtoShow), 1, (250, 183, 50))
        win.blit(texts, (149, 201))

        font = pygame.font.SysFont('Consolas', 35)
        text = font.render(str(self.amtBombtoShow), 1, (250, 183, 50))
        win.blit(text, (149, 242))
        
        pygame.display.update()

    def restart(self):
        self.gameState = 0
        self.amtBombtoShow = self.amtBomb
        self.amtFlagtoShow = 0
        for x in range(self.size):
            for y in range(self.size):
                self.isi[x][y].visibility = 0

    def setGameState(self):
        if self.isWin():
            self.gameState = 1
            print("kamu menang")
        elif self.isLose():
            self.gameState = -1

def redrawGameWindow():
    win.blit(bg1, (0,0))
    if gameStatus == 1:
        game.draw(win)
        game.drawScore(win)
    pygame.display.update()

size = 0
amt_bomb = 0
arBombX = []
arBombY = []
arBomb = []
print("Welcome to Minesweeper dengan GUI! ")
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
    env.load('minesweeper6.clp')

    for i in range(size):
        for k in range(size):
            result_facts.append(add_val(i,k,game.isi[i][k].status))
            if ((i == 0) and (k == 0)):
                result_facts.append(add_tile(i,k,3,0,0))
            elif (((i == size-1) and (k == size-1)) or ((i == 0) and (k == size-1)) or ((i == size-1) and (k == 0))):
                result_facts.append(add_tile(i,k,3,0,-1))
            elif ((i == 0) or (k == 0) or (i == size-1) or (k == size-1)):
                result_facts.append(add_tile(i,k,5,0,-1))
            else:
                result_facts.append(add_tile(i,k,8,0,-1))

    game.open_result(0,0)

    for f in result_facts:
        faktas = env.assert_string(f)
    env.run()

    pygame.init()
    win = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Let's Play Minesweeper!") # Judul gamenya

    run = True
    gameStatus = 0 #0 belum mulai, 1 udah mulai, 2 udah selesai
    bg = [pygame.image.load('design\\background.png'),pygame.image.load('design\\background2.png')]
    bg1 = pygame.transform.scale(bg[0], (960, 540))
    win.blit(bg1, (0,0))

    LEFT = 1
    RIGHT = 3
    l = 0
    while run:
        if gameStatus == 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if pygame.Rect(game.startHitbox).collidepoint(event.pos):
                        gameStatus = 1 #biar bisa pindah page
                        bg1 = pygame.transform.scale(bg[1], (960, 540))
                        win.blit(bg1, (0,0))
        elif gameStatus == 1:
            for event in pygame.event.get():
                result_facts.clear()

                for factz in env.facts():
                    factx = str(factz)
                    result_facts.append(factx)

                daftar_fakta_baru = []

                for faktaBaru in result_facts:
                    substringFactx = ""
                    mulaiTarik = False
                    for i in range(len(faktaBaru)):
                        if (faktaBaru[i] == "(" and not mulaiTarik):
                            mulaiTarik = True
                            substringFactx += faktaBaru[i]
                        elif mulaiTarik:
                            substringFactx += faktaBaru[i]
                    daftar_fakta_baru.append(substringFactx)
                
                daftar_aksi = []

                for i in range(len(daftar_fakta_baru)):
                    if(daftar_fakta_baru[i][1]=="o"):
                        daftar_aksi.append(daftar_fakta_baru[i])
                    elif(daftar_fakta_baru[i][1]=="b"):
                        daftar_aksi.append(daftar_fakta_baru[i])
                    else:
                        pass

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #kalau dia mencet sesuatu
                    if(daftar_aksi[l][1]=="o"):
                        x,y = parse_opened(daftar_aksi[l])
                        game.open(x,y)
                    if(daftar_aksi[l][1]=="b"):
                        x,y = parse_bomb(daftar_aksi[l])
                        game.flag(x,y)
                    l += 1

        if event.type == pygame.QUIT:
            run = False

        redrawGameWindow()
       
        
