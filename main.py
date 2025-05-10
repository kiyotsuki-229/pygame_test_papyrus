from meta1 import *
from player1 import *
from meta2 import *
from pygame import *
import pygame
import sys
import traceback
import math
import asyncio

def return_long(x1,y1,x2,y2):
    try:
        n1=(x1-x2)**2+(y1-y2)**2
        n2=math.sqrt(n1)
        return n2
    except:
        return 0

def return_size(l1,l2,l3):
    try:
        s1=(l1+l2+l3)/2
        s2=math.sqrt(s1*(s1-l1)*(s1-l2)*(s1-l3))
        return s2
    except:
        return 0
    
def judge_3(l1,l2,l3):
    l1_1=l1**2
    l2_2=l2**2
    l3_3=l3**2
    
    L1=(l2_2+l3_3-l1_1)/(2*l2*l3) if l2 and l3 else 0
    L2=(l1_1+l3_3-l2_2)/(2*l1*l3) if l1 and l3 else 0
    L3=(l2_2+l1_1-l3_3)/(2*l2*l1) if l1 and l2 else 0
    return L1,L2,L3


def play_control(value):
    prk = pygame.key.get_pressed()
    v=0.5 if prk[K_LSHIFT] else 1
    if prk[K_RIGHT]:
        value.move_x(v)
    if prk[K_LEFT]:
        value.move_x(-v)
    if prk[K_UP]:
        value.move_y(-v)
    elif value.MYS_F and not value.FALLING:
        value.MYS=True
    if prk[K_DOWN]:
        value.move_y(v)

def gameover(pl):
    pass

