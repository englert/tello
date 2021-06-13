from djitellopy import tello
import keypress as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())


def get_key_input():
    x, y, z, forog = 0, 0, 0, 0
    speed = 10

    if   kp.get_key("LEFT"):  x =  -speed
    elif kp.get_key("RIGHT"): x =   speed

    elif kp.get_key("UP"):    y =   speed
    elif kp.get_key("DOWN"):  y =  -speed

    elif kp.get_key("w"):     z =   speed
    elif kp.get_key("s"):     z =  -speed

    elif kp.get_key("a"): forog =  -speed
    elif kp.get_key("d"): forog =   speed

    elif kp.get_key("q"): 
        me.land()
        sleep(3)
    elif kp.get_key("e"): 
        me.takeoff()
    return(x, y, z, forog)

while True:
    ##print(kp.get_key("s"))
    ##me.send_rc_control(0,0,0,0)
    k = get_key_input()
    me.send_rc_control( *k)
    sleep(0.05)
