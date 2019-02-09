import turtle as tr
import time


tr2 = tr.Turtle()

def setup():
    tr.setup(width=1000, height=700, startx=0, starty=0)
    tr.Screen()
    tr.ht()
    tr2.ht()
    tr2.up()
    tr.tracer(0, 0)

def hand(num_hand, num_poi, col_hand, col_poi):
    isstaff = False
    isfan = True
    tr.pensize(9)
    tr.home()
    tr.down()
    tr.color(col_hand)
    tr.left(num_hand)
    tr.forward(130)
    tr.dot(13)
    if isfan == False and isstaff == False:
        poi(num_poi, col_poi)
    elif isfan == True:
        fan(num_poi, col_poi)
    elif isstaff == True:
        staff(num_poi, col_poi)

def staff(number, color):
    tr.pensize(7)
    tr.color(color)
    tr.left(number)
    tr.forward(130)
    tr.dot(20)
    tr.backward(130*2)
    tr.dot(20)
    tr.up()

def fan(number, color):
    tr.pensize(3)
    tr.color(color)
    tr.left(number)

    tr.forward(110)
    tr.dot(15)
    tr.backward(110)

    tr.left(22)
    tr.forward(110)
    tr.dot(15)
    tr.backward(110)

    tr.left(22)
    tr.forward(110)
    tr.dot(15)
    tr.backward(110)

    tr.left(-22*3)
    tr.forward(110)
    tr.dot(15)
    tr.backward(110)

    tr.left(-22)
    tr.forward(110)
    tr.dot(15)

    tr.up()

def poi(number, color):
    tr.down()
    tr.pensize(4)
    tr.color(color)
    tr.left(number)
    tr.dot(10)
    tr.forward(130)

#def shadow():
    #SHADOW
    poi_color_copy = tr.color()
    shadow_color = (poi_color_copy[0][0]+0.3, poi_color_copy[0][1]+0.3, poi_color_copy[0][2]+0.3)
    tr2.color(shadow_color)
    poi_position = tr.pos()
    tr2.setpos(poi_position)
    tr2.dot(18)
    tr.dot(30)
    tr.up()

def poi_mode (number, person, mode, poispeed, rot):
    if mode == 0:       #longarm
        handdir = number + rot
        poidir = 0
    if mode == 1:       #spin
        handdir = number + rot
        poidir = number * poispeed
    if mode == 2:       #antispin
        handdir = number + rot
        poidir = -number * poispeed
    if mode == 3:       #cateye
        handdir = number + rot
        poidir = -number *2+180
    if mode == 4:       #stay
        handdir = 0 + rot
        poidir = number * poispeed


    if person == 0:
        col1 = "black"
        col2 = (0.3, 0.7, 0) #green             #maximum 0.7
    elif person == 1:
        col1 = "orange"
        col2 = (0.3, 0, 0.7) #blue
    elif person == 2:
        col1 = "grey"
        col2 = (0.5, 0.5, 0.5) #yellow
    else:
        col1 = "purple"
        col2 = (0.7, 0, 0.2) #red
    hand(handdir, poidir, col1, col2)

def hand_relation(number, relation, person, firpoimod, secpoimod, firpoispeed, secpoispeed, rotate1, rotate2):
    if relation == 0:    #same sych
        poi_mode(number, person, firpoimod, firpoispeed, rotate1*45)
        poi_mode(number, person, secpoimod, secpoispeed, rotate2*45)
    elif relation == 1:    #same asych
        poi_mode(number, person, firpoimod, firpoispeed, rotate1*45)
        poi_mode(number, person, secpoimod, secpoispeed, rotate2*45+180)
    elif relation == 2:    #opp sych
        poi_mode(-number, person, firpoimod, firpoispeed, rotate1*45)
        poi_mode(number+180, person, secpoimod, secpoispeed, rotate2*45)
    elif relation == 3:    #opp asych
        poi_mode(number, person, firpoimod, firpoispeed, rotate1*45)
        poi_mode(-number, person, secpoimod, secpoispeed, rotate2*45)
    elif relation == 4:    #opp asych
        poi_mode(number, person, firpoimod, firpoispeed, rotate1*45)
        poi_mode(-number, person, secpoimod, secpoispeed, rotate2*45)

