'''
This is a picture of the Water Pokemon, Oshawott
Created by: Katrina Mei
Date: October 4 2019
Last Modified: October 20 2019
'''

background("#81CDFF")
size(500, 500)

#background grass
fill("#5AFF61")
ellipse(400,400,1300,500)

#background sand
fill("#CE9A4B")
ellipse(450,450,1000,250)


#trees
'''
All of the trunks have the same width and height.
Generally, triangle x points are found by:
    x1=rect x - 20
    x2=rect x + 30
    x3=rect x + 15
Generally, triangle y points are found by:
    y1= rect y + 10
    y2= rect y + 10
    y3= rect y - 40
Some points are adjusted to make trees look better.
'''
#trees left of Oshawott

#tree1
fill("#312316")
rect(70, 160, 15, 40)
fill("#1F7C3A")
triangle(50,170,100,170, 85, 120) 

#tree2
fill("#312316")
rect(110, 140, 15, 40)
fill("#1D4B0B")
triangle(90,155, 145,155, 120, 110)

#tree3
fill("#312316")
rect(130, 155, 15, 40)
fill("#19A541")
triangle(110,175, 150,175, 145, 130) 

#tree4
fill("#312316")
rect(100, 170, 15, 40)
fill("#0E6436")
triangle(70,190, 130,190, 115, 130) 

#trees right of oshawott

#tree5
fill("#312316")
rect(390, 130, 15, 40)
fill("#1D4B0B")
triangle(370,152, 420,152, 405, 110)

#tree6
fill("#312316")
rect(440, 135, 15, 40)
fill("#326C27")
triangle(420,150, 470,150, 455, 110)

#tree7
fill("#312316")
rect(420, 150, 15, 40)
fill("#007C13")
triangle(400,170, 460,170, 430, 120)

#tree8
fill("#312316")
rect(360, 155, 15, 40)
fill("#038308")
triangle(340,180, 390,180, 365, 130)

#tree9
fill("#312316")
rect(385, 170, 15, 40)
fill("#326C27")
triangle(365,190, 415,190, 395, 140)


#mountains
fill("#D4D4D8")

#left mountain
triangle(0,-25,-110,340,110,340)
#snow of the left mountain
noStroke()
fill("#FCFFFD")
triangle(0,-25,-110,90,33,90)

#rightmountain
fill("#D4D4D8")
stroke(1)
triangle(520,-40,420,280,500,280)
#snow of the mountain
noStroke()
fill("#FCFFFD")
triangle(520,-40,482,90,500,90)


#pink flower
stroke(1)
strokeWeight(3)

#flower stem
stroke("#18930D")
strokeCap(PROJECT);
line(380, 265, 380, 245)#find the middle of quad for x values: (390+370)/2=380

#soil
noStroke()
fill("#646464")
quad(370,280,375,265,385,265,390,280)

#petals
fill("#FF7EF0")
ellipse(380,240,9,9)#top petal, x is the same as the center. y=245-5
ellipse(372,245,9,9)#top left petal, x=380-8. y is the same at the center
ellipse(388,245,9,9)#top right petal, x=380+8. y is the same at the center
ellipse(375,250,9,9)#bottom left petal, x=380-5. y=245+5
ellipse(385,250,9,9)#bottom right petal, x=380+5. y=245+5

#center of flower
fill("#D9F540")
ellipse(380,245,7,7) #use end of line point


#purple flower
stroke(1)
strokeWeight(3)

#flower stem
stroke("#18930D")
strokeCap(PROJECT);
line(410, 285, 410, 265)#find the middle of quad for x values: (400+420)/2=410

#soil
noStroke()
fill("#646464")
quad(400,300,405,285,415,285,420,300)

#petals
fill("#CB7EFF")
ellipse(410,260,9,9)#top petal, x is the same as the center. y=265-5
ellipse(402,265,9,9)#top left petal, x=410-8. y is the same at the center
ellipse(418,265,9,9)#top right petal, x=410+8. y is the same at the center
ellipse(405,270,9,9)#bottom left petal, x=410-5. y=265+5
ellipse(415,270,9,9)#bottom right petal, x=410+5. y=265+5

