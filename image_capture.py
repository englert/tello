from djitellopy import tello
import keypress as kp
import time
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

global img
me.streamon()

def get_key_input():
    x, y, z, forog = 0, 0, 0, 0
    speed = 10

    if   kp.get_key("LEFT"):  x =  -speed
    if kp.get_key("RIGHT"): x =   speed

    if kp.get_key("UP"):    y =   speed
    if kp.get_key("DOWN"):  y =  -speed

    if kp.get_key("w"):     z =   speed
    if kp.get_key("s"):     z =  -speed

    if kp.get_key("a"): forog =  -speed
    if kp.get_key("d"): forog =   speed

    if kp.get_key("q"): 
        me.land()
        time.sleep(3)
    if kp.get_key("e"): 
        me.takeoff()

    if kp.get_key("z"):
        cv2.imwrite(f'images/{time.time()}.jpg', img)  
        time.sleep(0.3)
    return(x, y, z, forog)

while True:
    ##print(kp.get_key("s"))
    ##me.send_rc_control(0,0,0,0)
    k = get_key_input()
    me.send_rc_control( *k)
    import cv2
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
