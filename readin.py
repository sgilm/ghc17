###  Google Hash Code 2017 - Popularity-Based Cache Allocation for P2P Video ###
### 2/23/2017 - Team Tony - Sam Gilmour x Kyle Hall ###


#latencies in latencies, fall back latencies in fallbackLatency, connections in connections, requests in requests, video sizes in videos, capacity in meta[4]


import sys, copy

#first line of file with meta details in order specified in problem
meta = []

#size of videos in milliseconds with ID = index
videos = []


#housekeeping
f = open('kittens.in', 'r')

#read first line, store in meta
meta = f.readline()
meta = meta.split()
for i in range(0, 5):
    meta[i] = int(meta[i])

#debug
#print(meta)


#latency from EP to Data Center with ID = Index, default set to sys.maxsize                                         
fallbackLatency = [sys.maxsize] * meta[1]

#latency from EP to Cache Server with latency[serverID][EndpointID] = latency from serverID to EndpointID, default set to sys.maxsize 
latencies = []

temp = [sys.maxsize] * meta[1]
for i in range(0, meta[3]):
    latencies.append(copy.deepcopy(temp))
#for i in range(0, len(latencies)):
 #   print(latencies[i])

#read next line, get size of videos 
videos = f.readline()
videos = videos.split()
for i in range(0, meta[0]):
    videos[i] = int(videos[i]) 

#debug
#print(videos)

#storing connections
connections = []
for i in range(0, meta[1]):
    connections.append([])

#processing endpoint data
i=0
while i < meta[1]:
    line = f.readline()
    line = line.split()
    #for j in range(0,2):
     #   line[j] = int(line[j])
    line[0] = int(line[0])
    line[1] = int(line[1])
    fallbackLatency[i] = line[0]
    k = line[1]
    j=0
    while j < k:
        line2 = f.readline()
        line2 = line2.split()
        line2[0] = int(line2[0])
        line2[1] = int(line2[1])
        serverindex = line2[0]
        line2.append(i)
 #       print(line2)
  #      print(i)
   #     print()
        
#        connections.append(line2)
        latencies[line2[0]][i] = line2[1]
        j=j+1
        connections[i].append(line2[0])
    i = i+1
#i=0
#for i in range(0,len(connections)):
 #   latencies[connections[i][0]][connections[i][2]] = connections[i][1]

#debug
#for i in range(0, len(latencies)):
 #   print(latencies[i])

#print(fallbackLatency)
#print(connections)

requests= []
#print(connections)
for i in range(0, meta[2]):
    line = f.readline()
    line = line.split()
    for j in range(0, len(line)):
        line[j] = int(line[j])
    requests.append(line)

#print(requests)