#center of flower
fill("#D9F540")
ellipse(410,265,7,7) #use end of line point


#red flower
stroke(1)
strokeWeight(3)

#flower stem
stroke("#18930D")
strokeCap(PROJECT);
line(110, 240, 110, 220)#find the middle of quad for x values: (100+120)/2=110

#soil
noStroke()
fill("#646464")
quad(100,250,105,240,115,240,120,250)

#petals
fill("#FF7EAB")
ellipse(110,215,9,9)#top petal, x is the same as the center. y=220-5
ellipse(102,220,9,9)#top left petal, x=110-8. y is the same at the center
ellipse(118,220,9,9)#top right petal, x=110+8. y is the same at the center
ellipse(105,225,9,9)#bottom left petal, x=110-5. y=220+5
ellipse(115,225,9,9)#bottom right petal, x=110+5. y=220+5

#center of flower
fill("#D9F540")
ellipse(110,220,7,7) #use end of line point


#texts
#The font must be located in the sketch's "data" directory to load successfully
font=loadFont("Cambria-BoldItalic-48.vlw") 
fill("#030202")
textFont(font,48)
textAlign(CENTER);
text("OSHAWOTT", 250,50)

#sounds Oshawott makes)
textAlign(LEFT);
fill("#F4F5AB")
textSize(10)
text("''Osha-osha''", 70, 100)

#more sounds
textAlign(CENTER);
textSize(10)
text("''Oshawott!!!!!!!!!!!!!''", 420, 100)

#Oshawott use a move command
textAlign(LEFT);
fill("#050505")
textSize(20)
text("''Oshawott use",15, 400)
text("razor shell''",30,430)


#Oshowott The Pokemon Drawing Begins

#ears
stroke(1)
strokeWeight(1)
fill("#0D91FA")

#left ear, points starting from left to right
beginShape();
curveVertex(145, 120);
curveVertex(145, 120);
curveVertex(140, 70);
curveVertex(200, 80);
curveVertex(200, 80);
endShape();

'''
logic to make the ears symmetrical points from left to right.
This is to find distance from center to ears
250-145=105
250-140=110
250-200=50
next line of code add the sum to 250 to maker right ear symmetrical.
'''

#right ear starting from right to left
beginShape();
curveVertex(355, 120); #250+105=355
curveVertex(355, 120);
curveVertex(360, 70); #250+110=360
curveVertex(300, 80);#250+50=300
curveVertex(300, 80);
endShape();

#head
fill("#FFFFFA")
ellipse(250,150,220,180)

#face
#eyes
fill("#000000")

#right eye
ellipse(200,120,30,50)
#right pupil
fill("#FFFFFA")
ellipse(200,110,10,10)

#left eye
fill("#000000")
ellipse(300,120,30,50)
#left pupil
fill("#FFFFFA")
ellipse(300,110,10,10)

#nose
fill("#5A3F25")
ellipse(250,150,50,30)

#mouth
fill("#FC121A")
arc(250, 190, 50, 40, radians(20), radians(200) )
line(227,183,273, 196) #this line is for the top of the mouth, it connects the endpoint of the arc.

#teeth
fill("#FFFFFF")
triangle( 230, 185, 240, 187, 235, 195) #x3=(x1+x2)/2  235=(230+240)/2, y2=y1+2  187=185+2
triangle( 250, 191, 260, 193, 255, 201) #x3=(x1+x2)/2  255=(250+260)/2, y2=y1+2  191=193+2


#freckles
fill("#000000")
ellipse(170,160,5,5)
ellipse(200,160,5,5)
ellipse(185,170,5,5) #x=(170+200)/2

ellipse(300,160,5,5)
ellipse(330,160,5,5)
ellipse(315,170,5,5) #x=(300+330)/2


