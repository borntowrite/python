##Write an algorithm (i.e., step-by-step instructions) via
##which someone could walk or drive from some origin to
##some destination, perhaps a path that you yourself tend
##to travel. Take care to specify what the origin and destination
##that you have in mind. And take care to use loops and
##conditions as needed, particularly if there might be obstacles (e.g., red lines).
##Assume that your algorithm will be executed by a robot (or lost friend)
##who will follow your directions precisely.

##########################
# Using Binary Search Tree & Stack 
##########################
from collections import defaultdict

class Route:
    def __init__(self, total_route):
        self.total_route=total_route
        self.route=defaultdict(list)
    def addRoute(self, u, v):
        self.route[u].append(v)
    def findPath(self, u, d, visited, path):
        visited[u]=True
        path.append(u)
        ########################
        #                        2
        #         0                                  1
        # 1       3       4                            3
        # 3       5       6                               5
        # 5       6                                           6
        # 6
        ########################
        if u==d: 
            print("arrive destination : ", path)
        else:
            print("current position : ", u)
            for i in self.route[u]: 
                if visited[i]==False:
                    print(path)
                    self.findPath(i,d,visited,path)
        ######################
        path.pop()
        print("pop if visited :", u)
        visited[u]=False
    def printAllPaths(self, origin,destination):
        visited=[False]*(self.total_route)
        path=[]
        self.findPath(origin, destination, visited, path)

#create route
#0 --> 1,2,3,4
#1 --> 3
#2 --> 0,1
#3 --> 5
#4 --> 6
#5 --> 6

r = Route(7)
r.addRoute(0, 1)
r.addRoute(0, 2)
r.addRoute(0, 3)
r.addRoute(0, 4)
r.addRoute(2, 0)
r.addRoute(2, 1)
r.addRoute(1, 3)
r.addRoute(3, 5)
r.addRoute(5, 6)
r.addRoute(4, 6)

origin = 2
destination = 6
print ("All paths from %d to %d :" %(origin, destination))
r.printAllPaths(origin, destination)

###############################
#gps client
###############################
##from gps3 import gps3
##gps_socket = gps3.GPSDSocket()
##data_stream = gps3.DataStream()
##gps_socket.connect()
##gps_socket.watch()
##for new_data in gps_socket:
##    if new_data:
##        data_stream.unpack(new_data)
##        print('Altitude = ', data_stream.TPV['alt'])
##        print('Latitude = ', data_stream.TPV['lat'])

##import os
##from gps import *
##from time import *
##import time
##import threading
##
##import gpsd
##gpsd.connect()
##packet = gpsd.get_current()
##print(packet.position())

###############################
# socket server
###############################
##import socket
##s = socket.socket()
##host = socket.gethostname()
##port = 1234
##s.bind((host, port))
##s.listen(5)
##while True:
##        c, addr = s.accept()
##        print('Got connection from', addr)
##        c.close()

###############################
# socket client (run from apache folder / htdoc
###############################
##s = socket.socket()
##host = socket.gethostname()
##port = 1234
##s.connect((host, port))
##print(s.recv(1024))








