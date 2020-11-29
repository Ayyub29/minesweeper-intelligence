import pygame
import time
import math

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
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        elif(self.visibility == 1):
            isiPapan = pygame.transform.scale(self.arrIsipapan[7], (size,size))
            win.blit(isiPapan, ((382 + self.x * int(55 * (8/self.size))), 60 + (self.y * int(58 * (8/self.size)))))
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        else:
            isiPapan = pygame.transform.scale(self.arrIsipapan[self.status], (size,size))
            win.blit(isiPapan, ((382 + self.x * int(55 * (8/self.size))), 60 + (self.y * int(58 * (8/self.size)))))
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

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
        # pygame.draw.rect(win, (255,0,0), self.startHitbox)

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
        # pygame.draw.rect(win, (255,0,0), self.restartHitbox, 2)
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
    if gameStatus == 2:
        game.draw(win)
        game.drawScore(win)
        if game.gameState == 1:
            game.drawWin()
        elif game.gameState == -1:
            game.drawLose()
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

    pygame.init()
    win = pygame.display.set_mode((960, 540))

    game = papan(size,arBomb)
    
    pygame.display.set_caption("Let's Play Minesweeper!") # Judul gamenya

    run = True
    gameStatus = 0 #0 belum mulai, 1 udah mulai, 2 udah selesai
    bg = [pygame.image.load('design\\background.png'),pygame.image.load('design\\background2.png')]
    bg1 = pygame.transform.scale(bg[0], (960, 540))
    win.blit(bg1, (0,0))

    LEFT = 1
    RIGHT = 3

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
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x, y = event.pos
                    if pygame.Rect(game.restartHitbox).collidepoint(event.pos):
                        # print(x,y)
                        game.restart()
                        gameStatus = 1
                    for i in range(game.size):
                        for j in range(game.size):
                            if pygame.Rect(game.isi[i][j].hitbox).collidepoint(event.pos) and game.isi[i][j].visibility == 0:
                                if event.button == LEFT:
                                    # print(x,y)
                                    game.open(i,j)
                                elif event.button == RIGHT:
                                    # print(x,y)
                                    game.flag(i,j)
                            elif pygame.Rect(game.isi[i][j].hitbox).collidepoint(event.pos) and game.isi[i][j].visibility == 1:
                                if event.button == RIGHT:
                                    # print(x,y)
                                    game.unflag(i,j)
            if game.isWin() or game.isLose():
                game.setGameState()
                gameStatus = 2
        else:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x, y = event.pos
                    if pygame.Rect(game.restartHitbox).collidepoint(event.pos):
                        # print(x,y)
                        game.restart()
                        gameStatus = 1

        if event.type == pygame.QUIT:
            run = False

        redrawGameWindow()
       
        
