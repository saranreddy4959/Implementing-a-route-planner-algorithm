from math import sqrt



def shortest_path(M,start,goal):
   #initialising the frontier as a set I used sets because there will be no duplicates in it and intialising it with start
    frontier = set([start])
    #intialising the explored as an empty set
    explored = set()
    
    #Here I am creating a dictionary to keep track of the paths and its values 
    starting_path = {
            "nodeValue":start,  #node value to know at which node it is 
            "coordinate_values":M.intersections[start], #cordinate values to point the exact location of node 
            "parent":False,  #parent node to determine the value of parent initially it is defined as false 
            "g":0,   #to determine the distnce from the starting point
            "cost":distance(M.intersections[start], M.intersections[goal]) #total cost to reach the goal point 
    }
    road_path = {start:starting_path} 
    
 
    while frontier:
        #to find the cheapest node 
        cheapNode = next(iter(frontier))
        for node in frontier:
            #it compares the cost between two nodes  
            if road_path[node]["cost"] < road_path[cheapNode]["cost"]:
                cheapNode = node
            #now we get the cheapest path from the cheapest node
        cheapest_path = road_path[cheapNode]
        
   #From the cheapest path we will be getting the next interections points for that node so that we will be getting a newfrontier
        #in the roads we will the points which are to be frontiers
        roads = set(M.roads[cheapest_path["nodeValue"]]) - explored
        frontier = frontier.union(roads)
        #in this we are keeping track of explored nodes 
        explored.add(cheapest_path["nodeValue"])
        #here we are removing the explored nodes from the frontier
        frontier.remove(cheapest_path["nodeValue"])
        
        
        for node in roads:
            #to keep store the parent value for the node 
            parent = cheapest_path["nodeValue"]
            #here we calculate the distance from the start node
            g = cheapest_path["g"] + distance(M.intersections[node], M.intersections[parent]) 
            #calculating the heuristic distance from that node to the goal
            h = distance(M.intersections[node], M.intersections[goal])
            #f is the total cost of the path 
            f = g + h
            #we are assigning the values of that particular node in a dictionary to keep track for all the nodes covered
            if node not in road_path or f < road_path[node]["cost"]:
                road_path[node] = {
                    "nodeValue":node,
                    "coordinates_values":M.intersections[node],
                    "parent":parent,
                    "g":g,
                    "cost":f 
                }
        #when the goal is reached we add all the nodes to a list by using the parent value for the node 
        if cheapest_path["nodeValue"] == goal:
            finalList = [goal]
            node = goal
            while road_path[node]["parent"]:
                finalList.insert(0,road_path[node]["parent"])
                node = road_path[node]["parent"]
            return finalList
        
    
    return "there is no path to the goal"
    
    return

#to calculate the distance between two points 
def distance(node1,node2):

    a = node2[0]-node1[0]
    b = node2[1]-node1[1]
    z=sqrt(a*a + b*b)
    return z