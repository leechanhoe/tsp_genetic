import random as rd
import chart
import map
import data
import time

gen = 0
best = 100000000
start = time.time()
m=map.loadMap()


while True:
    gen+=1

    dist = data.getDistanceList()
    solv = rd.sample(range(0, 1000), 1000)
    solvDist = 0

    for i in range(1,1000):
        solvDist+=dist[solv[i-1]][solv[i]]