def mirror(number, relation, person, firpoimod, secpoimod, firpoispeed, secpoispeed, rotate1, rotate2):
    hand_relation(number, relation, person, firpoimod, secpoimod, firpoispeed, secpoispeed, rotate1, rotate2)
    hand_relation(-number, relation, person+1, firpoimod, secpoimod, firpoispeed, secpoispeed, -rotate1, -rotate2)

def mirror2(number, relation, person, firpoimod, secpoimod, firpoispeed, secpoispeed, rotate1, rotate2):
    hand_relation(number, relation, person, firpoimod, secpoimod, firpoispeed, secpoispeed, rotate1, rotate2)
    hand_relation(-number, relation, person+1, firpoimod, secpoimod, firpoispeed, secpoispeed, -rotate1, -rotate2)
    hand_relation(number, relation, person+2, firpoimod, secpoimod, firpoispeed, secpoispeed, rotate1+2, rotate2+2)
    hand_relation(-number, relation, person+3, firpoimod, secpoimod, firpoispeed, secpoispeed, -rotate1+2, -rotate2+2)

#------------------------------------------------------

def update_position(i):
        #      i, r, p, fpm, spm, fps, sps, rot1, rot2
        mirror(i, 1, 0, 2,   2,   4,   4,   0 ,   0)


        """     W RZEDZIE
        cycles = 1
        if i < 360*0.8:
            mirror2( i*1.25, 1, 0, 0,   0,   4,   4,   0, 0)
        if i > 360*0.8:
            mirror2( i*1.25, 1, 0, 4,   4,   4,   4,   0, 0)
        """

        """     ANTISPIN + ANTYSPIN W MIEJSCU Z PRZESUNIECIEM CO 4
        cycles = 4
        if i < 360*0.75:
            mirror( i, 0, 0, 2,   4,   4,   -4,   0, j*2)
        if i > 360*0.75:
            mirror( i, 0, 0, 2,   2,   4,   4,   0, j*2 + 2)
        """

        #  0-360      0-3             0-1                 0-3                   0-6                   0-8
        # (number,     relation,       person,     1poimod, 2poimod,   1poispeed,  2poispeed,      rotate1, rotate2):
        #   i         0 = same synch  0 = first       0 = longarm           0 = 1:1                   0 = 0
        #             1 = same asynch 1 = second      1 = spin              1 = 1:2                   1 = 45
        #             2 = opp synch   2...            2 = antispin          2 = 1:3                   2 = 2*45
        #             3 = opp asynch  3...            3 = cateye            3 = 1:4                   3 = 45*3
        #                                             4 = stay                                        4....
#------------------------------------------------------

setup()
fps = 50
time_for_cycle = 5.000 #sek

shadow = False
update_view = True
cycles = 1

tim0 = time.clock()
dtim = 0.0

tick = 1.000/fps
while True:

    """
    while dtim > time_step:
        #licz_krok_fizyki(time_step)
        dtim -= time_step
        update_view = True
    """

    tim1 = time.clock()
    dtim = tim1-tim0
    tim0 = tim1
    print(dtim)
    print(tick)
    print(tick*fps)
    print("               ")
    if tick - (dtim-time_for_cycle)/(fps*time_for_cycle) > 0:
        tick -= (dtim-time_for_cycle)/(fps*time_for_cycle)
    else:
        tick = 0

    for i in range(int(time_for_cycle*fps)):

        if shadow == False:
            tr2.clear()

        tr.clear()
        update_position(int(i*(360/(time_for_cycle*fps))))
        tr.update()

        time.sleep(tick)
