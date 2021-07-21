import random
def make_rover(name,color) :
    my_rover = {}
    sensor_length = 60

    my_rover['Xpos'] = random.randrange(10,100)
    my_rover['Ypos'] = random.randrange(10,100)
    my_rover['Name'] = name
    my_rover['Color'] = color
    my_rover['Velocity'] = 1
    my_rover['Angle_index'] = random.randrange(0,8)
    my_rover['Old_angle_index'] = random.randrange(0,8)
    my_rover['Sensor_angle'] = random.randrange(0,8)
    my_rover['Sensor_length'] = sensor_length
    my_rover['Sensor_data'] = []
    my_rover['Binary_sensor_data'] = []
    my_rover['Time_to_live'] = 1000
    my_rover['Dead'] = 0
    my_rover['Fitness'] = 0.0
    my_rover['TTL'] = 2000
    my_rover['Num_sensors'] = 3
    my_rover['Num_angles'] = 8
    my_rover['Num_brains'] = 10

    #print("IN MAKE_ROVER: ",my_rover)
    return my_rover

