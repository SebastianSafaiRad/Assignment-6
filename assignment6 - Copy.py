from graph import Graph
from graph import Vertex
from queue2050 import Queue
import math


class assignment6:

    def __init__(self, a_volume, b_volume, goal_amount):
        self.container_a = Container(a_volume)
        self.container_b = Container(b_volume)
        self.goal_amount = goal_amount
        self.graph = Graph()

    def findsolution(self, a, b, goal_amount):
        if goal_amount % math.gcd(a, b) == 0:
            return self.bfSearch(self.buildGraph())
        else:
            print("There is no solution")

    def getEligibleStates(self, a, b, curr_state):
        pass

    def buildGraph(self):
        q = Queue()
        graphVert = self.graph.addVertex("0,0")
        q.enqueue(graphVert)
        while not q.isEmpty():
            curr_node = q.dequeue()
            nodeid = curr_node.getId()
            idList = nodeid.split(",")
            self.container_a.setCurrVolume(int(idList[0]))
            self.container_b.setCurrVolume(int(idList[1]))
            if not self.container_a.isFull():
                self.container_a.fill()
                newVertex = Vertex(str(self.container_a.getCurrVolume()) + "," + idList[1])
                self.graph.addEdge(curr_node, newVertex)
                q.enqueue(newVertex)
                self.container_a.setCurrVolume(idList[0])
            if not self.container_b.isFull():
                self.container_b.fill()
                newVertex = Vertex(idList[0] + "," + str(self.container_b.getCurrVolume()))
                self.graph.addEdge(curr_node, newVertex)
                q.enqueue(newVertex)
                self.container_b.setCurrVolume(idList[1])
            if self.canPour(self.container_a, self.container_b):
                self.pour(self.container_a, self.container_b)
                newVertex = Vertex(self.container_a.getCurrVolume() + "," + self.container_b.getCurrVolume())
                self.graph.addEdge(curr_node, newVertex)
                q.enqueue(newVertex)
                self.container_a.setCurrVolume(idList[0])
            if self.canPour(self.container_b, self.container_a):
                self.pour(self.container_b, self.container_a)
                newVertex = Vertex(self.container_a.getCurrVolume() + "," + self.container_b.getCurrVolume())
                self.graph.addEdge(curr_node, newVertex)
                q.enqueue(newVertex)

            # return q

    def bfSearch(self, graph):
        visited = []
        queue = Queue()
        rootVertex = "0,0"  # this is just a string object, not a Vertex
        self.graph = graph  # this overwrites the class variable "graph" with the function parameter "graph"
                            # you don't need to do this, as you're passing the class variable in when you do
                            # the function call in "findSolution"

        # need to establish initial conditions for the queue
        # put an element on the queue before enterint the while loop
        # what are you doing with the loop control test here?
        while queue:
            d = queue.dequeue(0)
            for neighbor in graph(d):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.enqueue(neighbor)

        pass

    def pour(self, source, destination):
        maxAmountToPour = destination.max_volume - destination.curr_volume
        if source.curr_volume <= maxAmountToPour:
            destination.curr_volume = destination.curr_volume + source.curr_volume
            source.curr_volume = 0
        else:
            source.curr_volume = source.curr_volume - maxAmountToPour
            destination.curr_volume = destination.curr_volume + maxAmountToPour

    def canPour(self, source, destination):
        if source.isEmpty():
            return False
        elif destination.isFull():
            return False
        else:
            return True


class Container:
    max_volume = 0
    curr_volume = 0

    def __init__(self, max_volume):
        self.max_volume = max_volume

    def fill(self):
        self.curr_volume = self.max_volume

    def getCurrVolume(self):
        return self.curr_volume

    def getMaxVolume(self):
        return self.max_volume

    def setCurrVolume(self, volume):
        self.v = volume

    def isFull(self):
        if self.curr_volume == self.max_volume:
            return True
        else:
            return False

    def isEmpty(self):
        if self.curr_volume == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    g = Graph()
    kv = {}
    g.addEdge(0, 1)
    kv[0] = "0,0"
    kv[1] = "3,0"
    g.addEdge(0, 2)
    kv[2] = "0,4"
    g.addEdge(0, 3)
    kv[3] = "3,4"
    g.addEdge(1, 4)
    kv[4] = "0,3"
    g.addEdge(1, 5)
    kv[5] = "3,4"
    g.addEdge(2, 6)
    kv[6] = "3,1"
    print("all vertices :", g.getVertices())
    print("all kv dict entries : ", kv)
    v0 = g.getVertex(0)
    v1 = g.getVertex(1)
    print("v0 ID : ", v0.getId())
    print("v1 ID : ", v1.getId())
    print("v0 connections : ", v0.getConnections())
    print("v1 connections : ", v1.getConnections())
    for v in v0.getConnections():
        print("v0 connection ID : ", v.getId())
        print("v0 connection value : ", kv[v.getId()])
    for v in v1.getConnections():
        print("v1 connection ID : ", v.getId())
        print("v1 connection value : ", kv[v.getId()])
