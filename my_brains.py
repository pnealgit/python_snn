import random
import copy

brains = []
NUM_BRAINS = 10
NUM_NEURONS = 12
def reset_brain(brain,my_rover) :
     print("BRAIN DEAD FITNESS : ",brain['Fitness']," TTL: ",my_rover['TTL'])
     if len(brains) < NUM_BRAINS :
         brains.append(brain)
         brain = make_brain()
         return brain
     else:
         #sort brains by fitness
         brains.sort(key=lambda b: b['Fitness'],reverse=True)
         print("\nSORTED BRAINS")
         for bb in range(0,len(brains)) :
             print(brains[bb]['Fitness'])
         print("\n")
         #replace less fit
         if brains[NUM_BRAINS-1]['Fitness'] < brain['Fitness']:
             brains.pop();
             brains.append(brain)


         #get elite
         newidx = random.randrange(0,4) # 4 is arbitrary
         brain = copy.deepcopy(brains[newidx])
         brain = mutate(brain)
         return brain

def make_brain() :
    brain = {}
    brain['Fitness'] = 0.0
    brain['Num_neurons'] = NUM_NEURONS 

    xsign = [0]*NUM_NEURONS
    for ix in range(0,NUM_NEURONS):
        xsign[ix] = random.randrange(0,2)
        brain['xsign'] = xsign
        iconn = [[1]*NUM_NEURONS for i in range(NUM_NEURONS)]
        brain['iconn'] = iconn
        nconn = [[0]*NUM_NEURONS for i in range(NUM_NEURONS)]
        for ix in range(0,NUM_NEURONS):
            for iy in range(0,NUM_NEURONS):
                nconn[ix][iy] = random.randrange(0, 2)

        brain['nconn'] = nconn
    return brain

def mutate(brain):
    brain['Fitness'] = 0.0
    #start mutations here ...
    NUM_NEURONS = brain['Num_neurons']
    mutidx = random.randrange(0,NUM_NEURONS)
    if brain['xsign'][mutidx] == 0 :
        brain['xsign'][mutidx] = 1
    else :
        brain['xsign'][mutidx] = 0

    mutidx = random.randrange(0,NUM_NEURONS)
    ilink = random.randrange(0,NUM_NEURONS)
    if brain['nconn'][mutidx][ilink] == 0 :
        brain['nconn'][mutidx][ilink] = 1
    else :
        brain['nconn'][mutidx][ilink] = 0

   #might not want to do this.
    #lets keep all input signals

    mutidx = random.randrange(0,NUM_NEURONS)
    ilink = random.randrange(0,NUM_NEURONS)
    if brain['iconn'][mutidx][ilink] == 0 :
       brain['iconn'][mutidx][ilink] = 1
    else :
        brain['iconn'][mutidx][ilink] = 0

    return brain


