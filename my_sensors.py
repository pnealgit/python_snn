import math
import copy
ANGLES_DX = [1.0, 1.0, 0.0, -1.0, -1.0, -1.0, 0.0, 1.0];
ANGLES_DY = [0.0, 1.0, 1.0, 1.0, 0.0, -1.0, -1.0, -1.0];


def make_binary_sensor_data(my_rover):
    #8(Num_neuron) spots left = 3, mid = 2 , right = 3
    #convert to string for easier reading
    #gotta be an easier way of doing this

    sensor_data = copy.deepcopy(my_rover['Sensor_data'])
    knt = 0
    binary_sensor_data = []
    #get position of rover
    xpos = my_rover['Xpos']
    ypos = my_rover['Ypos']
    j1 = ""
    j2 = ""
    j3 = ""
    for i in range(0,my_rover['Num_sensors']):
        x = sensor_data.pop(0)
        y = sensor_data.pop(0)
        dx = xpos - x
        dy = ypos - y
        d = math.hypot(dx,dy)
        if d > my_rover['Sensor_length']:
            d = my_rover['Sensor_length']
        #from Floreano paper scale is based on reflected light strength

        junkf = 1.0 - (d/my_rover['Sensor_length'])
        #now convert distances....
        if junkf >= 0.80 :
            if i == 0 :
                j1 = "111"
            if i == 1 :
                j2 = "11"
            if i == 2 :
                j3 = "111"
        # end of if on .80

        if junkf >= 0.50 and junkf < 0.80 :
            if i == 0 :
                j1 = "011"
            if i == 1 :
                j2 = "11"
            if i == 2 :
                j3 = "011"

        if junkf >= 0.15 and junkf < 0.50 :

            if i == 0 :
                j1 = "001"
            if i == 1 :
                j2 = "01"
            if i == 2 :
                j3 = "001"

        if junkf < .15 :
            if i == 0 :
                j1 = "000"
            if i == 1 :
                j2 = "00"
            if i == 2 :
                j3 = "000"

    junksd = "".join((j1,j2,j3))
    binary_sensor_data = [int(s) for s in list(junksd)]
    my_rover['Binary_sensor_data'] = binary_sensor_data
    return my_rover

def check_borders(xp,yp,setup):
    # what wall did it hit
    if yp  <= 0 :
        return 1
    if yp >= setup["height"]  :
        return 2
    if xp <= 0 :
        return 3
    if xp >= setup["width"]  :
        return 4

    #do all rectangles
    #ulx ,uly is upper left x,y
    #lrx ,lry is lower rightt x,y
    lrx = 0
    lry = 0
    r = {}

    rects = setup['rectangles']
    num_rects = len(rects);
    #inside the big blue square....dead meat
    for i in range(0,num_rects):
        r = rects[i]
        lrx = r['ulx'] + r['rw']
        lry = r['uly'] + r['rh']
        if ((r['ulx'] <= xp and xp <= lrx  ) and (r['uly'] <= yp and yp  <= lry) ):
            return 99
    #didn't hit anything ... return 0
    return 0;

def get_sensor_data(my_rover,setup) :

    Xpos = 0
    Ypos = 0
    deltax = 0.0
    deltay = 0.0
    Wall = -9
    fdx = 0
    fdy = 0
    dist = 0.0
    knt = 0
    
    my_rover['Sensor_data'] = []

    for isensor in range(0,my_rover['Num_sensors']):
        wall = -9;
        Xpos = my_rover['Xpos']
        Ypos = my_rover['Ypos']
        #angle_index is between 0,7
        angle_index = get_sensor_angle_index(isensor,my_rover);
        deltax = ANGLES_DX[angle_index]
        deltay = ANGLES_DY[angle_index]
        for step in range(0,my_rover['Sensor_length']):
            Xpos += deltax
            Ypos += deltay
            fdx = Xpos - my_rover['Xpos']
            fdy = Ypos - my_rover['Ypos']
            dist = math.hypot(fdx,fdy)
            if dist >= my_rover['Sensor_length'] :
                break

            wall = check_borders(Xpos,Ypos,setup)
            if (wall > 0 ):
               break

        my_rover['Sensor_data'].append(Xpos)
        my_rover['Sensor_data'].append(Ypos)

    return my_rover

def get_sensor_angle_index(i,my_rover):
       
    ai = 99
    if (i == 0) :
      ai = my_rover['Angle_index'] + 1
    if (i == 1) :
      ai = my_rover['Angle_index']
     
    if (i == 2) :
      ai = my_rover['Angle_index'] - 1
     
    
    if (ai > my_rover['Num_angles'] -1) :
       ai = ai % my_rover['Num_angles']
    
    if (ai < 0) :
       ai = my_rover['Num_angles'] - 1

    return ai