# left leg
fill("#0D91FA")
beginShape();
curveVertex(180, 420);
curveVertex(180, 420);
curveVertex(160, 470);
curveVertex(210, 470);
curveVertex(230, 430);
curveVertex(230, 430);
endShape();

#left toe
strokeCap(SQUARE);
strokeWeight(2);
line(200, 450, 190, 475)
line(180, 450, 170, 475)


'''
To make right leg symetrical to left,logic:
the x values:
250-230=20 then 250+20=270
250-160=90 then 250+90=340
250-210=40 then 250+40=290
250-230=20 then 250+20=270
the y values are the same as the left leg
'''

#right leg 
beginShape();
curveVertex(270, 430);
curveVertex(270, 430);
curveVertex(290, 470);
curveVertex(340, 470); 
curveVertex(320, 420); 
curveVertex(320, 420);
endShape();

#right toe
strokeCap(SQUARE);
line(300, 450, 310, 475)
line(320, 450, 330, 475)

'''
to make points symetrical use points from left toe to help
line1: x250-200
       x=50
then:  x1=250+50
       x1=300
       
       x2=x1+10
       
line2: x=250-180
       x=70
then:  x1=250+70
       x1=320
       
       x2=x1+10
       
The y points are the same as the left ones.

'''


#tail
#points were made with help of drawing
strokeWeight(1)
beginShape();
curveVertex(320, 380);
curveVertex(320, 380);
curveVertex(420, 320);
curveVertex(480, 380);
curveVertex(340, 400);
curveVertex(340, 400);
endShape();


#left arm
fill("#FFFFFA")
beginShape();
curveVertex(175, 250);
curveVertex(175, 250);
curveVertex(70, 300);
curveVertex(110, 320);
curveVertex(160, 300);
curveVertex(160, 300);
endShape();



#body
#outline of the body
noFill()
stroke(2)
strokeCap(ROUND);

#large body outline
ellipse(250,345,221,211)

#quad part of the body outline
quad(309,240,181,240,149,300,341,300)

#smaller circles of the body outline
ellipse(210,240,67,67)
ellipse(160,220,67,67)
ellipse(300,250,67,67)
ellipse(330,220,67,67)



#filling of the body
noStroke()
fill("#64B6F7")

#quad part of the body
quad(310,240,180,240,150,300,340,300) #this shape was used to fill gap between the ellipse's

#larger body
ellipse(250,345,220,210)

#smaller circles for neck area
ellipse(210,240,65,65)
ellipse(160,220,65,65)
ellipse(300,250,65,65)
ellipse(330,220,65,65)


#right arm 
stroke(1)
fill("#FFFFFA")
beginShape();
curveVertex(334, 250);
curveVertex(334, 250);
curveVertex(230, 300);
curveVertex(270, 320);
curveVertex(335, 290);
curveVertex(335, 290);
endShape();

#end of right arm, this is to end the curve.
arc(331, 271, 40, 40, radians(-90), radians(80)) #y=(250+290)/2, y=270. y was found by finding midpoint of the end of the curve. y was adjusted to make the arm look better. 

#to remove a line from the arc
stroke("#64B6F7")
line(334, 249, 334, 248,) 


#shell
stroke("#0F0F0F")
fill("#F7FC70")

#bottom of shell
triangle(250, 320, 220, 380, 280,380)

#round part of shell
stroke(1)
arc(250, 340, 100, 40, radians(0), radians(180) )
arc(250, 340, 100, 40, radians(180), radians(360) )
noStroke()
triangle(250, 320, 222, 380, 279,380)

#lines of the shell
stroke("#080707")
strokeWeight(2);
noFill()

#right line of shell
beginShape();
curveVertex(230,323);
curveVertex(230,323);
curveVertex(225,331);
curveVertex(222,340);
curveVertex(225,348);
curveVertex(230,357);
curveVertex(230,357);
endShape();

#left line of shell
beginShape();
curveVertex(270,323);
curveVertex(270,323);
curveVertex(275,331);
curveVertex(277,340);
curveVertex(275,348);
curveVertex(270,357);
curveVertex(270,357);
endShape();
