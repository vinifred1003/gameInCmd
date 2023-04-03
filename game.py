import os
import random
import time
import WConio2
import cursor


os.system('cls')




nave = "■"
naveX = 20
naveY = 23


nave1 = "█"
nave1X = 21
nave1Y = 23


nave2 = "█"
nave2X = 19
nave2Y = 23


nave3 = "A"
nave3X = 21
nave3Y = 24


nave4 = "A"
nave4X = 19
nave4Y = 24


nave5 = "■"
nave5X = 20
nave5Y = 14

nave6 = "■"
nave6X = 20
nave6Y = 14

meteoro = '█'
meteoroX = 12
meteoroY = 3


fogo = "##"
fogoX = 12
fogoY = 2


meteoro1 = '█'  
meteoro1X = 24
meteoro1Y = 3

meteoro2 = '█'
meteoro2X = 36
meteoro2Y = 3


meteoro3 = '█'
meteoro3X = 48
meteoro3Y = 3


star = "▪"

cont = 0


while True:
    WConio2.gotoxy(0, 0)
    print("*" * 50)

    for j in range(25):
      print("*",end="")
      for k in range(38):
          char = " "
                     
          if j==meteoroY and k==meteoroX:
                char = meteoro
            
          if j==meteoro1Y and k==meteoro1X:
                char = meteoro1 
           
          if j==meteoro2Y and k==meteoro2X:
                char = meteoro2
           
          if j==meteoro3Y and k==meteoro3X:
                char = meteoro3
          


          if j==naveY and k==naveX:
                char = nave
          if j==nave1Y and k==nave1X:
                char = nave1
          if j==nave2Y and k==nave2X:
                char = nave2
          if j==nave3Y and k==nave3X:
                char = nave3
          if j==nave4Y and k==nave4X:
                char = nave4
           
          print(char, end="")
      print("*")
    print("*" *42)
    if cont%50 == 0:
        meteoroY+=1
        fogoY+=1
        
    if cont%50 == 0:
        meteoro1Y+=1
        
    if cont%50 == 0:
        meteoro2Y+=1
        
    if cont%50 == 0:
        meteoro3Y+=1
        


    if meteoroY > 25:
        aleatorio = random.randint(0, 38)
        meteoroY = 1
        meteorodY = 1
        fogoY = 0
        meteoroX = aleatorio
        fogox = aleatorio
    if meteoro1Y > 25:
        aleatorio = random.randint(0, 38)
        meteoro1Y = 0
        meteoro1X = aleatorio
    if meteoro2Y > 25:
        aleatorio = random.randint(0, 38)
        meteoro2Y = 0
        meteoro2X = aleatorio
    if meteoro3Y > 25:
        aleatorio = random.randint(0, 38)
        meteoro3Y = 0
        meteoro3X = aleatorio




    if WConio2.kbhit():
      (key, symbol) = WConio2.getch()
      if symbol == 'a':
          naveX-=1
          nave1X-=1
          nave2X-=1
          nave3X-=1
          nave4X-=1
                   

      if symbol == 'd':
        naveX+=1
        nave1X+=1
        nave2X+=1
        nave3X+=1
        nave4X+=1
                   
           
      if symbol == 'w':
                    naveY-=1
                    nave1Y-=1
                    nave2Y-=1
                    nave3Y-=1
                    nave4Y-=1
                   
           
      if symbol == 's':
                    naveY+=1
                    nave1Y+=1
                    nave2Y+=1
                    nave3Y+=1
                    nave4Y+=1
               
    if naveX==meteoroX and naveY==meteoroY or naveX==meteoro1X and naveY==meteoro1Y or naveX==meteoro2X and naveY==meteoro2Y or naveX==meteoro3X and naveY==meteoro3Y or nave1X==meteoroX and nave1Y==meteoroY or nave1X==meteoro1X and nave1Y==meteoro1Y or nave1X==meteoro2X and nave1Y==meteoro2Y or nave1X==meteoro3X and nave1Y==meteoro3Y or nave2X==meteoroX and nave2Y==meteoroY or nave2X==meteoro1X and nave2Y==meteoro1Y or nave2X==meteoro2X and nave2Y==meteoro2Y or nave2X==meteoro3X and nave2Y==meteoro3Y :
        print("GAME OVER")
        break
    cont+=1