# -*- coding: UTF-8 -*-
import random

class TestRandom:
    Red_Ball = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    Blue_Ball = [1,2,3,4,5,6,7,8,9,10,11,12]
    Checked_RedBall = []
    Checked_BlueBall = []
    while len(Red_Ball)>29:
        Num = random.choice(Red_Ball)
        Red_Ball.remove(Num)
        Checked_RedBall.append(Num)
    while len(Blue_Ball)>10:
        Num = random.choice(Blue_Ball)
        Blue_Ball.remove(Num)
        Checked_BlueBall.append(Num)
    print(Checked_RedBall,Checked_BlueBall)




