from balled1 import *
import math

class menu1():
    OBJS1={}#球専用
    OBJS2={}#線専用
    OBJS3={}#画像専用
    POINTS={}
    def action1(self,f):
        if f==0:
            p1=point([0,0,0],[600,100,200])
            p2=point([0,0,0],[600,100,-200])
            p3=point([0,0,0],[200,100,200])
            p4=point([0,0,0],[200,100,-200])
            p5=point([0,0,0],[600,500,200])
            p6=point([0,0,0],[600,500,-200])
            p7=point([0,0,0],[200,500,200])
            p8=point([0,0,0],[200,500,-200])
            self.POINTS['test!1']=p1
            self.POINTS['test!2']=p2
            self.POINTS['test!3']=p3
            self.POINTS['test!4']=p4
            self.POINTS['test!5']=p5
            self.POINTS['test!6']=p6
            self.POINTS['test!7']=p7
            self.POINTS['test!8']=p8
            p9=point([0,0,0],[400,300,0])
            self.POINTS['test_a']=p9
            l1=line1(10,p1,p2,[0,255,255])
            l2=line1(10,p3,p4,[0,255,255])
            l3=line1(10,p5,p6,[0,255,255])
            l4=line1(10,p7,p8,[0,255,255])
            l5=line1(10,p1,p5,[0,255,255])
            l6=line1(10,p2,p6,[0,255,255])
            l7=line1(10,p3,p7,[0,255,255])
            l8=line1(10,p4,p8,[0,255,255])
            l9=line1(10,p1,p3,[0,255,255])
            l10=line1(10,p2,p4,[0,255,255])
            l11=line1(10,p5,p7,[0,255,255])
            l12=line1(10,p6,p8,[0,255,255])

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
        
        if f>0:
            c=math.cos(math.radians(f))
            s=math.sin(math.radians(f))
            for i in range(1,9):
                p0,p1=self.POINTS['test!'+str(int(i))].LOCAL_XYZ[0],self.POINTS['test!'+str(int(i))].LOCAL_XYZ[1]
                self.POINTS['test!'+str(int(i))].turn_y(self.POINTS['test_a'].WORLD_XYZ,-1*p1)
                self.POINTS['test!'+str(int(i))].turn_x(self.POINTS['test_a'].WORLD_XYZ,c)
                self.POINTS['test!'+str(int(i))].turn_y(self.POINTS['test_a'].WORLD_XYZ,2+p1)

    def action2(self,f):
        if f==0:
            p1=point([0,0,0],[600,100,200])
            p2=point([0,0,0],[600,100,-200])
            p3=point([0,0,0],[200,100,200])
            p4=point([0,0,0],[200,100,-200])
            p5=point([0,0,0],[600,500,200])
            p6=point([0,0,0],[600,500,-200])
            p7=point([0,0,0],[200,500,200])
            p8=point([0,0,0],[200,500,-200])
            self.POINTS['test!1']=p1
            self.POINTS['test!2']=p2
            self.POINTS['test!3']=p3
            self.POINTS['test!4']=p4
            self.POINTS['test!5']=p5
            self.POINTS['test!6']=p6
            self.POINTS['test!7']=p7
            self.POINTS['test!8']=p8
            p9=point([0,0,0],[400,300,0])
            self.POINTS['test_a']=p9
            l1=line1(10,p1,p2,[0,255,255])
            l2=line1(10,p3,p4,[0,255,255])
            l3=line1(10,p5,p6,[0,255,255])
            l4=line1(10,p7,p8,[0,255,255])
            l5=line1(10,p1,p5,[0,255,255])
            l6=line1(10,p2,p6,[0,255,255])
            l7=line1(10,p3,p7,[0,255,255])
            l8=line1(10,p4,p8,[0,255,255])
            l9=line1(10,p1,p3,[0,255,255])
            l10=line1(10,p2,p4,[0,255,255])
            l11=line1(10,p5,p7,[0,255,255])
            l12=line1(10,p6,p8,[0,255,255])

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
        
        if f>0:
            c=math.cos(math.radians(f))
            s=math.sin(math.radians(f))
            for i in range(1,9):
                p0,p1=self.POINTS['test!'+str(int(i))].LOCAL_XYZ[0],self.POINTS['test!'+str(int(i))].LOCAL_XYZ[1]
                self.POINTS['test!'+str(int(i))].turn_y(self.POINTS['test_a'].WORLD_XYZ,-1*p1)
                self.POINTS['test!'+str(int(i))].turn_x(self.POINTS['test_a'].WORLD_XYZ,1)
                self.POINTS['test!'+str(int(i))].turn_y(self.POINTS['test_a'].WORLD_XYZ,1+p1)

        if f>200:
            for i in range(1,9):
                self.POINTS['test!'+str(int(i))].move_bigger(self.POINTS['test_a'].WORLD_XYZ,0.1)
                
        if f>250:
            self.OBJS2.clear()

    def action3(self,f):
        if f==0:
            point1=[400,300,0]
            n1=180
            p1=point([0,0,0],[point1[0]+n1,point1[1]-n1,n1])
            p2=point([0,0,0],[point1[0]+n1,point1[1]-n1,-n1])
            p3=point([0,0,0],[point1[0]-n1,point1[1]-n1,n1])
            p4=point([0,0,0],[point1[0]-n1,point1[1]-n1,-n1])
            p5=point([0,0,0],[point1[0]+n1,point1[1]+n1,n1])
            p6=point([0,0,0],[point1[0]+n1,point1[1]+n1,-n1])
            p7=point([0,0,0],[point1[0]-n1,point1[1]+n1,n1])
            p8=point([0,0,0],[point1[0]-n1,point1[1]+n1,-n1])
            self.POINTS['test!1']=p1
            self.POINTS['test!2']=p2
            self.POINTS['test!3']=p3
            self.POINTS['test!4']=p4
            self.POINTS['test!5']=p5
            self.POINTS['test!6']=p6
            self.POINTS['test!7']=p7
            self.POINTS['test!8']=p8
            p9=point([0,0,0],point1)
            self.POINTS['test_a']=p9
            l1=line1(10,p1,p2,[0,255,255])
            l2=line1(10,p3,p4,[0,255,255])
            l3=line1(10,p5,p6,[0,255,255])
            l4=line1(10,p7,p8,[0,255,255])
            l5=line1(10,p1,p5,[0,255,255])
            l6=line1(10,p2,p6,[0,255,255])
            l7=line1(10,p3,p7,[0,255,255])
            l8=line1(10,p4,p8,[0,255,255])
            l9=line1(10,p1,p3,[0,255,255])
            l10=line1(10,p2,p4,[0,255,255])
            l11=line1(10,p5,p7,[0,255,255])
            l12=line1(10,p6,p8,[0,255,255])

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

            n=1/math.sqrt(3)
            for i in range(1,9):
                self.POINTS['test!'+str(int(i))].turn_y(self.POINTS['test_a'].WORLD_XYZ,45)
                self.POINTS['test!'+str(int(i))].turn_x(self.POINTS['test_a'].WORLD_XYZ,math.degrees(math.asin(n)))

        if f>0:
            for i in range(1,9):
                self.POINTS['test!'+str(int(i))].turn_z(self.POINTS['test_a'].WORLD_XYZ,1)

        if f>200:
            for i in range(1,9):
                self.POINTS['test!'+str(int(i))].move_bigger(self.POINTS['test_a'].WORLD_XYZ,0.1)

class __system1():
    OBJS1={}#球専用
    OBJS2={}#線専用
    OBJS3={}#画像専用
    POINTS={}