async def main(s1,s2):
    X,Y=640,480
    s2=s1
    x=150
    t1=0
    
    pygame.init()
    pygame.font.init()
    font1=pygame.font.Font('JF-Dot-Shinonome14.ttf',20)
    text1=font1.render('キャラ　Lv 1',True,(255,255,255))
    
    screen3=pygame.display.set_mode((X,Y))
    screen=pygame.Surface((X,Y))
    sc_rect=screen.get_rect(center=(X/2,Y/2))

    screen4=pygame.Surface((X,Y))
    
    
    box1=pygame.Surface(s2.BOX_SIZE)
    clock=pygame.time.Clock()
    BX,BY=box1.get_size()
    
    soul_img=pygame.image.load('soul1.png')
    soul_img=pygame.transform.scale(soul_img,(18,18))
    soul_img2=pygame.image.load('soul2.png')
    soul_img2=pygame.transform.scale(soul_img2,(18,18))
    
    pl=player([BX/2,BY/2,0],4,5,[0,255,0],(X,Y),x)
    pl.SIZE2=soul_img.get_size()
    pl.BOX_INF=[5,s1.BOX_SIZE[0],s1.BOX_SIZE[1]]
    
    runnning=1
    f=0
    while runnning:
        box1=pygame.Surface(s2.BOX_SIZE)
        screen.fill((0,0,0))
        pygame.transform.scale(box1,s2.BOX_SIZE)
        box1.fill((0,0,0))
        s2.action0(f,pl)
        xyz1=s1.camera1(s2.OBJS1,f)
        xyz2=s1.camera1(s2.OBJS2,f)
        xyz1_2=s1.camera1(s2.B_OBJS1,f)
        xyz2_2=s1.camera1(s2.B_OBJS2,f)

        pl.BOX_INF=[5,s2.BOX_SIZE[0],s2.BOX_SIZE[1]]

        for c1 in s2.OBJS1.keys():
            if s2.OBJS1[c1].CS:
                pygame.draw.circle(screen,s2.OBJS1[c1].COLOR,
                                   (xyz1[c1].POINT1.WORLD_XYZ[0],xyz1[c1].POINT1.WORLD_XYZ[1]),xyz1[c1].SIZE)
            n1=(pl.SIZE+xyz1[c1].SIZE)**2
            n2=(pl.XYZ1[0]-xyz1[c1].POINT1.WORLD_XYZ[0])**2
            n3=(pl.XYZ1[1]-xyz1[c1].POINT1.WORLD_XYZ[1])**2
            if n1>=n2+n3 and s2.OBJS1[c1].COL and t1==0:
                pl.HP-=1
                pl.GAUGES[1]+=1
                t1=pl.NO_HIT_TIME
            else:
                pl.GAUGES[3]+=0.001


        for l1 in s2.OBJS2.keys():
            if s2.OBJS2[l1].CS:
                pygame.draw.line(screen,s2.OBJS2[l1].COLOR,(xyz2[l1].POINT1.WORLD_XYZ[0],xyz2[l1].POINT1.WORLD_XYZ[1]),(xyz2[l1].POINT2.WORLD_XYZ[0],xyz2[l1].POINT2.WORLD_XYZ[1]),s2.OBJS2[l1].WIDTH)
            try:
                long1=return_long(xyz2[l1].POINT1.WORLD_XYZ[0],xyz2[l1].POINT1.WORLD_XYZ[1],
                                  xyz2[l1].POINT2.WORLD_XYZ[0],xyz2[l1].POINT2.WORLD_XYZ[1])
                long2=return_long(pl.XYZ1[0],pl.XYZ1[1],xyz2[l1].POINT2.WORLD_XYZ[0],xyz2[l1].POINT2.WORLD_XYZ[1])
                long3=return_long(pl.XYZ1[0],pl.XYZ1[1],xyz2[l1].POINT1.WORLD_XYZ[0],xyz2[l1].POINT1.WORLD_XYZ[1])
                far1=return_size(long1,long2,long3)
                
                far3=judge_3(long1,long2,long3)
                skip1=1
                
                if long1:
                    far2=far1*2/long1
                else:
                    far2=0
                    skip1=0
                    
                if far2<=pl.SIZE and (far3[1]>=0 or long3<=pl.SIZE) and (far3[2]>=0 or long2<=pl.SIZE) and s2.OBJS2[l1].COL and skip1 and t1==0:
                    prk = pygame.key.get_pressed()
                    if s2.OBJS2[l1].COLOR==[0,255,255] and not (prk[K_RIGHT] or prk[K_LEFT] or prk[K_DOWN] or prk[K_UP] or pl.FALLING):
                        pass
                    else:
                        pl.HP-=1
                        pl.GAUGES[1]+=1
                        t1=pl.NO_HIT_TIME
               
                else:
                    pl.GAUGES[3]+=0.001
            except Exception as e:

                t=traceback.format_exc()
                print(t)
                return

        for l1 in s2.OBJS3.keys():
            screen.blit(s2.OBJS3[l1].IMAGE,(s2.OBJS3[l1].XYZ_2.WORLD_XYZ[0]-s2.OBJS3[l1].WIDTH/2,s2.OBJS3[l1].XYZ_2.WORLD_XYZ[1]-s2.OBJS3[l1].HEIGHT/2))

        for c1 in s2.B_OBJS1.keys():
            if s2.B_OBJS1[c1].CS:
                pygame.draw.circle(box1,s2.B_OBJS1[c1].COLOR,
                                   (xyz1_2[c1].POINT1.WORLD_XYZ[0],xyz1_2[c1].POINT1.WORLD_XYZ[1]),xyz1_2[c1].SIZE)
            n1=(pl.SIZE+xyz1_2[c1].SIZE)**2
            n2=(pl.XYZ1[0]-xyz1_2[c1].POINT1.WORLD_XYZ[0])**2
            n3=(pl.XYZ1[1]-xyz1_2[c1].POINT1.WORLD_XYZ[1])**2
            if n1>=n2+n3 and s2.OBJS1[c1].COL and t1==0:
                pl.HP-=1
                pl.GAUGES[1]+=1
                t1=pl.NO_HIT_TIME
            else:
                pl.GAUGES[3]+=0.001


        for l1 in s2.B_OBJS2.keys():
            if s2.B_OBJS2[l1].CS:
                pygame.draw.line(box1,s2.B_OBJS2[l1].COLOR,(xyz2_2[l1].POINT1.WORLD_XYZ[0],xyz2_2[l1].POINT1.WORLD_XYZ[1]),
                                 (xyz2_2[l1].POINT2.WORLD_XYZ[0],xyz2_2[l1].POINT2.WORLD_XYZ[1]),s2.B_OBJS2[l1].WIDTH)
            try:
                long1=return_long(xyz2_2[l1].POINT1.WORLD_XYZ[0],xyz2_2[l1].POINT1.WORLD_XYZ[1],
                                  xyz2_2[l1].POINT2.WORLD_XYZ[0],xyz2_2[l1].POINT2.WORLD_XYZ[1])
                long2=return_long(pl.XYZ1[0],pl.XYZ1[1],xyz2_2[l1].POINT2.WORLD_XYZ[0],xyz2_2[l1].POINT2.WORLD_XYZ[1])
                long3=return_long(pl.XYZ1[0],pl.XYZ1[1],xyz2_2[l1].POINT1.WORLD_XYZ[0],xyz2_2[l1].POINT1.WORLD_XYZ[1])
                far1=return_size(long1,long2,long3)
                
                far3=judge_3(long1,long2,long3)
                skip1=1
                if long1:
                    far2=far1*2/long1
                else:
                    far2=0
                    skip1=0
                    
                if far2<=pl.SIZE and (far3[1]>=0 or long3<=pl.SIZE) and (far3[2]>=0 or long2<=pl.SIZE) and s2.B_OBJS2[l1].COL and skip1 and t1==0:
                    prk = pygame.key.get_pressed()
                    if s2.B_OBJS2[l1].COLOR==[0,255,255] and not (prk[K_RIGHT] or prk[K_LEFT] or prk[K_DOWN] or prk[K_UP] or pl.FALLING):
                        pass
                    else:
                        pl.HP-=1
                        pl.GAUGES[1]+=1
                        t1=pl.NO_HIT_TIME
               
                else:
                    pl.GAUGES[3]+=0.001
            except Exception as e:

                t=traceback.format_exc()
                print(t)
                return

        for l1 in s2.B_OBJS3.keys():
            box1.blit(s2.B_OBJS3[l1].IMAGE,(s2.B_OBJS3[l1].XYZ_2.WORLD_XYZ[0]-s2.B_OBJS3[l1].WIDTH/2,s2.B_OBJS3[l1].XYZ_2.WORLD_XYZ[1]-s2.B_OBJS3[l1].HEIGHT/2))

        if pl.BLUESOUL:
            si=soul_img2
        else:
            si=soul_img

        if t1%5==0 and not t1==0:
            si.set_alpha(128)
        else:
            si.set_alpha(255)

        
        box1.blit(si,(pl.XYZ1[0]-10,pl.XYZ1[1]-10))
        #pygame.draw.circle(box1,pl.COLOR,(pl.XYZ1[0],pl.XYZ1[1]),pl.SIZE)

        screen.blit(text1,(100,390))
        text2=font1.render('{:02}'.format(pl.HP)+'/{}'.format(pl.HP_MAX),True,(255,255,255))
        screen.blit(text2,(350,390))
        

        pl.BLUESOUL=True
        pl.gravity()
        play_control(pl)

        if pl.HP<=0:
            #screen2=pygame.Surface((X,Y), pygame.SRCALPHA, 32)
            #n3=abs(int(math.sin(math.radians(f))*255))
            #screen2.fill((255,0,0,n3))
            #screen.blit(screen2,(0,0))
            gameover(pl)

        hp1=pl.HP_MAX
        hp2=pl.HP
        pygame.draw.line(screen,(159,32,21),(300,400),(300+hp1*2,400),20)
        pygame.draw.line(screen,(255,255,0),(300,400),(300+hp2*2,400),20)
            
        bx1,by1=s2.BOX_XY[0]-s2.BOX_SIZE[0]/2,s2.BOX_XY[1]-s2.BOX_SIZE[1]/2
        screen.blit(box1,(bx1,by1))
        pygame.draw.lines(screen,(255,255,255),1,((bx1,by1),(bx1,by1+s2.BOX_SIZE[1]),(bx1+s2.BOX_SIZE[0],by1+s2.BOX_SIZE[1]),(bx1+s2.BOX_SIZE[0],by1)),5)


        
        wave_amplitude = 10  # 波の高さ
        wave_frequency = 0.05  # 波の周波数
        wave_speed = 0.1  # 波の進行速度
        for y in range(Y):
            offset = int(wave_amplitude * math.sin(wave_frequency * y + f * wave_speed))
            screen4.blit(screen, (offset, y), pygame.Rect(0, y, X, 1))

        #screen6=pygame.transform.rotate(screen4,math.cos(f/30)*30)
        #screen5=screen6.get_rect(center=sc_rect.center)
        #screen3.blit(screen6,screen5)
        screen3.blit(screen,(0,0))
        pygame.display.update()

        
        f+=1
        if t1:
            t1-=1
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        await asyncio.sleep(0)
        clock.tick(30)

if __name__=='__main__':
    try:
        s1=system1()
        s2=menu1()
        asyncio.run(main(s1,s2))
    except Exception as e:
        t=traceback.format_exc()
        print(t)
        pygame.quit()
        sys.exit()
