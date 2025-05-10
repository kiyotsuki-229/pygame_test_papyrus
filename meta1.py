from balled1 import *
import math
import pygame
import random

class system1():
    OBJS1={}#球専用
    OBJS2={}#線専用
    OBJS3={}#画像専用
    POINTS={}#ポイントの集合体
    B_OBJS1={}#球専用  ボックス内
    B_OBJS2={}#線専用  ボックス内
    B_OBJS3={}#画像専用  ボックス内
    B_POINTS={}#ポイントの集合体  ボックス内
    BOX_SIZE=[140,140]
    BOX_XY=[320,310]

    def ut_bone(self,p1,p2):
        pass
        #p1_1=point()
    
    def action0(self,f,p):
        if f==0:
            
            pygame.mixer.init(frequency = 22050)
            pygame.mixer.music.load('Bonetrousle.wav')
            pygame.mixer.music.play(-1)
            p1=point([0,0,0],[0,0,0])
            p2=point([0,0,0],[0,140,0])
            l1=line1(5,p1,p2,[0,255,255])
            p3=point([0,0,0],[320,120,0])
            self.B_OBJS2['bone1']=l1
            i1=image1('papyrus1.png',p3,255,400,200)
            self.OBJS3['sanes']=i1
            self.B_OBJS2['bone1'].COL=True
        if f>0:
            self.B_OBJS2['bone1'].POINT1.move_W((3,0,0))
            self.B_OBJS2['bone1'].POINT2.move_W((3,0,0))
            for k in self.B_OBJS2.keys():
                if 'B1_' in k:
                    self.B_OBJS2[k].POINT1.move_W((1,0,0))
                    self.B_OBJS2[k].POINT2.move_W((1,0,0))
            if self.B_OBJS2['bone1'].POINT1.WORLD_XYZ[0]>self.BOX_SIZE[0]:
                self.B_OBJS2['bone1'].POINT1.WORLD_XYZ[0]=0
                self.B_OBJS2['bone1'].POINT2.WORLD_XYZ[0]=0
            if self.BOX_SIZE[0]<=500:
                num1=4
                self.BOX_SIZE[0]+=num1
                p.XYZ1[0]+=num1/2
            
            if f%50==0:
                p1=point([0,0,0],[0,self.BOX_SIZE[1],0])
                p3=point([0,0,0],[0,self.BOX_SIZE[1]-random.randint(0,int(self.BOX_SIZE[1]*(3/5))),0])
                l1=line1(5,p1,p3,[255,255,255])
                self.B_OBJS2['B1_'+str(f)]=l1
                
    
    def action1(self,f):
        if f==0:
            p1=point([10,10,10],[10,10,10])
            b1=ball(p1,[0,0,255],10)
            self.OBJS1['test1']=b1
        if f>0:
            self.OBJS1['test1'].POINT1.move_W([1,0,0])

    
    def action2(self,f):
        if f==0:
            p1=point([100,100,50],[100,100,50])
            b1=ball(p1,[0,255,0],10)
            p2=point([100,100,-50],[100,100,-50])
            b2=ball(p2,[0,255,0],10)
            p3=point([200,100,50],[200,100,50])
            b3=ball(p3,[0,255,0],10)
            p4=point([200,100,-50],[200,100,-50])
            b4=ball(p4,[0,255,0],10)
            p5=point([100,200,50],[100,200,50])
            b5=ball(p5,[0,255,0],10)
            p6=point([100,200,-50],[100,200,-50])
            b6=ball(p6,[0,255,0],10)
            p7=point([200,200,50],[200,200,50])
            b7=ball(p7,[0,255,0],10)
            p8=point([200,200,-50],[200,200,-50])
            b8=ball(p8,[0,255,0],10)
            self.OBJS1['test!1']=b1
            self.OBJS1['test!2']=b2
            self.OBJS1['test!3']=b3
            self.OBJS1['test!4']=b4
            self.OBJS1['test!5']=b5
            self.OBJS1['test!6']=b6
            self.OBJS1['test!7']=b7
            self.OBJS1['test!8']=b8
            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9
        if 0<f:
            for i in range(1,9):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS1['test!'+str(int(i))].POINT1.turn_z(self.POINTS['test_a'].WORLD_XYZ,1)
                self.OBJS1['test!'+str(int(i))].POINT1.turn_x(self.POINTS['test_a'].WORLD_XYZ,1)
        if f>100:
            for i in range(1,9):
                self.OBJS1['test!'+str(int(i))].POINT1.move_W([1,0,0])
            self.POINTS['test_a'].move_W([1,0,0])

    def action4(self,f):
        if f==0:
            p1=point([135,45,135],[100,100,50])
            p2=point([225,135,135],[100,100,-50])
            p3=point([135,315,225],[200,100,50])
            p4=point([225,225,225],[200,100,-50])
            p5=point([45,45,45],[100,200,50])
            p6=point([315,135,45],[100,200,-50])
            p7=point([45,315,315],[200,200,50])
            p8=point([315,225,315],[200,200,-50])

            l1=line1(3,p1,p2,[0,255,255])
            l2=line1(3,p3,p4,[0,255,255])
            l3=line1(3,p5,p6,[0,255,255])
            l4=line1(3,p7,p8,[0,255,255])
            l5=line1(3,p1,p5,[0,255,255])
            l6=line1(3,p2,p6,[0,255,255])
            l7=line1(3,p3,p7,[0,255,255])
            l8=line1(3,p4,p8,[0,255,255])
            l9=line1(3,p1,p3,[0,255,255])
            l10=line1(3,p2,p4,[0,255,255])
            l11=line1(3,p5,p7,[0,255,255])
            l12=line1(3,p6,p8,[0,255,255])

            self.OBJS2['test_l!1']=l1
            self.OBJS2['test_l!2']=l2
            self.OBJS2['test_l!3']=l3
            self.OBJS2['test_l!4']=l4
            self.OBJS2['test_l!5']=l5
            self.OBJS2['test_l!6']=l6
            self.OBJS2['test_l!7']=l7
            self.OBJS2['test_l!8']=l8
            self.OBJS2['test_l!9']=l9
            self.OBJS2['test_l!10']=l10
            self.OBJS2['test_l!11']=l11
            self.OBJS2['test_l!12']=l12

            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9

        if 0<f:
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5)
                #self.OBJS2['test_l!'+str(int(i))].POINT1.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)
                #self.OBJS2['test_l!'+str(int(i))].POINT2.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)
        if f>100:
            for i in range(1,5):#4回の繰り返しで、p1~p8の移動を全て制御できる
                self.OBJS2['test_l!'+str(int(i))].POINT1.move_L(self.POINTS['test_a'],[1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT2.move_L(self.POINTS['test_a'],[1,0,0])
            self.POINTS['test_a'].move_W([1,0,0])

    def action3(self,f):
        if f==0:
            p1=point([100,100,50],[100,100,50])
            p2=point([100,100,-50],[100,100,-50])
            p3=point([200,100,50],[200,100,50])
            p4=point([200,100,-50],[200,100,-50])
            p5=point([100,200,50],[100,200,50])
            p6=point([100,200,-50],[100,200,-50])
            p7=point([200,200,50],[200,200,50])
            p8=point([200,200,-50],[200,200,-50])

            l1=line1(3,p1,p2,[0,255,255])
            l2=line1(3,p3,p4,[0,255,255])
            l3=line1(3,p5,p6,[0,255,255])
            l4=line1(3,p7,p8,[0,255,255])
            l5=line1(3,p1,p5,[0,255,255])
            l6=line1(3,p2,p6,[0,255,255])
            l7=line1(3,p3,p7,[0,255,255])
            l8=line1(3,p4,p8,[0,255,255])
            l9=line1(3,p1,p3,[0,255,255])
            l10=line1(3,p2,p4,[0,255,255])
            l11=line1(3,p5,p7,[0,255,255])
            l12=line1(3,p6,p8,[0,255,255])

            self.OBJS2['test_l!1']=l1
            self.OBJS2['test_l!2']=l2
            self.OBJS2['test_l!3']=l3
            self.OBJS2['test_l!4']=l4
            self.OBJS2['test_l!5']=l5
            self.OBJS2['test_l!6']=l6
            self.OBJS2['test_l!7']=l7
            self.OBJS2['test_l!8']=l8
            self.OBJS2['test_l!9']=l9
            self.OBJS2['test_l!10']=l10
            self.OBJS2['test_l!11']=l11
            self.OBJS2['test_l!12']=l12

            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9

        if 0<f:
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)

    def action_x(self,f):
        if f==0:
            p1=point([100,100,50],[100,100,50])
            p2=point([100,100,-50],[100,100,-50])
            p3=point([200,100,50],[200,100,50])
            p4=point([200,100,-50],[200,100,-50])
            p5=point([100,200,50],[100,200,50])
            p6=point([100,200,-50],[100,200,-50])
            p7=point([200,200,50],[200,200,50])
            p8=point([200,200,-50],[200,200,-50])

            l1=line1(3,p1,p2,[0,255,255])
            l2=line1(3,p3,p4,[0,255,255])
            l3=line1(3,p5,p6,[0,255,255])
            l4=line1(3,p7,p8,[0,255,255])
            l5=line1(3,p1,p5,[0,255,255])
            l6=line1(3,p2,p6,[0,255,255])
            l7=line1(3,p3,p7,[0,255,255])
            l8=line1(3,p4,p8,[0,255,255])
            l9=line1(3,p1,p3,[0,255,255])
            l10=line1(3,p2,p4,[0,255,255])
            l11=line1(3,p5,p7,[0,255,255])
            l12=line1(3,p6,p8,[0,255,255])

            self.OBJS2['test_l!1']=l1
            self.OBJS2['test_l!2']=l2
            self.OBJS2['test_l!3']=l3
            self.OBJS2['test_l!4']=l4
            self.OBJS2['test_l!5']=l5
            self.OBJS2['test_l!6']=l6
            self.OBJS2['test_l!7']=l7
            self.OBJS2['test_l!8']=l8
            self.OBJS2['test_l!9']=l9
            self.OBJS2['test_l!10']=l10
            self.OBJS2['test_l!11']=l11
            self.OBJS2['test_l!12']=l12

            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_z(self.POINTS['test_a'].WORLD_XYZ,10)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_z(self.POINTS['test_a'].WORLD_XYZ,10)
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,10)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,10)

        if 0<f:
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_x(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_x(self.POINTS['test_a'].WORLD_XYZ,0.5)

    def action_y(self,f):
        if f==0:
            p1=point([100,100,50],[100,100,50])
            p2=point([100,100,-50],[100,100,-50])
            p3=point([200,100,50],[200,100,50])
            p4=point([200,100,-50],[200,100,-50])
            p5=point([100,200,50],[100,200,50])
            p6=point([100,200,-50],[100,200,-50])
            p7=point([200,200,50],[200,200,50])
            p8=point([200,200,-50],[200,200,-50])

            l1=line1(3,p1,p2,[0,255,255])
            l2=line1(3,p3,p4,[0,255,255])
            l3=line1(3,p5,p6,[0,255,255])
            l4=line1(3,p7,p8,[0,255,255])
            l5=line1(3,p1,p5,[0,255,255])
            l6=line1(3,p2,p6,[0,255,255])
            l7=line1(3,p3,p7,[0,255,255])
            l8=line1(3,p4,p8,[0,255,255])
            l9=line1(3,p1,p3,[0,255,255])
            l10=line1(3,p2,p4,[0,255,255])
            l11=line1(3,p5,p7,[0,255,255])
            l12=line1(3,p6,p8,[0,255,255])

            self.OBJS2['test_l!1']=l1
            self.OBJS2['test_l!2']=l2
            self.OBJS2['test_l!3']=l3
            self.OBJS2['test_l!4']=l4
            self.OBJS2['test_l!5']=l5
            self.OBJS2['test_l!6']=l6
            self.OBJS2['test_l!7']=l7
            self.OBJS2['test_l!8']=l8
            self.OBJS2['test_l!9']=l9
            self.OBJS2['test_l!10']=l10
            self.OBJS2['test_l!11']=l11
            self.OBJS2['test_l!12']=l12

            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_x(self.POINTS['test_a'].WORLD_XYZ,10)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_x(self.POINTS['test_a'].WORLD_XYZ,10)
        
        if f>0:
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5)

    def action_z(self,f):
        if f==0:
            p1=point([100,100,50],[100,100,50])
            p2=point([100,100,-50],[100,100,-50])
            p3=point([200,100,50],[200,100,50])
            p4=point([200,100,-50],[200,100,-50])
            p5=point([100,200,50],[100,200,50])
            p6=point([100,200,-50],[100,200,-50])
            p7=point([200,200,50],[200,200,50])
            p8=point([200,200,-50],[200,200,-50])

            l1=line1(3,p1,p2,[0,255,255])
            l2=line1(3,p3,p4,[0,255,255])
            l3=line1(3,p5,p6,[0,255,255])
            l4=line1(3,p7,p8,[0,255,255])
            l5=line1(3,p1,p5,[0,255,255])
            l6=line1(3,p2,p6,[0,255,255])
            l7=line1(3,p3,p7,[0,255,255])
            l8=line1(3,p4,p8,[0,255,255])
            l9=line1(3,p1,p3,[0,255,255])
            l10=line1(3,p2,p4,[0,255,255])
            l11=line1(3,p5,p7,[0,255,255])
            l12=line1(3,p6,p8,[0,255,255])

            self.OBJS2['test_l!1']=l1
            self.OBJS2['test_l!2']=l2
            self.OBJS2['test_l!3']=l3
            self.OBJS2['test_l!4']=l4
            self.OBJS2['test_l!5']=l5
            self.OBJS2['test_l!6']=l6
            self.OBJS2['test_l!7']=l7
            self.OBJS2['test_l!8']=l8
            self.OBJS2['test_l!9']=l9
            self.OBJS2['test_l!10']=l10
            self.OBJS2['test_l!11']=l11
            self.OBJS2['test_l!12']=l12

            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,10)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,10)

        if 0<f:
            for i in range(1,5):
                #self.POINTS['test_a'].move_W([1,0,0])
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)

    def action5(self,f):
        if f==0:
            p1=point([100,100,50],[100,100,50])
            p2=point([100,100,-50],[100,100,-50])
            p3=point([200,100,50],[200,100,50])
            p4=point([200,100,-50],[200,100,-50])
            p5=point([100,200,50],[100,200,50])
            p6=point([100,200,-50],[100,200,-50])
            p7=point([200,200,50],[200,200,50])
            p8=point([200,200,-50],[200,200,-50])

            l1=line1(3,p1,p2,[0,255,255])
            l2=line1(3,p3,p4,[0,255,255])
            l3=line1(3,p5,p6,[0,255,255])
            l4=line1(3,p7,p8,[0,255,255])
            l5=line1(3,p1,p5,[0,255,255])
            l6=line1(3,p2,p6,[0,255,255])
            l7=line1(3,p3,p7,[0,255,255])
            l8=line1(3,p4,p8,[0,255,255])
            l9=line1(3,p1,p3,[0,255,255])
            l10=line1(3,p2,p4,[0,255,255])
            l11=line1(3,p5,p7,[0,255,255])
            l12=line1(3,p6,p8,[0,255,255])

            self.OBJS2['test_l!1']=l1
            self.OBJS2['test_l!2']=l2
            self.OBJS2['test_l!3']=l3
            self.OBJS2['test_l!4']=l4
            self.OBJS2['test_l!5']=l5
            self.OBJS2['test_l!6']=l6
            self.OBJS2['test_l!7']=l7
            self.OBJS2['test_l!8']=l8
            self.OBJS2['test_l!9']=l9
            self.OBJS2['test_l!10']=l10
            self.OBJS2['test_l!11']=l11
            self.OBJS2['test_l!12']=l12

            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9
        if f>0:
            for i in range(1,5):
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,-0.5*(f%90-1))
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,-0.5*(f%90-1))
            for i in range(1,5):
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_z(self.POINTS['test_a'].WORLD_XYZ,0.5)
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5*(f%90))
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,0.5*(f%90))
            
    def action6(self,f):
        if f==0:
            p1=point([100,100,50],[100,100,50])
            p2=point([100,100,-50],[100,100,-50])
            p3=point([200,100,50],[200,100,50])
            p4=point([200,100,-50],[200,100,-50])
            p5=point([100,200,50],[100,200,50])
            p6=point([100,200,-50],[100,200,-50])
            p7=point([200,200,50],[200,200,50])
            p8=point([200,200,-50],[200,200,-50])

            l1=line1(3,p1,p2,[0,255,255])
            l2=line1(3,p3,p4,[0,255,255])
            l3=line1(3,p5,p6,[0,255,255])
            l4=line1(3,p7,p8,[0,255,255])
            l5=line1(3,p1,p5,[0,255,255])
            l6=line1(3,p2,p6,[0,255,255])
            l7=line1(3,p3,p7,[0,255,255])
            l8=line1(3,p4,p8,[0,255,255])
            l9=line1(3,p1,p3,[0,255,255])
            l10=line1(3,p2,p4,[0,255,255])
            l11=line1(3,p5,p7,[0,255,255])
            l12=line1(3,p6,p8,[0,255,255])

            self.OBJS2['test_l!1']=l1
            self.OBJS2['test_l!2']=l2
            self.OBJS2['test_l!3']=l3
            self.OBJS2['test_l!4']=l4
            self.OBJS2['test_l!5']=l5
            self.OBJS2['test_l!6']=l6
            self.OBJS2['test_l!7']=l7
            self.OBJS2['test_l!8']=l8
            self.OBJS2['test_l!9']=l9
            self.OBJS2['test_l!10']=l10
            self.OBJS2['test_l!11']=l11
            self.OBJS2['test_l!12']=l12

            p9=point([150,150,0],[150,150,0])
            b9=ball(p9,[255,0,0],5)
            b9.CS=False
            self.OBJS1['T!P']=b9
            self.POINTS['test_a']=p9
            for i in range(1,5):
                self.OBJS2['test_l!'+str(int(i))].POINT1.LOCAL_XYZ=[0,0,0]
                self.OBJS2['test_l!'+str(int(i))].POINT2.LOCAL_XYZ=[0,0,0]

            p10=point([30,40,0],[400,300,0])
            self.OBJS3['test!1']=image1('sword1.png',p10,255)
        if f>0:
            c=math.cos(math.radians(f))
            s=math.sin(math.radians(f))
            for i in range(1,5):
                p1,p2=self.OBJS2['test_l!'+str(int(i))].POINT1.LOCAL_XYZ[1],self.OBJS2['test_l!'+str(int(i))].POINT2.LOCAL_XYZ[1]
                x1,x2=self.OBJS2['test_l!'+str(int(i))].POINT1.LOCAL_XYZ[0],self.OBJS2['test_l!'+str(int(i))].POINT2.LOCAL_XYZ[0]
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,-1*p1)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,-1*p2)
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_x(self.POINTS['test_a'].WORLD_XYZ,-1*x1)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_x(self.POINTS['test_a'].WORLD_XYZ,-1*x2)
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_z(self.POINTS['test_a'].WORLD_XYZ,-1)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_z(self.POINTS['test_a'].WORLD_XYZ,-1)
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_x(self.POINTS['test_a'].WORLD_XYZ,-1+x1)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_x(self.POINTS['test_a'].WORLD_XYZ,-1+x2)
                self.OBJS2['test_l!'+str(int(i))].POINT1.turn_y(self.POINTS['test_a'].WORLD_XYZ,1+p1)
                self.OBJS2['test_l!'+str(int(i))].POINT2.turn_y(self.POINTS['test_a'].WORLD_XYZ,1+p2)
            for i in range(1,5):
                self.OBJS2['test_l!'+str(int(i))].POINT1.move_W([c,s,0])
                self.OBJS2['test_l!'+str(int(i))].POINT2.move_W([c,s,0])
            self.POINTS['test_a'].move_W([c,s,0])
            #self.OBJS3['test!1'].IMAGE.set_alpha(math.sin(math.radians(f%180))*255)
            self.OBJS3['test!1'].turn_img(1,-1)

    def camera1(self,value,f):
        return value
