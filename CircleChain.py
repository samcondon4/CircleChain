#Example implementation of the objects in Circles.py

from Circles import *

c = circle(radius_=20,rgb_=(0,0,0))
cx = circle_chain(initial_=c,num_=25)

def setup():
    size(1000,1000)
    background(0,0,0)
    cx.order1_set(dx_=30,dy_=1,dradius_=1,drgb_=(1,1,1))
    cx.order2_set(d2x_=-2,d2y_=1,d2rgb_=(10,2,20))
    cx.chain_create()

def draw():
    background(0,0,0)
    translate(500,500)
    cx.chain_display()
    cx.lines_draw()
    cx.rgb_sum((1,2,3),(3,4,5))


def keyPressed(chain_):
   cx.chain_randomMove(mvRangeY_=(-20,20),mvRangeX_=(-20,20))
   #cx.chain_dmove() 


