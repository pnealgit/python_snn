import random

brain = {}
brain['fitness'] = 0.0
xsign = [0]*8
for ix in range(0,8):
    xsign[ix] = random.randrange(0,2)
brain['xsign'] = xsign
iconn = [1]*8
brain['iconn'] = iconn
nconn = [ [0]*8 for i in range(8)]
for ix in range(0,8):
    for iy in range(0,8):
        nconn[ix][iy] = random.randrange(0, 2)
print("NCONN: ",nconn)

brain['nconn'] = nconn
print("FINAL BRAIN: ",brain)

