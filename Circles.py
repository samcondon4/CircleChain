#Source for object definitions



#Basic circle class
class circle:

    def __init__(self,x_=0,y_=0,rgb_=(255,255,255),radius_=20,next_=None,fill_=True):
        self.x = x_
        self.y = y_

        self.rgb = rgb_

        self.radius = radius_
        self.next = next_
        self.fil = fill_

    def display(self):
        col = color(self.rgb[0],self.rgb[1],self.rgb[2])
        fill(col)
        ellipse(self.x,self.y,self.radius,self.radius)
        return

#Chain of circles object
class circle_chain:
    
    def __init__(self, initial_, num_, dx_=0, dy_=0, dradius_=0, drgb_=(0,0,0)):
        self.initial = initial_
        self.num = num_

        self.dx = dx_
        self.dy = dy_
        self.d2x = 0
        self.d2y = 0


        self.dradius = dradius_
        self.d2radius = 0

        self.drgb = drgb_
        self.d2rgb = (0,0,0)

    def order1_set(self, dx_=None, dy_=None, dradius_=None, drgb_=None):
        if dx_ != None:
            self.dx = dx_
        if dy_ != None:
            self.dy = dy_
        if dradius_ != None:
            self.dradius = dradius_
        if drgb_ != None:
            self.drgb = drgb_

    def order2_set(self, d2x_=None, d2y_=None, d2radius_=None, d2rgb_=None):
        if d2x_ != None:
            self.d2x = d2x_
        if d2y_ != None:
            self.d2y = d2y_
        if d2radius_ != None:
            self.d2radius = d2radius_
        if d2rgb_ != None:
            self.d2rgb = d2rgb_

    def chain_create(self, circl=None, num=None):
        if num != 0:
            if num == None:
                num = self.num
            if circl == None:
                circl = self.initial
            newX = circl.x + self.dx
            newY = circl.y + self.dy
            newDx = self.dx + self.d2x
            newDy = self.dy + self.d2y

            newRadius = circl.radius + self.dradius
            newDRadius = self.dradius + self.d2radius

            newRGB = self.rgb_sum(circl.rgb,self.drgb)
            newDRGB = self.rgb_sum(self.drgb,self.d2rgb)

            self.order1_set(newDx, newDy, newDRadius, newDRGB)

            circl.next = circle(newX, newY, newRGB, newRadius)

            self.chain_create(circl.next, num - 1)

        return 0

    #Specify a delay between circles displaying for more of a chain effect
    def chain_display(self, circl=None):
        if circl == None:
            circl = self.initial
        if circl.next != None:
            circl.display()
            self.chain_display(circl.next)
        return 0

    #Draw lines displaying connection between circles
    def lines_draw(self,circl=None,col=(255,255,255)):
        if(circl == None):
            circl = self.initial
        if(circl.next != None):
            stroke(color(col[0],col[1],col[2]))
            line(circl.x,circl.y,circl.next.x,circl.next.y)
            self.lines_draw(circl.next)
        return 0

    def chain_randomMove(self, circl=None, mvRangeX_=(-10,10), mvRangeY_=(-10,10)):
        if circl == None:
            circl = self.initial
        if circl.next != None:
            mvX = random(mvRangeX_[0],mvRangeX_[1])
            mvY = random(mvRangeY_[0],mvRangeY_[1])
            circl.x = circl.x + mvX
            circl.y = circl.y + mvY
            self.chain_randomMove(circl.next, mvRangeX_, mvRangeY_)
        return 0

    def rgb_sum(self, rgb1, rgb2):
        r = rgb1[0] + rgb2[0]
        g = rgb1[1] + rgb2[1]
        b = rgb1[2] + rgb2[2]
        return (r,g,b)

