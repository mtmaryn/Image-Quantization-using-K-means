#lib
import math
import time
from PIL import Image

picture = "ch.jpg"

#Functions
def printHello():
    print "Hello World"

def getPixels(d):
    print "Starting..."
    im = Image.open(picture)
    pix = im.load()

    print im.size
    width, height = im.size

    for i in range(0, width):
        if i % 100 == 0:
            print "Working..."
        for j in range(0, height):
            if pix[i,j] in d:
                d[pix[i,j]] = d[pix[i,j]] + 1
            else:
                d[pix[i,j]] = 1;
                
    print "This image uses %d colors" % len(d)
    print "///////////////////////////////////////////////////////////////////"
    print "Please Wait..."
    print "///////////////////////////////////////////////////////////////////"

def newImage(points,centers):
    print "Starting..."
    timer = 0
    im = Image.open(picture)
    pix = im.load()
    #d = {}
    print im.size
    width, height = im.size
    for i in range(0, width):
        print "Working... %d" % i
        for j in range(0, height):
            for k in range(0, len(points)):
                x,y,z,d,c = points[k]
                if pix[i,j] == (x,y,z):
                    x1,y1,z1,b = centers[c]
                    pix[i,j] = (x1,y1,z1)
                    timer = timer + 1
                    break
    im.save("new.jpg")
    print "Done"

def newImage2(points,centers):
    print "Starting..."
    timer = 0
    im = Image.open(picture)
    pix = im.load()
    #d = {}
    sortPoints(points)
    print im.size
    width, height = im.size
    for i in range(0, width):
        print "Working... %d" % i
        for j in range(0, height):
            noe = binary_search(points,pix[i,j])
            #print noe
            x1,y1,z1,b = centers[noe]
            pix[i,j] = (x1,y1,z1)                 
    im.save("new.jpg")
    print "Done"
    
def sortPoints(array):
    array.sort()

def binary_search(array,target):
    #set limits
    lower = 0
    upper = len(array)
    #print "Searching..."
    while lower < upper:
        x = (upper + lower)/2
        x1,y1,z1,d,c = array[x]
        val = x1,y1,z1
        #print x,val
        if target == val:
            return c
        elif target > val:
            lower = x
        elif target < val:
            upper = x
        else:
            return 0

def printThis(array):
    newList = []
    for i in range(0,len(array)):
        x,y = array[i]
        newList.append(x)
    return newList

def printClusters(points, centers, num):
    for i in range(0,num):
        print "Cluster %d -- %s" % (i, centers[i])
        #for j in range(0, len(points)):
            #x,y,z,d,c = points[j]
            #if c == i:
                #print "(%d,%d,%d)" % (x, y, z)

def findDistance(first, second):
    x1,y1,z1,d,c = first
    x2,y2,z2,b = second
    deltaX = x1 - x2
    X = deltaX * deltaX
    deltaY = y1 - y2
    Y = deltaY * deltaY
    deltaZ = z1 - z2
    Z = deltaZ * deltaZ
    d = math.sqrt(X + Y + Z)
    answer = d
    return answer

def kMeans(points, centers, num):
    for i in range(0,len(points)):
        x1,y1,z1,d,c = points[i]
        points[i] = (x1,y1,z1,99999999,c)
    for i in range(0,num):
        #print "Cluster %d: " % i
        for j in range(0, len(points)):
            tempDist = findDistance(points[j],centers[i])
            x1,y1,z1,d,c = points[j]
            #print points[j]
            if(d > tempDist):
                #print tempDist
                d = tempDist
                #print d
                c = i
            points[j] = (x1,y1,z1,d,c)
            #print points[j]

    return points

def findCenters(points, centers, num):
    for i in range(0,num):
        totalX = 0
        totalY = 0
        totalZ = 0
        resultX = 0
        resultY = 0
        resultZ = 0
        tempX, tempY, tempZ, tempB = centers[i]
        x2,y2,z2,b = centers[i]
        cntr = 0
        for j in range(0,len(points)):
            x1,y1,z1,d,c = points[j]
            if c == i:
                totalX = totalX + x1
                totalY = totalY + y1
                totalZ = totalZ + z1
                cntr = cntr + 1
        resultX = totalX/cntr
        resultY = totalY/cntr
        resultZ = totalZ/cntr
        x2 = resultX
        y2 = resultY
        z2 = resultZ
        if tempX >= x2 & tempY == y2 & tempZ == y2:
            b = False
        else:
            b = True
        centers[i] = (x2,y2,z2,b)
    return centers
                
def findCenter(first, second):
    x1,y1,z1,d,c = first
    x2,y2,z2,b = second
    deltaX = x1 - x2
    deltaY = y1 - y2
    deltaZ = z1 - z2
    x1 = x1 - deltaX/2.0
    y1 = y1 - deltaY/2.0
    z1 = z1 - deltaZ/2.0
    answer = (x1,y1,z1)
    return answer

def findDistanceFromCenter(points, centers):
    for i in range(0,len(points)):
        x,y,z,d,c = points[i]
        points[i] = findDistance(points[i],centers[c])
    return points

def initClusters(num):
    centers = []
    for i in range(0,num):
        x1,y1,z1,d,c = points[i]
        centers.append((x1,y1,z1, True))
    return centers

def done(centers, num):
    for i in range(0,num):
        x,y,z,b = centers[i]
        if b == True:
            return False
    return True            

#Main Loop
#Format for points (X, Y, Z, distance from center, what cluster number)
d= {}
points = []
getPixels(d)
for key,value in d.iteritems():
    x1,y1,z1 = key
    n = (x1,y1,z1,0,0)
    points.append(n)
#points = [(2,10,0,0,0),(2,5,0,0,0),(8,4,-1,0,0),(5,8,5,0,0),(7,5,3,0,0),(6,4,6,0,0),(1,2,2,0,0),(4,9,8,0,0)]
clusterNum = raw_input("How many clusters? ")
start_time = time.time()
num = int(clusterNum)
centers = initClusters(num)
max = 0
print "Loading..."
while done(centers,num) == False:
    max = max + 1
    #print points
    points = kMeans(points, centers, num)
    #print points
    centers = findCenters(points, centers, num)
    if max % 50 == 0:
        percent = max*100/100;
        print "Loading...%d percent" % percent
    if(max == 100): 
        break
#print points
printClusters(points, centers, num)
newImage2(points,centers)
print("--- %s seconds ---" % (time.time() - start_time))
