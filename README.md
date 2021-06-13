# tello
```
#!/bin/bash pip3 install djitellopy
#!/bin/bash pip3 install opencv-python
#!/bin/bash pip3 install numpy
#!/bin/bash pip3 install pygame


DJITellopy:
DJI Tello drone python interfész a hivatalos Tello SDK és Tello EDU SDK használatával:
github.com/damiafuentes/DJITellopy
Example:
```
```python
from djitellopy import Tello
tello = Tello()
tello.connect()
tello.takeoff()
tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)
tello.land()
```



