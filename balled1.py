import functools
import  math
import pygame

class point():
    LOCAL_XYZ=[0,0,0]#相対的回転度
    WORLD_XYZ=[0,0,0]#絶対的座標
    def __init__(self,l,w):
        self.LOCAL_XYZ=l
        self.WORLD_XYZ=w
    def turn_z(self,p2,n):#p2: 回転の中心　n: 回転する角度
        if n<0:
            n=n+360
        A,B,C=self.WORLD_XYZ
        X,Y,Z=p2
        t=math.radians(n)
        c1,s1=math.cos(t),math.sin(t)
        self.WORLD_XYZ[0]=(A-X)*c1+(B-Y)*s1+X
        self.WORLD_XYZ[1]=(-(A-X)*s1+(B-Y)*c1+Y)
        self.LOCAL_XYZ[2]+=n
    def turn_x(self,p2,n):#p2: 回転の中心　n: 回転する角度
        if n<0:
            n=n+360
        A,B,C=self.WORLD_XYZ
        X,Y,Z=p2
        t=math.radians(n)
        c1,s1=math.cos(t),math.sin(t)
        self.WORLD_XYZ[2]=(C-Z)*c1+(B-Y)*s1+Z
        self.WORLD_XYZ[1]=-(C-Z)*s1+(B-Y)*c1+Y
        self.LOCAL_XYZ[0]+=n
    def turn_y(self,p2,n):#p2: 回転の中心　n: 回転する角度
        if n<0:
            n=n+360
        A,B,C=self.WORLD_XYZ
        X,Y,Z=p2
        t=math.radians(n)
        c1,s1=math.cos(t),math.sin(t)
        self.WORLD_XYZ[0]=(A-X)*c1+(C-Z)*s1+X
        self.WORLD_XYZ[2]=-(A-X)*s1+(C-Z)*c1+Z
        self.LOCAL_XYZ[1]+=n
    def move_W(self,b):
        for i in range(3):
            self.WORLD_XYZ[i]+=b[i]
    def move_L(self, p, b):
        # Save the original local rotations
        original_local = self.LOCAL_XYZ[:]

        # Rotate the point to align with the world axes
        self.turn_x(p.WORLD_XYZ, -original_local[0])
        self.turn_y(p.WORLD_XYZ, -original_local[1])
        self.turn_z(p.WORLD_XYZ, -original_local[2])

        # Move the point in the local coordinate system
        self.move_W(b)

        # Rotate the point back to its original orientation
        self.turn_z(p.WORLD_XYZ, original_local[2])
        self.turn_y(p.WORLD_XYZ, original_local[1])
        self.turn_x(p.WORLD_XYZ, original_local[0])

    def move_bigger(self,p,b):
        xyz1=[0,0,0]
        xyz2=[0,0,0]
        for i in range(3):
            xyz1[i]=p[i]-self.WORLD_XYZ[i]
            xyz2[i]=xyz1[i]*b
            self.WORLD_XYZ[i]+=xyz2[i]


class ball():
    CS=True
    COL=True
    SIZE=1
    COLOR=[0,0,0]
    POINT1=None
    def __init__(self,xyz,c,s):
        self.POINT1=xyz
        self.COLOR=c
        self.SIZE=s

class image1():
    CS=True
    COL=True
    ALPHA1=255
    O_WIDTH,O_HEIGHT=[0,0]
    WIDTH,HEIGHT=[0,0]
    XYZ_TURN=[0,0,0]
    XYZ_2=None
    IMAGE=None
    XY_CON=[0,0]
    
    def __init__(self,img,xyz,alp,wid=False,hei=False):
        self.IMAGE=pygame.image.load(img)
        self.IMAGE.set_alpha(self.ALPHA1)
        if (wid and hei):
            self.WIDTH,self.HEIGHT=wid,hei
        else:
            self.WIDTH,self.HEIGHT=self.IMAGE.get_size()
        self.O_WIDTH,self.O_HEIGHT=self.WIDTH,self.HEIGHT
        self.XYZ_2=xyz
        self.HEIGHT*=math.cos(math.radians(self.XYZ_2.LOCAL_XYZ[0]))
        self.WIDTH*=math.cos(math.radians(self.XYZ_2.LOCAL_XYZ[1]))
        self.IMAGE=pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
        self.O_IMAGE=self.IMAGE

    def change_alpha(self,n):
        self.IMAGE.set_alpha(n)
    def turn_img(self,w,h):
        self.XYZ_2.LOCAL_XYZ[0]+=w
        self.XYZ_2.LOCAL_XYZ[1]+=h
        
        self.HEIGHT=self.O_HEIGHT*math.cos(math.radians(self.XYZ_2.LOCAL_XYZ[0]))
        self.WIDTH=self.O_WIDTH*math.cos(math.radians(self.XYZ_2.LOCAL_XYZ[1]))
        
        if self.XY_CON[1]:
            self.HEIGHT*=-1
        if self.XY_CON[0]:
            self.WIDTH*=-1
        
        try:
            self.IMAGE=pygame.transform.flip(self.O_IMAGE,self.XY_CON[0],self.XY_CON[1])
            self.IMAGE=pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
        except:
            if self.HEIGHT<=0:
                self.XY_CON[1]=not self.XY_CON[1]
                self.IMAGE=pygame.transform.flip(self.O_IMAGE,0,self.XY_CON[1])
                self.HEIGHT*=-1
            if self.WIDTH<=0:
                self.XY_CON[0]=not self.XY_CON[0]
                self.IMAGE=pygame.transform.flip(self.O_IMAGE,self.XY_CON[0],0)
                self.WIDTH*=-1
            self.IMAGE=pygame.transform.scale(self.IMAGE,(self.WIDTH,self.HEIGHT))
        #print(self.WIDTH,self.HEIGHT,self.XY_CON)
        


class line1():
    CS=True
    COL=True
    WIDTH=1
    POINT1=None
    POINT2=None
    COLOR=[0,0,0]
    def __init__(self,w,p1,p2,c):
        self.WIDTH=w
        self.POINT1=p1
        self.POINT2=p2
        self.COLOR=c
