import asyncio
import websockets
import json
import random
import math
import copy
import time
import my_state
import my_brains
import my_sensors

setup = {}
name = "red_stuff"
color = "red"
#
NUM_BRAINS = 10;

my_rover = {}

my_position_msg = "";

def reset_food(setup):
    
    for k in range(0,len(setup['rectangles'])):
            if setup['rectangles'][k]['type'] == 2 :
                setup['rectangles'][k]['eaten'] = 0

def think(brain,my_rover,setup) :
        #In most cases , the sensor_data_vector will be all zeros.
        #so add some bias to make something happen.
        #
        my_rover = my_sensors.make_binary_sensor_data(my_rover,setup)
        #print("THINK BINARY SENSOR_DATA IS: ",my_rover['Binary_sensor_data'])
        NUM_NEURONS = brain['Num_neurons']
        THRES = 3

        #throw in some noise if the sensors sense nothing...Just vast
        #empty space....

        knt = 0;
        for ik in range(0,NUM_NEURONS) :
            knt = knt + my_rover['Binary_sensor_data'][ik]

        if knt <= 0 :
            ridx = random.randrange(0, NUM_NEURONS)
            my_rover['Binary_sensor_data'][ridx] = 1

        leaking_constant = 1
        temp_outps = [0] * NUM_NEURONS
        inps = copy.deepcopy(my_rover['Binary_sensor_data'])  # need deep copy here ?

        memb = [0]*NUM_NEURONS
 
        outps = [0]*NUM_NEURONS
        fire_knt = [0]*NUM_NEURONS
        settling_time = 20; #loop through settling_time times

        for _epoch in range(0,settling_time) :
            for nindex in range(0,NUM_NEURONS):
                memb[nindex] = 0;
                if outps[nindex] == 0 :
                    #not in refactory state
                    for ilink in range(0,NUM_NEURONS):
                        memb[nindex] += inps[nindex] * brain['iconn'][nindex][ilink];
                    #count from other neurons with positive or negative
                    for ilink in range(0,NUM_NEURONS) :
                        stuff = outps[nindex]  \
                        * brain['nconn'][nindex][ilink] \
                        * brain['xsign'][ilink] 

                        memb[nindex] += stuff
                        if memb[nindex] < 0:
                            memb[nindex] = 0

                    #end of loop on ilink
                #end of not refactory
                #fire or not !
                r = random.randrange(-2, 3);
                if memb[nindex] >= (THRES + r) :
                    temp_outps[nindex] = 1
                    memb[nindex] = 0
                else :
                    temp_outps[nindex] = 0
 
                #leakage
                if memb[nindex] >= leaking_constant :
                    memb[nindex] -= leaking_constant
            #end of pass through all neurons

            #fire_knt is used to choose what sensor to go with
            for k in range(0,4):
                fire_knt[0] += temp_outps[k];
            for k in range(4,8):
                fire_knt[1] += temp_outps[k];
            for k in range(8,12):
                fire_knt[2] += temp_outps[k];


            #save outps for refactory
            outps = copy.deepcopy(temp_outps)
            temp_outps = [0] * NUM_NEURONS
        #end of settling_time loop

        min_index = 1; #go straight if nothing happens;
        min_value = 99;

        #choose a direction based on sensor.
        for i in range(0,my_rover['Num_sensors']):
            if fire_knt[i] <= min_value :
                min_value = fire_knt[i]
                min_index = i

            fire_knt[i] = 0

        new_angle_index = my_rover['Angle_index']
        if min_index == 0 :
            new_angle_index = new_angle_index + 1
            if new_angle_index > my_rover['Num_angles'] - 1 :
                new_angle_index = 0

        if min_index == 2 :
            if new_angle_index > 0 :
                new_angle_index = new_angle_index - 1
            else :
                new_angle_index = my_rover['Num_angles'] - 1

        #end of if on minindex 2
        #print("INPS ",inps," angle index ",new_angle_index)
        if new_angle_index == my_rover['Angle_index'] :
            brain['Fitness'] += 1.0

        my_rover['Old_angle_index'] = my_rover['Angle_index']
        my_rover['Angle_index'] = new_angle_index
        my_rover['Xpos'] = my_rover['Xpos'] + my_sensors.ANGLES_DX[new_angle_index]
        my_rover['Ypos'] = my_rover['Ypos'] + my_sensors.ANGLES_DY[new_angle_index]
        my_rover['TTL'] -= 1
        return my_rover


def make_new_msg(my_rover) :
        print("SENDING NEW MESSAGE")
        new_msg = "new," + my_rover['Name'] + ","+my_rover['Color'];
        return new_msg

async def hello():
    uri = "ws://localhost:8088"
    async with websockets.connect(uri) as websocket:
        my_rover = my_state.make_rover(name,color)
        setup_request =  make_new_msg(my_rover)
        print(setup_request)
        await websocket.send(setup_request)
        jsetup = await websocket.recv()
        setup = json.loads(jsetup)
        my_rover = my_state.add_setup_to_my_rover(my_rover,setup)

        bidx = 0
        while bidx < 100:
            print("TRY COUNT: ",bidx)
            my_rover = my_state.make_rover(name,color)
            brain = my_brains.make_brain()  # get initial brain
            while True:
                wall = 0;
                wall = my_sensors.check_position_borders(my_rover['Xpos'],my_rover['Ypos'],setup)
                #food
                if wall == setup['food'] :
                    my_rover['TTL'] += 10
                    print("GOOD FOOD TTL : ",my_rover['TTL'])

                if wall == setup['poison'] :
                    my_rover['Dead'] = 1
                    print("BAD WALL: ")

                if my_rover['TTL'] <= 0:
                    my_rover['Dead'] = 1
                    print("BAD TTL : ",my_rover['TTL'])

                if my_rover['Dead'] == 1:
                    brain = my_brains.reset_brain(brain,my_rover)
                    my_rover = my_state.make_rover(name,color)
                    reset_food(setup)
                else:
                    my_rover = my_sensors.get_sensor_data(my_rover,setup)
                    my_rover = think(brain,my_rover,setup)
                    
                    data_to_send = []
                    data_to_send.append(my_rover['Xpos'])
                    data_to_send.append(my_rover['Ypos'])
                    data_to_send.append(my_rover['Num_sensors'])
                    data_to_send += my_rover['Sensor_data']
                    sdata = [str(int) for int in data_to_send]
                    ssd = ",".join(sdata);
                    position_msg = "position,"+my_rover['Name'] + "," + ssd; await websocket.send(position_msg)

        bidx += 1
        print("AT BOTTOM TRY = ",bidx)
         
asyncio.get_event_loop().run_until_complete(hello())

