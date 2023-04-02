import numpy as np
import csv
import tsp_genetic

cities = []
sol = []

def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist

def getDistanceList():
    global dist
    dist = [[None] * len(cities) for _ in range(len(cities))]
    for i in range(len(cities)):
        for j in range(len(cities)):
            dist[i][j] = distance([cities[i][0], cities[i][1]], [cities[j][0], cities[j][1]])
    return dist

def getCities():
    return cities

with open('example_solution.csv', mode='r', newline='') as solution:

    reader = csv.reader(solution)
    for row in reader:
        sol.append(int(row[0]))
    
    idx = sol.index(0)

    front = sol[idx:]
    back = sol[0:idx]

    sol = front + back
    
    sol.append(int(0))

with open('2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(list(map(float, row)))


total_cost = 0

for idx in range(len(sol)-1):

    pos_city_1 = [cities[sol[idx]][0], cities[sol[idx]][1]]
    pos_city_2 = [cities[sol[idx+1]][0], cities[sol[idx+1]][1]]

    dist = distance(pos_city_1, pos_city_2)

    total_cost += dist

print('final cost: ' + str(total_cost))