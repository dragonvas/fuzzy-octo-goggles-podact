e=33
ee=33

q=0
w=200
eee=800
r=100

t=200
yy=0
u=20
i=150

o=350
p=0
a=200
s=10

d=420
f=10
g=10
h=90
j=0

k=700
l=400
z=20
xx=100

c=700
v=200
b=100
n=200

m=700
qq=500
ww=100
eeee=150

rr=800
tt=780
yyy=200
uu=20
ii=0
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter): 
    testX = cx
    testY = cy
    if cx < rx:
        testX = rx
    elif cx > rx+rw:
        testX = rx+rw
    if cy < ry:
        testY = ry
    elif cy > ry+rh:
        testY = ry+rh
    distance = dist(cx,cy,testX,testY)
    if distance <= diameter/2:
        return True
    else:
        return False
def setup():
    size(1000,800)
def draw():
    global e,ee,j,g,h,f,ii,tt
    background(123,234,0)
    j=j+1
    ii=ii+1
    r1 = collideRectCircle(q,w,eee,r, e, ee, 30)
    r2 = collideRectCircle(0,0,1000,2, e, ee, 30)
    r3 = collideRectCircle(0,0,2,1000, e, ee, 30)
    r4 = collideRectCircle(0,798,1000,2, e, ee, 30)
    r5 = collideRectCircle(1000,0,2,1000, e, ee, 30)
    r6 = collideRectCircle(t,yy,u,i, e, ee, 30)
    r7 = collideRectCircle(o,p,a,s, e, ee, 30)
    r8 = collideRectCircle(o,p+100,a,s, e, ee, 30)
    r9 = collideRectCircle(d,f,g,h, e, ee, 30)
    r10 = collideRectCircle(k,l,z,xx, e, ee, 30)
    r11 = collideRectCircle(c,v,b,n, e, ee, 30)
    r12 = collideRectCircle(m,qq,ww,eeee, e, ee, 30)
    r13 = collideRectCircle(k,l+250,z,xx, e, ee, 30)
    r14 = collideRectCircle(rr,tt,yyy,uu, e, ee, 30)
    rect(q,w,eee,r)
    rect(t,yy,u,i)
    rect(o,p,a,s)
    rect(o,p+100,a,s)
    rect(d,f,g,h)
    rect(c,v,b,n)
    rect(k,l,z,xx)
    rect(m,qq,ww,eeee)
    rect(k,l+250,z,xx)
    rect(rr,tt,yyy,uu)
    ellipse(e, ee, 30, 30)
    colide = r1 or r2 or r3 or r4 or r5 or r6 or r7 or r8 or r9 or r10 or r11 or r12 or r13 or r14
    if colide == True:
        e=33
        ee=33
    if j > 150:
        f=110
    if j > 300:
        f=10
        j=0
    if ii > 0:
        tt=tt-3
    if ii > 312:
        tt=780
        ii=0
    if keyPressed:
        if keyCode == UP:
            ee=ee-3
        if keyCode == DOWN:
            ee=ee+3
        if keyCode == LEFT:
            e=e-3
        if keyCode == RIGHT:
            e=e+3
