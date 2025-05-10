class player():
    XYZ1=[0,0,0]
    SPEED=2
    SIZE=10
    SIZE2=(0,0)
    COLOR=[0,0,0]
    X,Y=800,600
    AREA=150
    HP=20
    HP_MAX=20
    GAUGES=[0,0,0,0]
    GAUGES_MAX=[100,100,100,100]
    GAUGES_COLOR=[(255,255,0),(255,0,255),(0,255,255),(255,255,255)]
    BOX_INF=[5,200,200]
    NO_HIT_TIME=25
    G_A=0.2
    G_SPEED=0
    POWER=6
    BLUESOUL=False
    MYS=False
    MYS_F=False
    FALLING=True
    def __init__(self,xyz,sp,size,color,xy,area):
        self.XYZ1=xyz
        self.SPEED=sp
        self.SIZE=size
        self.COLOR=color
        self.X,self.Y=xy
        self.AREA=area

    def gravity(self):
        if self.BLUESOUL:
            COLOR=[0,0,255]
            if self.MYS:
                self.G_SPEED=0
                self.MYS=False
                self.MYS_F=False
                self.FALLING=True
            if self.XYZ1[1]+self.SIZE2[1]/2<self.BOX_INF[2]:
                self.G_SPEED+=self.G_A
                self.XYZ1[1]+=self.G_SPEED
            if self.XYZ1[1]+self.SIZE2[1]/2>=self.BOX_INF[2]:
                self.XYZ1[1]=self.BOX_INF[2]-self.SIZE2[1]/2
                self.G_SPEED=0
                self.FALLING=False
                self.MYS=False
                self.MYS_F=False
    
    def move_x(self,n):
        if (n<0 and self.XYZ1[0]-self.SIZE2[0]/2<=self.BOX_INF[0]) or (n>=0 and self.XYZ1[0]+self.SIZE2[0]/2>self.BOX_INF[1]-self.BOX_INF[0]):
            pass
        else:
            self.XYZ1[0]+=n*self.SPEED
    
    def move_y(self,n):
        if (n<0 and self.XYZ1[1]-self.SIZE2[1]/2<=self.BOX_INF[0]) or (n>=0 and self.XYZ1[1]+self.SIZE2[1]/2>self.BOX_INF[2]-self.BOX_INF[0]):
            pass
        else:
            if self.FALLING:
                return
            elif self.BLUESOUL and n<0:
                self.XYZ1[1]+=-1*self.POWER
            elif self.BLUESOUL:
                pass
            else:
                self.XYZ1[1]+=n*self.SPEED
        if n<0 and not self.G_SPEED-self.POWER>0:
            self.MYS_F=True
        elif self.G_SPEED-self.POWER>0:
            self.MYS=True
    
    def move_z(self,n):
        self.XYZ1[2]+=n*self.SPEED
